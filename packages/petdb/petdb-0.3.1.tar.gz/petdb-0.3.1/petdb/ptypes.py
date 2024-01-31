from typing import Any, Callable

type i_remove = str | dict | list[str | dict]
type i_sort = str | int | list[str | int] | tuple[str | int, ...] | Callable[[Any], Any] | None
