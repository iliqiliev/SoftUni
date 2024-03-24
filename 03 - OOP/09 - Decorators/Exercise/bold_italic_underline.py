from functools import wraps
from typing import Callable


def tag_text(func: Callable[..., str], tag: str) -> Callable[..., str]:

    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        return f"{tag}{func(*args, **kwargs)}{tag[:1] + '/' + tag[1:]}"

    return wrapper


def make_bold(func: Callable[..., str]) -> Callable[..., str]:
    return tag_text(func, tag="<b>")


def make_italic(func: Callable[..., str]) -> Callable[..., str]:
    return tag_text(func, tag="<i>")


def make_underline(func: Callable[..., str]) -> Callable[..., str]:
    return tag_text(func, tag="<u>")
