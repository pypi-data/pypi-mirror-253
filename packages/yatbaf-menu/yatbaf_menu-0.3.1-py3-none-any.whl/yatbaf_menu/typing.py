from __future__ import annotations

from typing import TYPE_CHECKING
from typing import TypeAlias

if TYPE_CHECKING:
    from yatbaf.types import CallbackQuery
    from yatbaf.types import Message

Query: TypeAlias = "Message | CallbackQuery"
