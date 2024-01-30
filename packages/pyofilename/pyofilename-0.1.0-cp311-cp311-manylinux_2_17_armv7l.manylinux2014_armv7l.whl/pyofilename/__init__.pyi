from typing import Literal, Optional


def is_name_reserved(name: str, strict: Optional[bool] = True) -> bool:
    ...


def is_safe_name(
    name: str,
    only_check_creatable: Optional[bool] = False,
    strict: Optional[bool] = True
) -> bool:
    ...


def to_safe_name(
    name: str,
    replace_method: Literal["fullwidth", "replace", "remove"],
    replace_char: Optional[str] = "_",
    dot_handling_policy: Optional[Literal["remove", "replace", "not_correct"]] = "replace",
    strict: Optional[bool] = True,
) -> str:
    ...
