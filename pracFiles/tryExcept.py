import random

def start_game():
    z = 0 # the number of attempts for guessing
    x = int(random.randint(1, 10)) # x is our random integer
    choice = input("Do you want to play the game? Enter Y or N: ")
    while choice.lower() == "y":
        try:
            y = input("Choose a number between 1 and 10, or enter q to quit: ") # y is our user input for guessing a number
            if int(y) < 1 or int(y) > 10:
                raise ValueError("The number you chose is too big or too small.")
            if x == int(y):
                z += 1
                print("You got the number! It took you " + str(z) + " attempt(s).")
                replay = input("Would you like to play again? Enter Y or N: ")
                z = 0
                x = int(random.randint(1, 10))
                if replay.lower() == "n":
                    print("Have a good day.")
                    break
            elif int(y) < x:
                print("The number is too low.")
                z += 1
            elif int(y) > x:
                print("The number is too high.")
                z += 1
        except ValueError as valErr:
            if str(y) == "q":
                print("Exiting the program now, have a nice day.")
                break
            else:
                print("That is not a valid input.")
    else:
        print("Have a good day!")

if __name__ == "__main__":
    start_game()
