import random
#Play a game of Rock, Paper, Scissors with the computer. 
#Prompt the user to enter a value: R, P or S
#Convert the value into Rock, Paper, or Scissors
#Ask the computer to generate a random value between 0 and 2
#Convert the computer's choice. 0 becomes Rock, 1 becomes Paper, 2 becomes Scissors
#Compare the user's choice with the computer's choice to display and message indicating whether the user on, lost or drew against the computer
#Defined a function that prompt the user to enter an action between S, P or R
#At the same time the computer generate as integer from 0 to 2
#Created conditional to convert computer number to action

#**** method 1**** User pass character on console
# max_score = 0
# current_score = 0
def rock_paper_scissors_game():
    value_user = input(
        f"Please enter which action would you like to play.\nPlease select from R, P or S (Press Q if you would like to quit): ")
    # action_user = lambda x: 'Rock' if value_user.upper() == 'R' else ('Paper' if value_user.upper() == 'P' else 'Scissors')
    action_user = lambda x: 'Rock' if value_user.upper() == 'R' else ('Paper' if value_user.upper() == 'P' else (
    'Scissors' if value_user.upper() == 'S' else print('You have quit the game'), exit()))
    # print(action_user(value_user))

    # Nested function to generate a random number and assign a value to it.
    # We save what this function return to a variable to use later
    def convert_computers_choice():
        action_computer_int = random.randint(0, 2)
        if action_computer_int == 0:
            action_computer = 'Rock'
        elif action_computer_int == 1:
            action_computer = 'Paper'
        else:
            action_computer = 'Scissors'
        return action_computer

    convert = convert_computers_choice()
    # action_computer = lambda x: 'Rock' if x == 0 else ('Paper' if x == 1 else 'Scissors')
    # convert = action_computer(random.randint(0, 2))
    print(f"The computer action is {convert} and your action was {action_user(value_user)}")

    # Added as part of the main function, to save
    main(action_user, convert, value_user)
    return action_user, convert, value_user

# Extrack method - converting code into a main() function - this block of code select who is the winner
def main(action_user, convert, value_user):
    winner2 = None
    if action_user(value_user) == 'Scissors' and convert == 'Rock' or action_user(
            value_user) == 'Paper' and convert == 'Scissors' or action_user(
        value_user) == 'Rock' and convert == 'Paper':
        print(f'Sorry! Computer wins!{chr(128575)}')
        winner2 = 'Computer'
        # score()
        play_again()
    elif action_user(value_user) == 'Scissors' and convert == 'Paper' or action_user(
            value_user) == 'Paper' and convert == 'Rock' or action_user(value_user) == 'Rock' and convert == 'Scissors':
        print(f'Congratulations! you are the winner!!{chr(128578)}')
        winner2 = 'User'
        # score()
        play_again()
    else:
        print(f"Draw!{chr(128579)}")
        # score()
        play_again()
    return winner2

# Defining a function to ask user whether they would like to play again. It would call the game function is user press Y or exit if user press N
# If user press lower case, would convert it to upper case.
# If user press another key, the program would ask again
def play_again():
    user_response = input("Would you like to play again? Press Y if Yes or N if No: ")
    if user_response.upper() == 'Y':
        rock_paper_scissors_game()
    elif user_response.upper() == 'N':
        exit()
    else:
        play_again()

# Defining function to keep current score and maximum score
# each winning give 50 points
# def score(winner):
#     param = rock_paper_scissors_game()
#     winner = main(*param)
#     global current_score, max_score
#     if winner == 'User':
#         current_score =+ 50
#         if max_score < current_score:
#             max_score = current_score
#             print(f'Congratulations!! You have got a new record of {max_score} points')
#     else:
#         print("No points this round.")
#     print(f'your current score is {current_score} points and your record is of {max_score} points')

with open('scoreboard.txt', 'w') as scoreboard:
    argum = rock_paper_scissors_game()
    winner = main(*argum)
    print(winner)
    scoreboard.write(f"The winner of this round was the:{winner}")
    # scoreboard.write(f"User Total Score: {user_score}")

# Our main() receives three arguments, so we save the arguments returned by pour main function into a variable
# Then we pass them to our main() function when calling it
# It gives an error that says that arguments is a tuple, so we have to use * to unpack it
if __name__ == "__main__":
    arguments = rock_paper_scissors_game()
    main(*arguments)