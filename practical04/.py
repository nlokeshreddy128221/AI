
import math

board = [" "] * 9

def display():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-----")

def winner():
    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in lines:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None

# Minimax with Alpha-Beta pruning
def minimax(is_max, alpha, beta):
    result = winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False, alpha, beta)
                board[i] = " "

                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True, alpha, beta)
                board[i] = " "

                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break

        return best

def best_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False, -math.inf, math.inf)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

# Play against the computer
while not winner():
    display()

    try:
        pos = int(input("Enter your position (1-9): ")) - 1
    except ValueError:
        print("Enter a number from 1 to 9.")
        continue

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid position. Try again.")
        continue

    board[pos] = "X"

    if winner():
        break

    move = best_move()
    board[move] = "O"
    print("Computer chooses position:", move + 1)

display()

result = winner()
if result == "Draw":
    print("Game Draw!")
elif result == "X":
    print("You Win!")
else:
    print("Computer Wins!")
