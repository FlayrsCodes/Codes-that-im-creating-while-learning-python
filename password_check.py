import string

def check_password(password):
    if len(password) < 8:
        return "password too short, it need to be more than 8 symbols"
    if not any(char.isdigit() for char in password):
        return "password must contain at least one word"
    if not any(char.isdigit() for char in password):
        return "password must contatin at least one number"
    return "password is safe"
password = input("input password")
print (check_password(password))
