import tkinter as tk
from webbrowser import open as webopen


class AtCharCountError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class EmailLengthError(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")
EMAIL_MIN_LENGTH = 4


def validate_email(address: tk.Entry, result: tk.Label) -> None:
    address_string = address.get()
    print("\nTrying to validate email address")

    try:
        validate_email_syntax(address_string)

    except (
        AtCharCountError,
        InvalidDomainError,
        EmailLengthError,
    ) as error_message:
        result.config(
            bg="indianred1",
            text=f"Error: {error_message}"
        )
        print(f'Email address "{address_string}" failed to validate:\n'
              f'{error_message}')

    else:
        result.config(
            bg="light green",
            text="Email is valid :)"
        )
        print(f'Email address "{address_string}" validated successfully')


def validate_email_syntax(address: str) -> None:
    at_char_count = address.count("@")
    domain = address.split(".")[-1]
    username = address.split("@")[0]

    if at_char_count != 1:
        raise AtCharCountError(
            f'Email contains "@" {at_char_count} times!\n'
            'It must contain "@" only once.'
        )

    if domain not in VALID_DOMAINS:
        raise InvalidDomainError(
            f"'{domain}' not in valid domains:\n{' '.join(VALID_DOMAINS)}"
        )

    if len(username) < EMAIL_MIN_LENGTH:
        raise EmailLengthError(
            f'Username "{username}" is too short!\n'
            f"{EMAIL_MIN_LENGTH} or more characters required."
        )


def clear_entry(address: tk.Entry, result: tk.Label, default_config: dict) -> None:
    address.delete(0, "end")
    result.config(**default_config)
    print(f"Entry {id(address)} cleared")


def main():
    root = tk.Tk()
    root.title("Email Address Validator")

    tk.Label(
        text="Enter your email address bellow",
        font=("Helvetica", 12),
    ).grid(row=0, column=0, padx=5, pady=5)

    tk.Button(
        text="Clear",
        command=lambda: clear_entry(
            email_address, validation_result, default_validation
        ),
        cursor="hand2"
    ).grid(row=0, column=1, ipadx=8)

    email_address = tk.Entry(width=33)
    email_address.grid(row=1, column=0)

    tk.Button(
        text="Validate",
        command=lambda: validate_email(email_address, validation_result),
        cursor="hand2"
    ).grid(row=1, column=1)

    default_validation = {
        "text": 'Press "Validate" to see the result\n',
        "font": ("Helvetica", 12),
        "bg": "lightgoldenrodyellow",
    }
    validation_result = tk.Label(**default_validation)

    validation_result.grid(
        row=2, rowspan=2,
        column=0, columnspan=2,
        pady=2, ipady=5, sticky="nsew"
    )

    tk.Button(
        text="Validate your password here next",
        command=lambda: webopen("https://neal.fun/password-game/"),
    ).grid(row=5, column=0, columnspan=2, pady=6)

    root.mainloop()


if __name__ == "__main__":
    main()
