from __future__ import annotations

__all__ = (
    "AbstractButton",
    "Action",
    "URL",
    "Submenu",
    "Back",
)

import asyncio
from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING

from yatbaf.handler import Handler
from yatbaf.types import InlineKeyboardButton

from .filter import CallbackPayload

if TYPE_CHECKING:
    from collections.abc import Awaitable
    from collections.abc import Callable

    from yatbaf import OnCallbackQuery

    from .menu import Menu
    from .payload import Payload
    from .typing import Query


class AbstractButton(ABC):
    __slots__ = ()

    @abstractmethod
    def _init(
        self, menu: Menu, router: OnCallbackQuery, payload: Payload, /
    ) -> None:
        pass

    @abstractmethod
    async def _build(self, q: Query, /) -> InlineKeyboardButton | None:
        pass


class BaseButton(AbstractButton):
    __slots__ = (
        "_title",
        "_dynamic_title",
        "_show",
    )

    def __init__(
        self,
        *,
        title: str | Callable[[Query], Awaitable[str]],
        show: Callable[[Query], Awaitable[bool]] | None = None,
    ) -> None:
        self._title = title
        self._show = show

    def __repr__(self) -> str:
        title = self._title or "`dynamic`"
        return f"<{self.__class__.__name__}[{title=!r}]>"

    async def _get_title(self, q: Query, /) -> str:
        if callable(self._title):
            return await self._title(q)
        return self._title

    async def _is_visible(self, q: Query, /) -> bool:
        if self._show is not None:
            return await self._show(q)
        return True


class Action(BaseButton):
    """This button does the action"""
    __slots__ = (
        "_action",
        "_payload",
    )

    def __init__(
        self,
        *,
        title: str | Callable[[Query], Awaitable[str]],
        action: Callable[[Query], Awaitable[None]],
        show: Callable[[Query], Awaitable[bool]] | None = None,
    ) -> None:
        """
        :param title: String or Callable which returns button title.
        :param action: Callable to run on click. Must be unique for the menu.
        :param show: *Optional.* Callable which returns visibility status.
        """
        super().__init__(
            title=title,
            show=show,
        )
        self._action = action
        self._payload: str | None = None

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Action) and (  # yapf: disable
            other is self or (
                other._action is self._action
                and other._title == self._title
                and other._show == self._show
            )
        )

    def _init(self, m: Menu, r: OnCallbackQuery, payload: Payload, /) -> None:
        if self._payload is not None:
            raise ValueError(
                f"{self!r} button must be unique to the entire menu."
            )

        self._payload = payload.get()
        handler = Handler(
            self._action,
            update_type=r._update_type,
            filters=[CallbackPayload(self._payload)],
        )
        if handler in r._handlers:
            raise ValueError(f"{self!r} `action` must be unique to menu.")

        r.add_handler(handler)

    async def _build(self, q: Query, /) -> InlineKeyboardButton | None:
        if not await self._is_visible(q):
            return None

        return InlineKeyboardButton(
            text=await self._get_title(q),
            callback_data=self._payload,
        )


class URL(BaseButton):
    """This button will open URL"""
    __slots__ = (
        "_url",
        "_dynamic_url",
    )

    def __init__(
        self,
        title: str | Callable[[Query], Awaitable[str]],
        url: str | Callable[[Query], Awaitable[str]],
        show: Callable[[Query], Awaitable[bool]] | None = None,
    ) -> None:
        """
        :param url: String or Callable which returns url.
        :param title: String or Callable which returns button title.
        :param show: *Optional.* Callable which returns visibility status.
        """
        super().__init__(
            title=title,
            show=show,
        )
        self._url = url

    def __eq__(self, other: object) -> bool:
        return isinstance(other, URL) and (  # yapf: disable
            other is self or (
                other._title == self._title
                and other._url == self._url
                and other._show == self._show
            )
        )

    def _init(self, m: Menu, r: OnCallbackQuery, p: Payload, /) -> None:
        pass  # nothing to do

    async def _get_url(self, q: Query, /) -> str:
        if callable(self._url):
            return await self._url(q)
        return self._url

    async def _build(self, q: Query, /) -> InlineKeyboardButton | None:
        if not await self._is_visible(q):
            return None

        async with asyncio.TaskGroup() as tg:
            title = tg.create_task(self._get_title(q))
            url = tg.create_task(self._get_url(q))

        return InlineKeyboardButton(
            text=title.result(),
            url=url.result(),
        )


class Submenu(BaseButton):
    """This button will open next menu"""
    __slots__ = (
        "_menu",
        "_payload",
    )

    def __init__(
        self,
        *,
        menu: str,
        title: str | Callable[[Query], Awaitable[str]],
        show: Callable[[Query], Awaitable[bool]] | None = None,
    ) -> None:
        """
        :param menu: Submenu name (see :class:`~yatbaf_menu.menu.Menu`).
        :param title: String or Callable which returns button title.
        :param show: *Optional.* Callable which returns visibility status.
        """
        super().__init__(
            title=title,
            show=show,
        )
        self._menu = menu
        self._payload: str | None = None

    def __repr__(self) -> str:
        return f"<Submenu[{self._menu=}]"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Submenu) and (  # yapf: disable
            other is self or (
                other._menu == self._menu
                and other._title == self._title
                and other._show == self._show
            )
        )

    def _init(self, m: Menu, r: OnCallbackQuery, _: Payload, /) -> None:
        if self._payload is not None:
            raise ValueError(f"{self!r} button must be unique.")
        self._payload = f"{m.get_submenu(self._menu)._prefix}##"

    async def _build(self, q: Query, /) -> InlineKeyboardButton | None:
        if not await self._is_visible(q):
            return None

        return InlineKeyboardButton(
            text=await self._get_title(q),
            callback_data=self._payload,
        )


class Back(BaseButton):
    """This button will open previous menu"""
    __slots__ = (
        "_visible",
        "_payload",
    )

    def __init__(
        self, *, title: str | Callable[[Query], Awaitable[str]]
    ) -> None:
        """
        :param title: String or Callable which returns button title.
        """
        super().__init__(title=title)
        self._visible: bool = False
        self._payload: str | None = None

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Back)
            and (other is self or (other._title == self._title))
        )

    def _init(self, m: Menu, r: OnCallbackQuery, _: Payload, /) -> None:
        if self._payload is not None:
            raise ValueError(f"{self!r} button must be unique.")

        if m._parent is not None:
            self._visible = True
            self._payload = f"{m._parent._prefix}##"

    async def _build(self, q: Query, /) -> InlineKeyboardButton | None:
        if not self._visible:
            return None

        # payload of button clicked in previous menu. useful in some cases.
        payload = getattr(q, "data", None) or ""
        return InlineKeyboardButton(
            text=await self._get_title(q),
            callback_data=f"{self._payload}{payload}",
        )
