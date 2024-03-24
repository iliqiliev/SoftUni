from typing import Any, Callable


class store_results:
    def __init__(self, func: Callable[..., Any]) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> str:
        result = self.func(*args, **kwargs)

        log_text = (
            f"Function '{self.func.__name__}' was called. "
            f"Result: {result}"
        )

        with open("log.txt", "a", encoding="utf-8") as log:
            log.write(log_text + "\n")

        return result
