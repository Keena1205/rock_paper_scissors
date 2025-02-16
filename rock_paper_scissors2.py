#importing the Random Module
import random

#Defining a function in-order for the computer to select randomly between rock, paper and scissors
def get_computer_choice():
    """
    Randomly selects from Rock, Paper or Scissors for the computer
    :return: str
    """
    return  random.choice (['Rock', 'Paper', 'Scissors']) #using.choice method to select one element.

#Using a variable to call the function we created.
computer_choice = get_computer_choice()

#Defining a dictionary to convert input to full names.
choices = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}

#while loop is ensuring that the user input is valid.
while True:
    user_input = input("Lets play Rock, Paper, Scissors!\nTo start enter R, P or S:").upper() #using upper method to avoid case sensitivity issues
    if user_input in choices: #Checks if input is valid
        user_choice = choices[user_input] #Converting user choice to the full word.
        break #Exit the loop when valid input is received
    else:
        input("You have entered an invalid option. Let's try again!\nPlease input  R, P or S:") #If input is invalid, prompts user to enter a valid inpout. The loop will continue until a correct input is given.

#Displaying what the user and computer have chosen
print(f"You have chosen: {user_choice}")
print(f"The computer chose: {computer_choice}")

#Determining the winner based on rules
if user_choice == computer_choice:
    print("It's a Draw!") # Both choices are the same it's a draw
elif (user_choice == "Rock" and computer_choice == "Scissors") or \
    (user_choice == "Scissors" and computer_choice == "Paper") or \
    (user_choice == "Paper" and computer_choice == "Rock"):
    print("You won! Congratulations! ") # Winning conditions
else:
    print("You lost!! Let's play again ") #Losing conditions.