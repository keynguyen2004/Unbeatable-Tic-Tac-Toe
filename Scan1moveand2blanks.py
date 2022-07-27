import random

def Scan1move(game, letter):

    square = -1
    flag = False

    # check rows
    if flag == False:
        for i in range(3):
            if (game.board[i*3:(i+1)*3].count(letter) == 1) and (game.board[i*3:(i+1)*3].count(" ") == 2):
                row = game.board[i*3:(i+1)*3]
                blankSquareIndex = [j for j in range(3) if row[j] == " "]
                square = (i*3) + random.choice(blankSquareIndex) + 1
                flag = True
                break
        
    # check columns
    if flag == False:
        for i in range (3):
            if (game.board[i:i+7:3].count(letter) == 1) and (game.board[i:i+7:3].count(" ") == 2):
                column = game.board[i:i+7:3]
                blankSquareIndex = [j for j in range(3) if column[j] == " "]
                square = ((random.choice(blankSquareIndex))* 3) + i + 1
                flag = True
                break
        

    # check diagonals
    if flag == False:
        diagonal1 = [game.board[i] for i in (0,4,8)]
        if (diagonal1.count(letter) == 1) and (diagonal1.count(" ") == 2):
            blankSquareIndex = [j for j in range (3) if diagonal1[j] == " "]
            square = ((random.choice(blankSquareIndex)) * 4) + 1
            flag = True
    
    if flag == False:
        diagonal2 = [game.board[i] for i in (2,4,6)]
        if (diagonal2.count(letter) == 1) and (diagonal2.count(" ") == 2):
            blankSquareIndex = [j for j in range (3) if diagonal2[j] == " "]
            square = (((random.choice(blankSquareIndex)) + 1) * 2) + 1
            flag = True

    return square