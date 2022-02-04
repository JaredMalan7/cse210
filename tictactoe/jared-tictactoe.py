'''
Prove Developer Solo Submission: Tic-Tac-Toe
Author: Jared Malan
BYU-I CSE210
'''


# --------------------------------------------------------------------
def print_board(board):
    print(f"""
 {board[0]} | {board[1]} | {board[2]}
---+---+---
 {board[3]} | {board[4]} | {board[5]}
---+---+---
 {board[6]} | {board[7]} | {board[8]}
""")

# --------------------------------------------------------------------


def make_board():
    board = []
    for number in range(9):
        board.append(number + 1)
    return board


# --------------------------------------------------------------------
def math(board):
    return (board[0] == board[1] and board[1] == board[2] or
            board[0] == board[3] and board[3] == board[6] or
            board[0] == board[4] and board[4] == board[8] or
            board[1] == board[4] and board[4] == board[7] or
            board[2] == board[5] and board[5] == board[8] or
            board[2] == board[4] and board[4] == board[6] or
            board[3] == board[4] and board[4] == board[5] or
            board[6] == board[7] and board[7] == board[8])

# --------------------------------------------------------------------


def main():

    board = make_board()

    switch = 0

    while not math(board) and switch < 9:

        print_board(board)

        switch = switch + 1
        if switch % 2 == 0:
            player = 'O'
        else:
            player = 'X'

        move = 0
        while move > 9 or move < 1:
            move = int(input(f"Player{player} choose a square (1-9): "))
            if move > 9 or move < 1:
                print("That is not a valid number. Please try again.")

        board[move - 1] = player

    print_board(board)
    if switch < 9:
        print(f"Congrants {player} you win!")
    else:
        print("It's a tie")


# --------------------------------------------------------------------
if __name__ == "__main__":
    main()
    print('Thank You for Playing')
