# All winning line combinations, used to determine whether game is over or not
winning_lines = ([0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontally
                 [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertically
                 [0, 4, 8], [2, 4, 6])  # Diagonally


# Print the board to the console with X:s and O:s
def print_board(board):
    board_print = [' ' if i == 0 else 'X' if i == -1 else 'O' if i == 1 else i for i in board]
    for row in range(3):
        print(f'\n{board_print[row*3:3+row*3]}' if row == 0 else board_print[row*3:3+row*3])


# Checks if the board is full (no 0:s left on the board)
def is_board_full(board):
    return 0 if 0 in board else 1


# Checks if a player has 3 in a row and therefore won the game
def evaluate(board, player):

    # Loop through all possible winning lines (horizontally, vertically and diagonally)
    for pos in winning_lines:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return 1


# Negamax function
def negamax(board, depth, player):

    # If one player has 3 in a row, return corresponding value
    # + depth is to make it chose the shortest way to victory
    if evaluate(board, player) == 1:
        return None, (10+depth)
    if evaluate(board, -player) == 1:
        return None, -(10 + depth)
    if is_board_full(board):
        return None, 0

    # Initialize best current score as worst possible score
    best_score = -20

    # Loop through all possible moves in the position
    for move in [i for i in range(len(board)) if board[i] == 0]:

        # Make the move
        board[move] = player

        # Calculate score for the new position
        score = -negamax(board, depth - 1, -player)[1]

        # Unmake the move
        board[move] = 0

        # If we find a better score than current best, then update best score
        if score > best_score:
            best_score = score
            best_move = move

    # Return the best move and score that was found f
    return best_move, best_score


def run_game():

    # Initialize board
    board = [0]*9

    # Print board before game starts
    print_board(board)

    # True = user plays first, False = AI plays first
    # Human is always 'X'
    user_turn = True

    while 1:

        # User turn to move
        if user_turn:

            # Loop until we get a valid input from user
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
                            board[user_input] = -1
                            print_board(board)
                            user_turn = not user_turn
                            break

        # Check for gameover or full board
        if evaluate(board, -1) or is_board_full(board):
            text = 'You won!' if evaluate(board, -1) else 'Game drawn!'

            # Ask if the user wants to play again.
            play_again = input(f'\n{text} Do you want to play again (y/n)? ')
            if play_again == 'y':
                run_game()
                break
            else:
                break

        # AI turn to make a move
        if not user_turn:

            # Get best move and score from the Negamax function
            # Depth 8 is to always loop until the board is full.
            depth = 8
            player = 1
            move, score = negamax(board, depth, player)

            # Make the AI move on the board, switch turns and print the new board to console
            board[move] = 1
            user_turn = not user_turn
            print_board(board)

        # Check for gameover or full board
        if evaluate(board, 1) or is_board_full(board):
            text = 'AI won!' if evaluate(board, 1) else 'Game drawn!'

            # Ask if the user wants to play again.
            play_again = input(f'\n{text} Do you want to play again (y/n)? ')
            if play_again == 'y':
                run_game()
                break
            else:
                break


# Run the game
run_game()
