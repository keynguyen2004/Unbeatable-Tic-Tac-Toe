import random
from Scan2movesandablank import Scan2Move
from Scan2movesIntersection import Scan2movesIntersection
from Scan1moveand2blanks import Scan1move

def Algorithm(game, letter):
    if letter == "X":
        BotLetter = "X"
        HumanLetter = "O"
    else:
        BotLetter = "O"
        HumanLetter = "X"
    
    square = -1

    if square == -1:    
        # BotLetter: Scan 2 moves and a blank
        square = Scan2Move(game, BotLetter)

    if square == -1:
        # HumanLetter: Scan 2 moves and a blank
        square = Scan2Move(game, HumanLetter)

    if square == -1:
        # BotLetter: Find two 2-moves intersections
        square = Scan2movesIntersection(game, BotLetter)
    
    if square == -1:
        # HumanLetter: Find two 2-moves intersections
        square = Scan2movesIntersection(game, HumanLetter)

    if square == -1:
        # BotLetter: Scan 1 move and 2 blanks
        square = Scan1move(game, BotLetter)

    if square == -1:
        # BotLetter: Else, choose random from available moves
        square = random.choice(game.availableMoves()) + 1
    
    return square