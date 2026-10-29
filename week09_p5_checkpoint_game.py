def show_intro():
   print("Greetings travler! it seems you have stumbled upon a cave... to get through you must do a quest!")

def play_once():
    choice = input("Will you do the quest? Yes or No: ").strip().lower()
    if choice == "yes":
        print("Amazing! All you have to do is find my magic tresure.")
    else:
        print("aww... thats just too bad. you have to play :(")
        print("All you have to do is find my magic tresure.")
    print("As you enter the cave you see a right turn and left turn, which way do you turn?")
    hoice = input("Left or Right: ").strip().lower()
    if hoice == "left":
        print("You have found a tourch!")
        print("The tourch helps you see hidden messages on the walls... they guide you to the magic treasure.")
        inventory = []
        inventory.append("Tourch")
        print("Inventory: ", inventory)
    else:
        print("You have found a map!")
        print("The map helps guide you to the magic treasure.")
        inventory = []
        inventory.append("Map")
        print("Inventory: ", inventory)
    print("Your on the last turn but your guides have stopped ebruptly, you decide to disregard them. Where do you go?")
    oice = input("Left or Right: ").strip().lower()
    if oice == "right":
        print("You have found the magic treasure!!")
        print("You find your way out and complete your quest.")
        inventory = []
        inventory.append("Magic treasure")
        print("Final inventory: ", inventory)
    else:
        print("You have fell for a secret booby trap and died...")
def main():
        show_intro()
        while True:
            play_once()
            again = input("Play again? ").strip().lower()
            if again == "no":
                print("Thanks for playing!")
                break
main()
