import random
from algo import Algorithm

def BotSquare1379(game, letter):
    if game.numEmptySquares() == 7: 
        if "O" in [game.board[i] for i in (1,3,5,7)]:
            square = 5
        # See Square1379Explanation.txt - Explanation #1
        elif ("O" not in game.board[4]) and\
        ((abs(game.board.index("X") - game.board.index("O")) == 2) or (abs(game.board.index("X") - game.board.index("O")) == 6)):
            # See Square1379Explanation.txt - Explanation #2
            cornerSet = {0, 2, 6, 8}
            square = random.choice(list(cornerSet.intersection(game.availableMoves()))) + 1
        elif "O" in game.board[4]:
            square = random.choice(game.availableMoves()) + 1
        # Opposite corner
        elif (game.board[0] == "X" and game.board[8] == "O") or (game.board[0] == "O" and game.board[8] == "X"):
            square = random.choice([3,7])
        # Opposite corner
        elif (game.board[2] == "X" and game.board[6] == "O") or (game.board[2] == "O" and game.board[6] == "X"):
            square = random.choice([1,9])
    else:
        square = Algorithm(game, letter)

    return square

def HumanSquare1379(game, letter):
    if game.numEmptySquares() == 8:
        square = 5
    elif game.numEmptySquares() == 6:
        # See Square1379Explanation.txt - Explanation #3
        # 8 special cases
        if game.board[0] == "X" and game.board[5] == "X":
            square = random.choice([2,3,8,9])
        elif game.board[0] == "X" and game.board[7] == "X":
            square = random.choice([4,6,7,9])
        elif game.board[2] == "X" and game.board[7] == "X":
            square = random.choice([4,6,7,9])
        elif game.board[2] == "X" and game.board[3] == "X":
            square = random.choice([1,2,7,8])
        elif game.board[8] == "X" and game.board[3] == "X":
            square = random.choice([1,2,7,8])
        elif game.board[8] == "X" and game.board[1] == "X":
            square = random.choice([1,3,4,6])
        elif game.board[6] == "X" and game.board[1] == "X":
            square = random.choice([1,3,4,6])
        elif game.board[6] == "X" and game.board[5] == "X":
            square = random.choice([2,3,8,9])
        # diagonal formation - from left to right, up to down
        elif (game.board[0] == "X") and (game.board[8] == "X"):
            square = random.choice([i for i in game.availableMoves() if i not in [2,6]]) + 1
        # diagonal formation - from right to left, up to down
        elif (game.board[2] == "X") and (game.board[6] == "X"):
            square = random.choice([i for i in game.availableMoves() if i not in [0,8]]) + 1
        else:
            square = Algorithm(game, letter)
    else:
        square = Algorithm(game, letter)

    return square
