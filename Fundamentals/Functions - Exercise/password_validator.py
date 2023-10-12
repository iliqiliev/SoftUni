def password_validator(password: str) -> str:
    
    is_alphanumeric = password.isalnum()
    is_long = 6 <= len(password) <= 10
    has_2_digits = sum(1 for char in password if char.isdigit()) > 1
    # for every digit it adds 1 and then sums them all and checks if the sum is at least 2
        
    if all([is_long, is_alphanumeric, has_2_digits]):
        return "Password is valid"
    
    errors = "Password must be between 6 and 10 characters\n" * (not is_long) + \
             "Password must consist only of letters and digits\n" * (not is_alphanumeric) + \
             "Password must have at least 2 digits\n" * (not has_2_digits)
    # by multiplying with the opposite of the boolean 
    # we only print if the condition is not met
             
    return errors.rstrip()


password = input()
print(password_validator(password))