import math
import random
import re
from Square5 import BotSquare5, HumanSquare5
from Square2468 import BotSquare2468, HumanSquare2468
from Square1379 import BotSquare1379, HumanSquare1379

class FirstPlayer:
    def GetFirstPlayer(self):
        flag = False
        # Choose the first player
        while flag == False:
            firstPlayer = input("Choose the first player (Human/Bot): ")
            try:
                if not (firstPlayer.lower() == "human" or firstPlayer.lower() == "bot"):
                    raise TypeError
                else:
                    flag = True
            except TypeError:
                print("Wrong data type. Please input either 'Human' or 'Bot' as the first player: ")    
        
        return firstPlayer

class Player:
    def __init__ (self, letter):
        # letter is either X or O
        self.letter = letter

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)  # Call the initialization of the superclass Player

    def getMove(self, game, letter):
        # Bot goes first
        if letter == "X":
            if game.numEmptySquares() == 9:                
                square = random.choice(game.availableMoves()) + 1
            else:
                if game.firstSquare == 5:
                    square = BotSquare5(game, letter)
                elif game.firstSquare in (2,4,6,8):
                    square = BotSquare2468(game, letter)
                else:
                    square = BotSquare1379(game, letter)

        # Human goes first
        else:            
            if game.firstSquare == 5:
                square = HumanSquare5(game, letter)
            elif game.firstSquare in (2,4,6,8):
                square = HumanSquare2468(game, letter)
            else:
                square = HumanSquare1379(game, letter)
   
        return square

class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)  # Call the initialization of the superclass Player
    
    # we want all players to get their next move given a game
    def getMove(self, game, letter):
        flag = False
        while flag == False:
            square = input(letter + "'s turn. Input move (1 to 9): ")
            try:
                if square.count(".") >= 1 or (square[0] != "-" and not square.isnumeric()):
                    raise TypeError
                elif int(square) < 1 or int(square) > 9:
                    raise IndexError
                elif int(square) - 1 not in game.availableMoves():
                    raise ValueError
                else:
                    square = int(square)
                    flag = True
            except TypeError:
                print("Wrong data type. Please try again.")
            except ValueError:
                print("Spot already taken. Please try again.")
            except IndexError:
                print("Invalid option. Please try again.")


        return square

    # we want to ask the player if they're up to another match
    @staticmethod
    def continueGame():
        flag = False
        while flag == False:
            continueGame = input("Do you want to play another match (Yes/No): ")
            try:
                if not ((continueGame.lower() == "yes") or (continueGame.lower() == "no")):
                    raise ValueError
                else:
                    flag = True
            except ValueError:
                print("Please enter 'Yes' or 'No' if you want to play another match.")
        
        return continueGame