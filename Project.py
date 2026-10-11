from random import randrange


def display_board(board):
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(
            board[row][0], board[row][1], board[row][2]
        ))
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))

            if move < 1 or move > 9:
                print("Invalid move. Choose a number from 1 to 9.")
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] in ['X', 'O']:
                print("Square already occupied.")
                continue

            board[row][col] = 'O'
            break

        except ValueError:
            print("Please enter a valid integer.")


def make_list_of_free_fields(board):
    free = []

    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free.append((row, col))

    return free


def victory_for(board, sign):

    # Rows
    for row in board:
        if row.count(sign) == 3:
            return sign

    # Columns
    for col in range(3):
        if board[0][col] == sign and \
           board[1][col] == sign and \
           board[2][col] == sign:
            return sign

    # Diagonals
    if board[0][0] == sign and \
       board[1][1] == sign and \
       board[2][2] == sign:
        return sign

    if board[0][2] == sign and \
       board[1][1] == sign and \
       board[2][0] == sign:
        return sign

    return None


def draw_move(board):
    free = make_list_of_free_fields(board)

    if len(free):
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'


board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]

while True:

    display_board(board)

    if victory_for(board, 'X'):
        print("Computer won!")
        break

    if victory_for(board, 'O'):
        print("You won!")
        break

    if not make_list_of_free_fields(board):
        print("Tie!")
        break

    enter_move(board)

    if victory_for(board, 'O'):
        display_board(board)
        print("You won!")
        break

    if not make_list_of_free_fields(board):
        display_board(board)
        print("Tie!")
        break

    draw_move(board)