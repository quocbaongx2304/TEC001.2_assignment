correct_username = "quoc.baooo"
correct_password = "lgbt"

attempts = 0

while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Wrong username or password")
        attempts += 1

if attempts == 3:
    print("Access denied")