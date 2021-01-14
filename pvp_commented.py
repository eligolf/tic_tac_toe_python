# All winning line combinations, used to determine whether game is over or not
winning_lines = ([0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontally
                 [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertically
                 [0, 4, 8], [2, 4, 6])  # Diagonally


# Print the board to the console with X:s and O:s
def print_board(board):
    board_print = ['-' if i == 0 else 'O' if i == -1 else 'X' if i == 1 else i for i in board]
    for row in range(3):
        print(f'\n{board_print[row*3:3+row*3]}' if row == 0 else board_print[row*3:3+row*3])


# Checks if the board is full (no 0:s left on the board)
def is_board_full(board):
    return 0 if 0 in board else 1


# Checks if a player has 3 in a row and therefore won the game
def is_game_won(board):
    for line in winning_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != 0:
            return 1
    return 0


# Game loop which handles input from the user
def run_game():

    # Define an empty board
    board = [0]*9

    # Print the board at the start
    print_board(board)

    # Initialize who starts the game (X in this case)
    turn_to_move = 1

    # Loop until the game is over
    while 1:

        # Get user input from the console
        user_input = input('\nPlease enter your move (1-9): ')

        # Check if user input is a number
        if user_input.isnumeric():

            # If it is a number, make the string an integer and subtract 1 since array indices starts at 0
            user_input = int(user_input) - 1

            # Check if the input - 1 is in range 0-8
            if user_input in range(9):

                # Check if the input is an empty square
                if board[user_input] == 0:

                    # If all conditions are true: Make the move on the board, print the new board and change turn
                    board[user_input] = turn_to_move
                    print_board(board)
                    turn_to_move = turn_to_move * -1

        # Check if game is over due to 3 in a row or a full board
        winner = is_game_won(board)
        board_full = is_board_full(board)
        if winner or board_full:
            player = 'X' if turn_to_move == -1 else 'O'
            text = f'\n{player} won!' if winner else 'Game drawn!'

            # Ask if the user wants to play again.
            play_again = input(f'{text} Do you want to play again (y/n)? ')
            if play_again == 'y':
                run_game()
                break
            else:
                break


# Run the game
run_game()








