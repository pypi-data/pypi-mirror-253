from __future__ import annotations

import asyncio
from contextlib import suppress
from typing import Dict, Any, Union, Optional

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    BufferedInputFile,
    InlineKeyboardMarkup,
    Message,
)
from aiogram.utils.markdown import hide_link
from redis.asyncio import Redis

from pytonconnect.exceptions import (
    UserRejectsError,
    WalletNotConnectedError,
)

from .tonconnect import AiogramTonConnect
from .tonconnect.storage import (
    ConnectWalletCallbackStorage,
    SendTransactionCallbackStorage,
    TaskStorage,
)
from .tonconnect.models import (
    AccountWallet,
    AppWallet,
    ConnectWalletCallbacks,
    SendTransactionCallbacks,
    Transaction,
    ATCUser,
)
from .utils.exceptions import (
    LanguageCodeNotSupported,
    MESSAGE_DELETE_ERRORS,
    MESSAGE_EDIT_ERRORS,
)
from .utils.keyboards import InlineKeyboardBase
from .utils.qrcode import QRCode
from .utils.states import TcState
from .utils.texts import TextMessageBase


class ATCManager:
    """
    Manager class for AiogramTonConnect integration.

    :param user: The AiogramTonConnect user.
    :param redis: Redis instance for storage.
    :param tonconnect: AiogramTonConnect instance.
    :param qrcode_type: Type for the QR code, `url` or `bytes`.
    :param qrcode_base_url: Base URL for generating the QR code (for qrcode_type `url`).
    :param text_message: TextMessageBase class for managing text messages.
    :param inline_keyboard: InlineKeyboardBase class for managing inline keyboards.
    :param data: Additional data.
    :param emoji: Emoji string. Defaults to "💎".
    """

    def __init__(
            self,
            user: ATCUser,
            redis: Redis,
            tonconnect: AiogramTonConnect,
            qrcode_type: str,
            qrcode_base_url: str,
            text_message: TextMessageBase,
            inline_keyboard: InlineKeyboardBase,
            data: Dict[str, Any],
            emoji: str = "💎",
    ) -> None:
        self.user: ATCUser = user
        self.redis: Redis = redis
        self.tonconnect: AiogramTonConnect = tonconnect

        self.__qrcode_type: str = qrcode_type
        self.__qrcode_base_url: str = qrcode_base_url
        self.__text_message: TextMessageBase = text_message
        self.__inline_keyboard: InlineKeyboardBase = inline_keyboard

        self.bot: Bot = data.get("bot")
        self.state: FSMContext = data.get("state")

        self.__data: Dict[str, Any] = data
        self.__emoji: str = emoji

        self.task_storage = TaskStorage(user.id)
        self.connect_wallet_callbacks_storage = ConnectWalletCallbackStorage(redis, user.id)
        self.send_transaction_callbacks_storage = SendTransactionCallbackStorage(redis, user.id)

    @property
    def middleware_data(self) -> Dict[str, Any]:
        """
        Get middleware data.
        """
        return self.__data

    async def update_interfaces_language(self, language_code: str) -> None:
        """
        Update interfaces language.

        :param language_code: The language code to update to.
        :raise LanguageCodeNotSupported: If the provided language code is not supported.
        """
        if (
                language_code in self.__text_message.texts_messages and
                language_code in self.__inline_keyboard.texts_buttons
        ):
            await self.state.update_data(language_code=language_code)
            self.user.language_code = language_code
            self.__text_message.language_code = self.__inline_keyboard.language_code = language_code
            return None

        raise LanguageCodeNotSupported(
            f"Language code '{language_code}' not in text message or button text"
        )

    async def connect_wallet(
            self, callbacks: Optional[ConnectWalletCallbacks] = None,
            button_wallet_width: int = 2,
    ) -> None:
        """
        Open the connect wallet window.

        :param callbacks: Callbacks to execute.
        :param button_wallet_width: The width of the wallet buttons in the inline keyboard.
        """
        if self.__qrcode_type == "bytes":
            await self.send_message(self.__emoji)

        if self.tonconnect.connected:
            await self.disconnect_wallet()

        if callbacks:
            await self.connect_wallet_callbacks_storage.add(callbacks)

        state_data = await self.state.get_data()
        wallets = await self.tonconnect.get_wallets()

        app_wallet_dict = state_data.get("app_wallet") or wallets[0].to_dict()
        app_wallet = AppWallet.from_dict(app_wallet_dict)

        universal_url = await self.tonconnect.connect(app_wallet.to_dict())
        await self.state.update_data(app_wallet=app_wallet.to_dict())

        task = asyncio.create_task(self.__wait_connect_wallet_task())
        self.task_storage.add(task)

        reply_markup = self.__inline_keyboard.connect_wallet(
            wallets, app_wallet, universal_url,
            wallet_name=app_wallet.name,
            width=button_wallet_width,
        )
        text = self.__text_message.get("connect_wallet").format(
            wallet_name=app_wallet.name
        )
        await self._send_connect_wallet_window(text, reply_markup, universal_url, app_wallet)
        await self.state.set_state(TcState.connect_wallet)

    async def _send_connect_wallet_window(
            self,
            text: str,
            reply_markup: InlineKeyboardMarkup,
            universal_url: str,
            app_wallet: AppWallet,
    ) -> None:
        """
        Send the connect wallet window with appropriate content based on the qrcode_type.

        :param text: The text message to be sent.
        :param reply_markup: The inline keyboard markup for the message.
        :param universal_url: The universal URL for connecting the wallet.
        :param app_wallet: The AppWallet instance representing the connected wallet.
        """
        if self.__qrcode_type == "bytes":
            photo = await QRCode.create_connect_wallet_image(
                universal_url, app_wallet.image
            )
            await self._send_photo(
                photo=BufferedInputFile(photo, "qr.png"),
                caption=text,
                reply_markup=reply_markup,
            )
        else:
            qrcode_url = QRCode.create_connect_wallet_url(
                universal_url, self.__qrcode_base_url, app_wallet.image
            )
            await self.send_message(
                text=hide_link(qrcode_url) + text,
                reply_markup=reply_markup,
            )

    async def disconnect_wallet(self) -> None:
        """
        Disconnect the connected wallet.
        """
        with suppress(WalletNotConnectedError):
            await self.tonconnect.restore_connection()
            await self.tonconnect.disconnect()

    async def send_transaction(
            self,
            callbacks: Optional[SendTransactionCallbacks] = None,
            transaction: Optional[Transaction] = None,
    ) -> None:
        """
        Open the send transaction window.

        :param callbacks: Callbacks to execute.
        :param transaction: The transaction details.
        """
        if transaction:
            await self.state.update_data(transaction=transaction.to_dict())

        if callbacks:
            await self.send_transaction_callbacks_storage.add(callbacks)

        task = asyncio.create_task(self.__wait_send_transaction_task())
        self.task_storage.add(task)

        text = self.__text_message.get("send_transaction").format(
            wallet_name=self.user.app_wallet.name,
        )
        universal_url = self.user.app_wallet.universal_url
        if self.user.app_wallet.app_name == "telegram-wallet":
            universal_url = universal_url.replace(
                "attach=wallet", "startattach=tonconnect-ret__back"
            )
        reply_markup = self.__inline_keyboard.send_transaction(
            self.user.app_wallet.name, universal_url,
        )

        await self.send_message(text=text, reply_markup=reply_markup)
        await self.state.set_state(TcState.send_transaction)

    async def _connect_wallet_timeout(self) -> None:
        """
        Handle the connect wallet timeout.
        """
        text = self.__text_message.get("connect_wallet_timeout")
        reply_markup = self.__inline_keyboard.send_transaction_timeout()

        await self.send_message(text=text, reply_markup=reply_markup)
        await self.state.set_state(TcState.connect_wallet_timeout)

    async def _send_transaction_timeout(self) -> None:
        """
        Handle the send transaction timeout.
        """
        text = self.__text_message.get("send_transaction_timeout")
        reply_markup = self.__inline_keyboard.send_transaction_timeout()

        await self.send_message(text=text, reply_markup=reply_markup)
        await self.state.set_state(TcState.send_transaction_timeout)

    async def _send_transaction_rejected(self) -> None:
        """
        Handle the send transaction rejection.
        """
        text = self.__text_message.get("send_transaction_rejected")
        reply_markup = self.__inline_keyboard.send_transaction_rejected()

        await self.send_message(text=text, reply_markup=reply_markup)
        await self.state.set_state(TcState.send_transaction_rejected)

    async def _send_photo(
            self,
            photo: Any,
            caption: Optional[str] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Message:
        """
        Send a photo to the user.

        :param photo: The photo to send.
        :param caption: The caption for the photo.
        :param reply_markup: Optional InlineKeyboardMarkup for the message.
        :return: Sent Message object.
        :raises TelegramBadRequest: If there is an issue with sending the photo.
        """
        message = await self.bot.send_photo(
            chat_id=self.user.id,
            photo=photo,
            caption=caption,
            reply_markup=reply_markup,
        )
        await self._delete_previous_message()
        await self.state.update_data(message_id=message.message_id)
        return message

    async def send_message(
            self,
            text: str,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Message:
        """
        Send or edit a message to the user.

        This method attempts to edit the existing message identified by the stored message ID. If editing is not
        possible (e.g., due to a message not found error), it sends a new message and deletes the previous one.

        :param text: The text content of the message.
        :param reply_markup: Optional InlineKeyboardMarkup for the message.
        :return: The edited or sent Message object.
        :raises TelegramBadRequest: If there is an issue with sending or editing the message.
        """
        state_data = await self.state.get_data()
        message_id = state_data.get("message_id", None)

        try:
            message = await self.bot.edit_message_text(
                text=text,
                chat_id=self.user.id,
                message_id=message_id,
                reply_markup=reply_markup,
            )
        except TelegramBadRequest as ex:
            if not any(e in ex.message for e in MESSAGE_EDIT_ERRORS):
                raise ex
            message = await self.bot.send_message(
                text=text,
                chat_id=self.state.key.chat_id,
                reply_markup=reply_markup,
            )
            await self._delete_previous_message()
        await self.state.update_data(message_id=message.message_id)

        return message

    async def _delete_previous_message(self) -> Union[Message, None]:
        """
        Delete the previous message.

        This method attempts to delete the previous message identified by the stored message ID. If deletion is not
        possible (e.g., due to a message not found error), it attempts to edit the previous message with a placeholder
        emoji. If editing is also not possible, it raises TelegramBadRequest with the appropriate error message.

        :return: The edited Message object or None if no previous message was found.
        :raises TelegramBadRequest: If there is an issue with deleting or editing the previous message.
        """
        state_data = await self.state.get_data()

        message_id = state_data.get("message_id")
        if not message_id: return  # noqa:E701

        try:
            await self.bot.delete_message(
                message_id=message_id,
                chat_id=self.user.id,
            )
        except TelegramBadRequest as ex:
            if any(e in ex.message for e in MESSAGE_DELETE_ERRORS):
                try:
                    return await self.bot.edit_message_text(
                        message_id=message_id,
                        chat_id=self.user.id,
                        text=self.__emoji,
                    )
                except TelegramBadRequest as ex:
                    if not any(e in ex.message for e in MESSAGE_EDIT_ERRORS):
                        raise ex

    async def __wait_connect_wallet_task(self) -> None:
        """
        Wait for the connect wallet task.

        This method checks the AiogramTonConnect connection status periodically for up to 3 minutes (360 iterations).
        If the connection is restored, it updates the account wallet details, executes the appropriate callbacks,
        and removes the task from the task storage. If the connection is not restored within the timeout, it
        triggers the connect wallet timeout handling.

        :raises asyncio.CancelledError: If the task is cancelled.
        :raises Exception: Any unexpected exception during the process.
        """
        try:
            for _ in range(1, 361):
                await asyncio.sleep(.5)
                if self.tonconnect.connected:
                    state_data = await self.state.get_data()
                    app_wallet = AppWallet.from_dict(state_data.get("app_wallet"))
                    account_wallet = AccountWallet(
                        address=self.tonconnect.account.address,
                        state_init=self.tonconnect.account.wallet_state_init,
                        public_key=self.tonconnect.account.public_key,
                        chain=self.tonconnect.account.chain,
                    )

                    self.middleware_data["account_wallet"] = account_wallet
                    self.middleware_data["app_wallet"] = app_wallet
                    await self.state.update_data(account_wallet=account_wallet.to_dict())

                    callbacks = await self.connect_wallet_callbacks_storage.get()
                    await callbacks.after_callback(**self.middleware_data)
                    break
            else:
                await self._connect_wallet_timeout()

        except asyncio.CancelledError:
            pass
        except Exception:
            raise
        finally:
            self.task_storage.remove()
        return

    async def __wait_send_transaction_task(self) -> None:
        """
        Wait for the send transaction task.

        This method waits for the Tonconnect to send a transaction within a timeout of 5 minutes. If the transaction
        is sent successfully, it updates the user's last transaction details, executes the appropriate callbacks, and
        removes the task from the task storage. If the user rejects the transaction, it triggers the send transaction
        rejection handling. If the transaction is not sent within the timeout, it triggers the send transaction
        timeout handling.

        :raises UserRejectsError: If the user rejects the transaction.
        :raises asyncio.TimeoutError: If the transaction is not sent within the timeout.
        :raises asyncio.CancelledError: If the task is cancelled.
        :raises Exception: Any unexpected exception during the process.
        """
        try:
            await self.tonconnect.restore_connection()
            await self.tonconnect.unpause_connection()

            data = await self.state.get_data()
            transaction = data.get("transaction")

            result = await asyncio.wait_for(
                self.tonconnect.send_transaction(transaction=transaction),
                timeout=300,
            )
            if result:
                last_transaction_boc = result.get("boc")
                self.user.last_transaction_boc = last_transaction_boc
                await self.state.update_data(last_transaction_boc=last_transaction_boc)

                callbacks = await self.send_transaction_callbacks_storage.get()
                self.middleware_data["boc"] = last_transaction_boc
                await callbacks.after_callback(**self.middleware_data)

        except UserRejectsError:
            current_state = await self.state.get_state()

            if current_state != TcState.send_transaction.state:
                return None
            await self._send_transaction_rejected()

        except asyncio.TimeoutError:
            current_state = await self.state.get_state()

            if current_state != TcState.send_transaction.state:
                return None
            await self._send_transaction_timeout()

        except asyncio.CancelledError:
            pass
        except Exception:
            raise
        finally:
            self.tonconnect.pause_connection()
            self.task_storage.remove()
        return
