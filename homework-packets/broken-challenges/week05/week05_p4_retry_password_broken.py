secret = "lion"
guess = input("Password: ")
While True:
    if guess == secret:
        print("Access granted")
        break
    print("Try again")
