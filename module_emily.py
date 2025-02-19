# import random module
import random

# convert function for user input
def convert_user(user_input):
    """
    This function converts the user input into Rock, Paper or Scissors\n
    If the input is not formatted correctly they will be prompted to try again
    :param user_input: str
    :return: str
    """
    if user_input == 'R':
        rock_output = 'Rock'
        return str(rock_output)
    elif user_input == 'P':
        paper_output = 'Paper'
        return str(paper_output)
    elif user_input == 'S':
        scissors_output = 'Scissors'
        return str(scissors_output)
    else:
        print('Please try again. Make sure letter is capitalised and has no spaces.')


# computer generated move function
# randint method
def computer():
    """
    This function generates the computers random move in Rock, Paper, Scissors\n
    :return: str
    """
    computer_move = ['Rock', 'Paper', 'Scissors']
    random_number = random.randint(0, 2)
    return str(computer_move[random_number])
    # return used so value can be assigned to a variable

# code to play the game
def play_rps(human_rps, computer_rps, score):
    """
    This function compares the human and computer moves in Rock, Paper, Scissors,
    and prints if the human won, lost or drew with the computer. It also amends the user's score.
    :param human_rps: str
    :param computer_rps: str
    :param computer_rps: int
    :return: int
    """
    if human_rps == computer_rps:
        print("It's a draw")
        score += 0
        print(f"Your score: {score}")
        return int(score)
    elif human_rps == 'Rock' and computer_rps == 'Paper':
            print('Computer wins')
            score += 0
            print(f"Your score: {score}")
            return int(score)
    elif human_rps == 'Paper' and computer_rps == 'Scissors':
            print('Computer wins')
            score += 0
            print(f"Your score: {score}")
            return int(score)
    elif human_rps == 'Scissors' and computer_rps == 'Rock':
            print('Computer wins')
            score += 0
            print(f"Your score: {score}")
            return int(score)
    else:
        print('You win!')
        score += 1
        print(f"Your score: {score}")
        return score


# test code in main trick block
def main():
    user_test = convert_user('S')
    print(user_test)
    computer_test = computer()
    print(computer_test)

if __name__ == '__main__':
    main()