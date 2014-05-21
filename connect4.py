import sys
from grid import Grid


class Connect4():
    """
    Plays Terminal Connect 4
    """

    def __init__(self):
        self.grid = Grid()
        self.lastMove = -1


    def runGame(self):
        p1sTurn = False
        self.grid.printGrid()
        self.nextMove(1)
        while not self.grid.isWinningState(self.lastMove) and not self.grid.isFull():
            self.grid.printGrid()
            if p1sTurn:
                self.nextMove(1)
                p1sTurn = False
            else:
                self.nextMove(2)
                p1sTurn = True
        
        self.grid.printGrid()
        if self.grid.isFull():
            print "Oh no! The grid filled up! :("
            return
        if p1sTurn:
            print "Congrats Player 2 - You win!"
        else:
            print "Congrats Player 1 - You win!"
            


    def nextMove(self, player):
        """
        Read and eval the next move
        """
        rawInput = raw_input("Please enter a column player " + str(player) + ": ")

        while not self.isValidInput(rawInput) or not self.grid.canInsert(int(rawInput)):
            rawInput = raw_input("Please enter a number from 0 to " + str(self.grid.getNumCols()) + " for a column that is not full: ")

        col = int(rawInput)
        self.grid.insertToken(col, player)
        self.lastMove = col


    def isValidInput(self, col):
        return col in [str(num) for num in range(0, self.grid.getNumCols())]


if __name__ == "__main__":
    game = Connect4()
    game.runGame()
