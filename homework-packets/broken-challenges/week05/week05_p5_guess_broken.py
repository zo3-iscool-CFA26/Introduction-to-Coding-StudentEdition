target = 11
while True:
    guess = input("Guess: ")
    if guess < target:
        print("Too high")
    elif guess > target:
        print("Too low")
    else:
        print("Correct")
    break
