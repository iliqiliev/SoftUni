def password_validator(password: str) -> str:
    
    has_only_chars_and_digits = True
    digit_counter = 0
    
    for char in password:
        if char.isdigit():
            digit_counter += 1
        elif char.isalpha():
            pass
        else:
            has_only_chars_and_digits = False
            
    is_long = 6 <= len(password) <= 10   
    has_2_digits = digit_counter > 1
    
    if all([is_long, has_only_chars_and_digits, has_2_digits]):
        return "Password is valid"
    
    errors = "Password must be between 6 and 10 characters\n" * (not is_long) + \
             "Password must consist only of letters and digits\n" * (not has_only_chars_and_digits) + \
             "Password must have at least 2 digits\n" * (not has_2_digits)
             
    return errors.rstrip()

password = input()
print(password_validator(password))