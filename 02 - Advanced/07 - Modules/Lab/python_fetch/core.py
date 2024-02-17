import os


# TODO: finish

def generate_system_info() -> dict[str, str]:
    if os.name == "posix":
        return generate_linux_info()

    return {}


def generate_linux_info() -> dict[str, str]:
    return {
        "System": "Arch"
    }
