# this program is a basic 4 function calculator with integers
import math

def start_cal():

    x, y, answer = 0, 0, 0
    print("Welcome to Emi's basic 4 function calculator.")
    yes_no = input("Do you want to do some math? Enter Y or N: ")
    while yes_no.lower() == "y":
        try:
            choice = input("Choose between +, -, *, or / (you can also choose q to quit): ")
            if choice == "+":
                print("Enter 2 numbers to add.")
                print("--------------------")
                x = input("Value 1: ")
                y = input("Value 2: ")
                answer = int(x) + int(y)
                print(str(x) + " + " + str(y) + " = " + str(answer))
            elif choice == "-":
                print("Enter 2 numbers to subtract.")
                print("--------------------")
                x = input("Value 1: ")
                y = input("Value 2: ")
                answer = int(x) - int(y)
                print(str(x) + " - " + str(y) + " = " + str(answer))
            elif choice == "*":
                print("Enter 2 numbers to multiply.")
                print("--------------------")
                x = input("Value 1: ")
                y = input("Value 2: ")
                answer = int(x) * int(y)
                print(str(x) + " * " + str(y) + " = " + str(answer))
            elif choice == "/":
                print("Enter 2 numbers to divide.")
                print("--------------------")
                x = input("Value 1: ")
                y = input("Value 2: ")
                answer = int(x) / int(y)
                print(str(x) + " / " + str(y) + " = " + str(answer))
            elif choice == "q":
                print("The calculator will exit now. Have a good day.")
                break
            else:
                print("This is not a valid input. Try again.")
        except:
            if str(choice) == "q":
                break
            # tried using a try/except for this program with little success, using the try block to handle everything
            # NEED TO FIND OUT WHY THIS EXCEPT BLOCK IS NEEDED FOR THE Q CONDITIONAL IN THE TRY BLOCK TO WORK PROPERLY

    else:

        print("Have a good day.")

if __name__ == "__main__":
    start_cal()
