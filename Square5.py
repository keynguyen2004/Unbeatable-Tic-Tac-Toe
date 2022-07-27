import random
from algo import Algorithm

def BotSquare5 (game, letter):
    if game.numEmptySquares() == 7: 
        if "O" in [game.board[i] for i in (1,3,5,7)]:
            if "O" in game.board[1]:
                square = random.choice([7, 9])
            elif "O" in game.board[3]:
                square = random.choice([3, 9])
            elif "O" in game.board[5]:
                square = random.choice([1, 7])
            else:
                square = random.choice([1, 3])
        else:
            # Make random move 
            # Even if we move at the corner opposite of the square,
            # we can create a trap (see the case of a diagonal with two X and one O)
            square = random.choice(game.availableMoves()) + 1
    else:
        square = Algorithm(game, letter)

    return square



def HumanSquare5 (game, letter):
    if game.numEmptySquares() == 8:
        square = random.choice([1, 3, 7, 9])
    elif game.numEmptySquares() == 6:
        # in case of diagonal two X and one O, you must block 
        # either of the remaining two corners
        if (game.board[0] == "O" and game.board[8] == "X") or (game.board[0] == "X" and game.board[8] == "O"):
            square = random.choice([3,7])
        elif (game.board[2] == "O" and game.board[6] == "X") or (game.board[2] == "X" and game.board[6] == "O"):
            square = random.choice([1,9])
        else:
            square = Algorithm(game, letter)
    else:
        square = Algorithm(game, letter)

    return square