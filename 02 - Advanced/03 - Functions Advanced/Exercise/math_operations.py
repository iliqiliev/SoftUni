import operator

operations = (
    operator.add,
    operator.sub,
    operator.truediv,
    operator.mul
)


def math_operations(*numbers: float, **kwargs) -> str:
    kwargs_len = len(kwargs)
    keys = list(kwargs.keys())

    for index, number in enumerate(numbers):
        current = index % kwargs_len
        key = keys[current]

        if key == "d" and not number:
            continue

        kwargs[key] = operations[current](kwargs[key], number)

    return "\n".join(f"{key}: {value:.1f}" for key, value in sorted(
        kwargs.items(),
        key=lambda kvp: (-kvp[1], kvp[0])
    ))
