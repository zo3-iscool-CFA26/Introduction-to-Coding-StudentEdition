number = 11
while True:
    guess = int(input("Guess: "))
    if guess < number:
      print("Too low")
    elif guess > number:
      print("Too high")
    else:
      print("Correct")
      break
