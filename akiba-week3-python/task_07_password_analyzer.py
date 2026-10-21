def check_length(password, min_length=8):
    return len(password) >= min_length


def check_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False


def check_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False


def check_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def check_special(password):
    for char in password:
        if not char.isalnum():
            return True
    return False


def analyze_password(password, min_length=8):
    result = {
        "Minimum length": check_length(password, min_length),
        "Uppercase letter": check_uppercase(password),
        "Lowercase letter": check_lowercase(password),
        "Digit": check_digit(password),
        "Special character": check_special(password)
    }

    return result


passwords = [
    "hello",
    "HELLOWORLD",
    "Hello123",
    "Hello@123",
    "abc@123"
]

for password in passwords:
    print("\nPassword:", password)

    report = analyze_password(password)

    for requirement, passed in report.items():
        if passed:
            print(requirement, ": PASS")
        else:
            print(requirement, ": FAIL")

    if all(report.values()):
        print("Password meets all requirements.")
    else:
        print("Password does not meet all requirements.")
