import random
import time
from os import system, name


def main():
    user_input = input("Enter an option (rock, paper, scissors): ").lower()
    valid_inputs = ["rock", "paper", "scissors"]

    def compare_input():
        if user_input in valid_inputs:
            game_start()
        else:
            print("\nINVALID INPUT!\n")
            main()

    # define our clear function
    def clear():

        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def game_start():
        comp_choice = random.choice(valid_inputs)

        # Rock smashes scissors.
        # Paper covers rock.
        # Scissors cut paper.
        if user_input == comp_choice:
            print(f"Comp: {comp_choice}, You: {user_input}, Its a tie!\n")
            main()
        else:
            result = comp_choice
            if result == "rock" and user_input == "scissors":
                print("Rock smashes scissors, YOU LOOSE!\n")
                main()
            elif result == "paper" and user_input == "rock":
                print("paper covers rock, YOU LOOSE!\n")
                main()
            elif result == "Scissors" and user_input == "paper":
                print("Scissors cuts paper, YOU LOOSE\n")
                main()
            else:
                print(f"Computer choice: {result}, Your choice: {user_input}. YOU WIN!\n")
                print("Would you like to try again? (y/n)")
                retry = input(">> ").lower()
                if retry == "y":
                    clear()
                    main()
                elif retry == "n":
                    print("\nBYE!")
                    exit()
                else:
                    print("Please enter a y or n.")
                    print("\nWould you like to try again? (y/n)")
                    retry = input(">> ").lower()
                    if retry == "y":
                        main()
                    elif retry == "n":
                        print("\nBYE!")
                        exit()
                    else:
                        print("\nYou have entered an invalid choice twice")
                        print("\n\t\tGAME RESTARTING ...")
                        time.sleep(5.0)
                        clear()
                        main()

    compare_input()


main()
