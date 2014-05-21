class Grid():
    """
    A game grid for Connect 4
    """


    def __init__(self):
        self.grid = []
        self._numCols = 7
        self._numRows = 6
        for num in range(0, self._numRows):
            row = []
            for num in range(0, self._numCols):
                row.append(0)
            self.grid.append(row)


    def setValue(self, row, col, player):
        self.grid[row][col] = player


    def insertToken(self, col, player):
        if self.canInsert(col):
            descending = range(0, self._numRows)
            descending.reverse()
            for row in descending:
                if self.getValue(row, col) == 0:
                    self.setValue(row, col, player)
                    return


    def canInsert(self, col):
        return self.getValue(0, col) == 0


    def isFourAdjacent(self, slice):
        """
        Checks if a player has 4 adjacent tiles in a silce
        """
        lastPlayer = -1
        count = 1
        for player in slice:
            if player != 0:
                if player == lastPlayer:
                    count += 1
                    if count >= 4:
                        return True
                else:
                    lastPlayer = player
                    count = 1
            else:
                lastPlayer = -1
                count = 1
        return False


    def getTopToken(self, column):
        for index in range(0, len(column)):
            if column[index] != 0:
                return index
        raise Exception("Tried to get a top token from an empty column")


    def inBounds(self, row, col):
        rowInBounds = row in range(0, self.getNumRows())
        colInBounds = col in range(0, self.getNumCols())
        return rowInBounds and colInBounds


    def getColumnCopy(self, col):
        column = []
        for row in range(0, self.getNumRows()):
            column.append(self.grid[row][col])
        return column


    def getDiagonalRight(self, row, col):
        """
        get diagonal that goes from top left to bottom right
        """
        diagonal = []

        #left walk
        rowIndex = row
        colIndex = col
        while self.inBounds(rowIndex, colIndex):
            diagonal = [self.getValue(rowIndex, colIndex)] + diagonal
            rowIndex -= 1
            colIndex -= 1

        #right walk
        rowIndex = row + 1
        colIndex = col + 1
        while self.inBounds(rowIndex, colIndex):
            diagonal.append(self.getValue(rowIndex, colIndex))
            rowIndex += 1
            colIndex += 1

        return diagonal


    def getDiagonalLeft(self, row, col):
        """
        get diagonal that goes from bottom left to top right
        """
        diagonal = []

        #left walk
        rowIndex = row
        colIndex = col
        while self.inBounds(rowIndex, colIndex):
            diagonal = [self.getValue(rowIndex, colIndex)] + diagonal
            rowIndex += 1
            colIndex -= 1

        #right walk
        rowIndex = row - 1
        colIndex = col + 1
        while self.inBounds(rowIndex, colIndex):
            diagonal.append(self.getValue(rowIndex, colIndex))
            rowIndex -= 1
            colIndex += 1

        return diagonal


    def isWinningState(self, col):
        column = self.getColumnCopy(col)

        rowIndex = self.getTopToken(column)
        row = self.grid[rowIndex]
        
        diagonalRight = self.getDiagonalRight(rowIndex, col)
        diagonalLeft = self.getDiagonalLeft(rowIndex, col)

        for slice in [diagonalRight, diagonalLeft, row, column]:
            if self.isFourAdjacent(slice):
                return True
        return False


    def isFull(self):
        return not 0 in self.getGrid()[0]


    def printGrid(self):
        for row in self.getGrid():
            print row
        print "\n"


    #############
    # Accessors #
    #############

    def getNumCols(self):
        return self._numCols


    def getNumRows(self):
        return self._numRows


    def getGrid(self):
        return self.grid


    def getValue(self, row, col):
        return self.getGrid()[row][col]
