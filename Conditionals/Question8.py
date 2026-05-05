

password = input("Enter password: ")

if len(password) < 6:
    print("Password is WEAK")
elif len(password) >= 6 and len(password) < 10:
    print("Password is MEDIUM")
elif len(password) >= 10:
    print("Password is STRONG")