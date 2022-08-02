password = input("Enter password: ")
minimum_password_length = 5

while len(password) < minimum_password_length:
    print("Password too short. Re-enter password.")
    password = input("Enter password: ")

for i in range(0, len(password)):
    print("*", end='')