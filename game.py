import time
from player import FirstPlayer, ComputerPlayer, HumanPlayer

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        """
        This is similar to 
        self. board = [" ", " ", " ",
                       " ", " ", " ",
                       " ", " ", " "]
        We can use this to represent the 3x3 board
        """
        self.currentWinner = None    # Keep track of current winner
        self.firstSquare = -1

    def printBoard(self):
        # See CodeExplanation.txt - Explanation #1
        for row in(self.board[i*3:(i+1)*3] for i in range(3)):
            print("| " + " | ".join(row) + " |")

    @staticmethod
    # It is a static method because it doesn't need to access any 
    # properties of TicTacToe itself and only requires the parameter
    def printBoardNums():
        # 1 | 2 | 3 etc (tells us what number corresponds to which box)
        numberBoard = [str(i) for i in range(1,10)]
        for row in (numberBoard[j*3:(j+1)*3] for j in range(3)):
            print("| " + " | ".join(row) + " |")

    # We need to know the available moves after you make a move
    def availableMoves(self):
        return [i for (i, spot) in enumerate(self.board) if spot == " "]
        """
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['X', 'X', 'O'] → [(0,'X'), (1,'X'), (2,'O')]
            if spot  == " ":
                moves.append(i)
        return moves
        """
    
    def emptySquares(self):
        if " " in self.board:
            return True
        else:
            return False

    def numEmptySquares(self):
        return self.board.count(" ")
        # We can also use
        # return len(self.availableMoves())
    
    def makeMove(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return True. If invalid, return False
        if self.board[square - 1] == " ":
            self.board[square - 1] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        else:
            return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere ... we have to check all of these
        # first let's check the row

        # See CodeExplanation.txt - Explanation #3
        rowIndex = (square - 1)//3
        row = self.board[rowIndex*3:(rowIndex+1)*3]
        if all([ spot == letter for spot in row]):
            return True

        # check column
        # See CodeExplanation.txt - Explanation #4
        columnIndex = (square - 1)%3
        column = [self.board[columnIndex + (i*3)] for i in range (3)]
        if all([ spot == letter for spot in column]):
            return True

        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves lie on the diagonal
        if (square - 1)%2 == 0:
            diagonal1 = [self.board[i] for i in (0,4,8)] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in (2,4,6)] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all these fail
        return False

def play(game, XPlayer, OPlayer, firstPlayer, printGame = True):

    # See CodeExplanation.txt - Explanation #2
    if printGame == True:
        game.printBoardNums()
    
    letter = "X"  # Starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about winner because we'll just return that
    # which breaks the loop)

    while game.emptySquares() == True:
        # get the move from appropriate player
        if letter == "O":
            # this square will always be +1 greater than the square chosen from availableMoves()
            square = OPlayer.getMove(game, letter)
        else:
            square = XPlayer.getMove(game, letter)
            if game.numEmptySquares() == 9:
                game.firstSquare = square

        # Let's define a function to make a move
        if game.makeMove(square, letter) == True:
            if printGame == True:
                print(letter + " makes a move to square " + str(square))
                print("")
                game.printBoard()
                print("")    # Just empty line
            
            if game.currentWinner != None:
                if (game.currentWinner == "X" and firstPlayer == "Computer") or (game.currentWinner == "O" and firstPlayer == "Human"):
                    global Computer
                    Computer += 1
                else:
                    global Player
                    Player += 1
                if printGame == True:
                    print(letter + " wins!")
                return letter             

                
            # After we made our move, we need to alternate the letter
            letter = "O" if letter == "X" else "X"
            """
            if letter == "X":
                letter = "O"
            else:
                letter = "X"
            """

        # Tiny break to make things easier to read
        time.sleep(0.25)

    if game.currentWinner == None:
        print("It's a tie!")
        global Tie
        Tie += 1
    


if __name__ == "__main__":
    
    
    Player = 0
    Tie = 0
    Computer = 0
    
    flag = False
    while flag == False:
        firstPlayer = FirstPlayer()
        if firstPlayer.GetFirstPlayer().lower() == "human":
            XPlayer = HumanPlayer("X")
            OPlayer = ComputerPlayer("O")
            firstPlayer = "Human"
            
        else:
            XPlayer = ComputerPlayer("X")
            OPlayer = HumanPlayer("O")
            firstPlayer = "Computer"
        t = TicTacToe()
        play(t, XPlayer, OPlayer, firstPlayer, printGame = True)

        print("")
        print("Player's wins: " + str(Player))
        print("Ties: " + str(Tie))
        print("Computer's wins: " + str(Computer))
        print("")

        continueGame = HumanPlayer.continueGame()
        print("")
        if continueGame.lower() == "no":
            flag = True

    print("Thank you for playing ^^")