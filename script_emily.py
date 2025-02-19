from module_emily import convert_user, computer, play_rps

# having game as a function
human_input=None
score = 0

while human_input != 'QUIT':
    human_input = input("Input R, P or S, or type QUIT to exit game:")
    if human_input == "QUIT":
        break
    elif human_input != 'R' and human_input != 'P' and human_input != 'S':
        print('Please try again. Make sure letter is capitalised and has no spaces.')
    else:
        # Rock, Paper or Scissors assigned to human_rps
        human_rps = (convert_user(human_input))
        print(f" You: {human_rps}")
        # Rock, Paper or Scissor assigned to computer_rps
        computer_rps = computer()
        print(f" Computer: {computer_rps}")
        score = play_rps(human_rps, computer_rps, score)
        # assign score to a variable within the loop so the value is fed back into the loop
        # function play_rps returns the value of score