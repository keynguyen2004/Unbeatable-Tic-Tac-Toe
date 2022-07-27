def Scan2Move(game, letter):
    
    square = -1

    flag = False

    # check rows
    if flag == False:
        for i in range(3):
            if (game.board[i*3:(i+1)*3].count(letter) == 2) and (game.board[i*3:(i+1)*3].count(" ") == 1):
                square = (i*3) + game.board[i*3:(i+1)*3].index(" ") + 1
                flag = True
                break
        

    # check columns
    if flag == False:
        for i in range (3):
            if (game.board[i:i+7:3].count(letter) == 2) and (game.board[i:i+7:3].count(" ") == 1):
                square = ((game.board[i:i+7:3].index(" ")) * 3) + i + 1
                flag = True
                break
        

    # check diagonals
    if flag == False:
        diagonal1 = [game.board[i] for i in (0,4,8)]
        if (diagonal1.count(letter) == 2) and (diagonal1.count(" ") == 1):
            square = (diagonal1.index(" ") * 4) + 1
            flag = True
        diagonal2 = [game.board[i] for i in (2,4,6)]
        if (diagonal2.count(letter) == 2) and (diagonal2.count(" ") == 1):
            square = ((diagonal2.index(" ") + 1) * 2) + 1
            flag = True

    return square
    