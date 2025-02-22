import random  # Import the random module (which picks random elements) to let the computer pick a choice

# Create a function  to prompt the user to enter a value R, P or S
def get_user_choice():
    """Ask the user to enter R, P, or S and return the full choice.
    param:
    return: str
    """
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}  # add a dictionary to match letters to the values

    while True: # set a loop until the user enters a suggested value, R, P or S
        user_input = input("Enter R for Rock, P for Paper, or S for Scissors: ")  # the input function allows the user to enter a value

        if user_input in choices:  # Set a conditional statement to check if user input is valid
            return choices[user_input]  # Return the full name that the user chose
        print("Invalid input. Please enter R, P, or S.")  # Show error message if input is wrong

# Create unction to get the computer's choice
def get_computer_choice():
    """Pick Rock, Paper, or Scissors randomly for the computer."""
    choices = ['Rock', 'Paper', 'Scissors']  # List of choices
    return random.choice(choices)  # random module generates random variables, in this case, random choices for the computer

# create a function to decide who wins
def determine_the_winner(user_choice, computer_choice):
    """Compare user and computer choices to find the winner."""
    print(f"You chose: {user_choice}")  # Show user’s choice
    print(f"Computer chose: {computer_choice}")  # Show computer’s choice

    if user_choice == computer_choice:  # If choices are the same, it's a tie
        return "It's a draw!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"  # User wins
    else:
        return "Computer wins!"  # Computer wins

# Function to play the game
def play_game():
    """Start the game and show the result."""
    print("Welcome to Rock, Paper, Scissors!")  # Greet the user
    user_choice = get_user_choice()  # Get user choice
    computer_choice = get_computer_choice()  # Get computer choice
    result = determine_the_winner(user_choice, computer_choice)  # Find the winner
    print(result)  # Print the result

# Run the game if this script is executed directly
if __name__ == "__main__": # this special character helps to run the game
    play_game()  # Start the game

