import random

def Scan2movesIntersection(game, letter):

    square = -1

    # check rows
    rowCount = 0
    for i in range(3):
        if (game.board[i*3:(i+1)*3].count(letter) == 1) and (game.board[i*3:(i+1)*3].count(" ") == 2):
            row = game.board[i*3:(i+1)*3]
            blankSquareIndex = [j for j in range(3) if row[j] == " "]
            blankRowIndex = [(i*3) + 1 + j for j in blankSquareIndex]
            rowCount += 1
            break
    

    # check columns
    columnCount = 0
    for i in range (3):
        if (game.board[i:i+7:3].count(letter) == 1) and (game.board[i:i+7:3].count(" ") == 2):
            column = game.board[i:i+7:3]
            blankSquareIndex = [j for j in range(3) if column[j] == " "]
            blankColumnIndex = [i + 1 + (j*3) for j in blankSquareIndex]
            columnCount += 1
            break
    

    # check diagonals
    diagonal1Count = 0
    diagonal1 = [game.board[i] for i in (0,4,8)]
    if (diagonal1.count(letter) == 1) and (diagonal1.count(" ") == 2):
        blankSquareIndex = [j for j in range (3) if diagonal1[j] == " "]
        blankDiagonal1Index = [1 + (j*4) for j in blankSquareIndex]
        diagonal1Count += 1

    diagonal2Count = 0    
    diagonal2 = [game.board[i] for i in (2,4,6)]
    if (diagonal2.count(letter) == 1) and (diagonal2.count(" ") == 2):
        blankSquareIndex = [j for j in range (3) if diagonal2[j] == " "]
        blankDiagonal2Index = [(((j + 1) * 2) + 1) for j in blankSquareIndex]
        diagonal2Count += 1

    # Test if there's any intersection
    if rowCount == 1 and columnCount == 1:
        IntersectionSet = (set(blankRowIndex).intersection(set(blankColumnIndex)))
        for i in IntersectionSet:
            square = i

    elif rowCount == 1 and diagonal1Count == 1:
        IntersectionSet = (set(blankRowIndex).intersection(set(blankDiagonal1Index)))
        for i in IntersectionSet:
            square = i

    elif rowCount == 1 and diagonal2Count == 1:
        IntersectionSet = (set(blankRowIndex).intersection(set(blankDiagonal2Index)))
        for i in IntersectionSet:
            square = i

    elif columnCount == 1 and diagonal1Count == 1:
        IntersectionSet = (set(blankColumnIndex).intersection(set(blankDiagonal1Index)))
        for i in IntersectionSet:
            square = i

    elif columnCount == 1 and diagonal2Count == 1:
        IntersectionSet = (set(blankColumnIndex).intersection(set(blankDiagonal2Index)))
        for i in IntersectionSet:
            square = i

    elif diagonal1Count == 1 and diagonal2Count == 1:
        square = 5

    
    
    return square