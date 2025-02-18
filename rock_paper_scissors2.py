# Importing the random module to enable random selection for the computer's choice
import random


# Defining a function to randomly select between Rock, Paper, or Scissors for the computer
def get_computer_choice():
    """
    Randomly selects from Rock, Paper or Scissors for the computer
    :return: str
    """
    return  random.choice (['Rock', 'Paper', 'Scissors']) # Using 'choice' method from the 'random' module to randomly select one option from the list


# Defining a function to find user choice.
def get_user_choice():
    # Dictionary to link user input (R, P, S) to full word choices (Rock, Paper, Scissors)
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    # This 'while' loop is ensuring that the user input is valid.
    while True:
        user_input = input("Lets play Rock, Paper, Scissors!\nTo start enter R, P or S:").upper()  # Using the .upper() method to Convert user input to uppercase to handle both lowercase and uppercase inputs
        if user_input in choices:  # Checks if user input is valid
            user_input = choices[user_input]  # Converting user choice to the full word.
            break  # Exit the loop when valid input is received
        else:
            print("You have entered an invalid option.")
           # user_input = input("You have entered an invalid option. Let's try again!\nPlease input  R, P or S:")  # If input is invalid, prompts user to enter a valid input. The loop will continue until a correct input is given.
    return user_input

#Function to determin the winner
def determin_winner(user_choice, computer_choice):
    # Determining the winner based on rules of rock, paper, scissors
    # Displaying what the user and computer have chosen using 'f' string. Using the variable to call our function.
    print(f"You have chosen: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a Draw!")  # Both choices are the same it's a draw
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
            (user_choice == "Scissors" and computer_choice == "Paper") or \
            (user_choice == "Paper" and computer_choice == "Rock"):
        print("You won! Congratulations! ")  # Winning conditions
    else:
        print("You lost!! Let's play again ")  # Losing conditions.

#Using a variable to call the functions we created.
computer_choice = get_computer_choice()
user_choice = get_user_choice()
determin_winner(user_choice, computer_choice)

#We could create a function for returning a string with winner rather than using thr print commands