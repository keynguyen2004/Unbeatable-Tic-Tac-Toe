import random
from algo import Algorithm
from Scan2movesandablank import Scan2Move

def BotSquare2468(game, letter):
    if game.numEmptySquares() == 7: 
        if game.board[4] == " ":
            square = 5
        else:
            if game.board[1] == "X":
                square = random.choice([i for i in game.availableMoves() if i != 7]) + 1
            elif game.board[3] == "X":
                square = random.choice([i for i in game.availableMoves() if i != 5]) + 1
            elif game.board[5] == "X":
                square = random.choice([i for i in game.availableMoves() if i != 3]) + 1
            elif game.board[7] == "X":
                square = random.choice([i for i in game.availableMoves() if i != 1]) + 1
    else:
        square = Algorithm(game, letter)

    return square

def HumanSquare2468(game, letter):
    if game.numEmptySquares() == 8:
        square = 5
    elif game.numEmptySquares() == 6:
        # 8 special cases - exact same to the problem encounter in test case square corner square
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
        # Winning cases              
        elif (game.board[1] == "X") and (game.board[7] == "X"):
            square = random.choice(game.availableMoves()) + 1
        elif (game.board[3] == "X") and (game.board[5] == "X"):
            square = random.choice(game.availableMoves()) + 1               
        else:
            square = -1
            if square == -1:
                square = Scan2Move(game, "X")
            if square == - 1:
                # 4 special cases - due to algorithm limitation
                # See Square2468Explanation.txt - Explanation #1
                if (game.board[1] == "X") and (game.board[3] == "X"):
                    square = random.choice([1,3,7])
                elif (game.board[1] == "X") and (game.board[5] == "X"):
                    square = random.choice([1,3,9])
                elif (game.board[3] == "X") and (game.board[7] == "X"):
                    square = random.choice([1,7,9])
                elif (game.board[5] == "X") and (game.board[7] == "X"):
                    square = random.choice([3,7,9])
            # Pretty sure all cases are covered, 
            # but leave this here just to catch any unexpected exceptions
            if square == -1:
                square = Algorithm(game, letter) 
    else:
        square = Algorithm(game, letter)

    return square
