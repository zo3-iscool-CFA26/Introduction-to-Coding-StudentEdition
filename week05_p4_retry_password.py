password = "lion"
while True:
    guess = input("Password: ")
    if guess == password:
          print("Access granted")
          break
    print("Try again")
