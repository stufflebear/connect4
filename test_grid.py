import unittest
from grid import Grid



class TestGridInit(unittest.TestCase):


    def testGridSize(self):
        grid = Grid()
        self.assertEqual(len(grid.getGrid()), 6)
        self.assertEqual(len(grid.getGrid()[0]), 7)



class TestCanInsert(unittest.TestCase):


    def setUp(self):
        self.grid = Grid()


    def testEmptyGrid(self):
        for col in range(0, self.grid.getNumCols()):
            self.assertTrue(self.grid.canInsert(col))


    def testPartiallyFilled(self):
        self.grid.insertToken(1, 2)
        self.assertTrue(self.grid.canInsert(1))


    def testFilledCol(self):
        col = 3
        for row in range(0, self.grid.getNumRows()):
            self.grid.insertToken(col, 2)
        self.assertFalse(self.grid.canInsert(col))
        self.assertTrue(self.grid.canInsert(4))



class TestGetColumnCopy(unittest.TestCase):


    def testSanity(self):
        grid = Grid()
        grid.insertToken(2, 2)
        grid.insertToken(2, 1)
        column = grid.getColumnCopy(2)
        self.assertEqual(column, [0, 0, 0, 0, 1, 2])
        


class TestGetDiagonalRight(unittest.TestCase):


    def testSanity(self):
        grid = Grid()
        grid.insertToken(1, 1)
        grid.insertToken(1, 2)
        grid.insertToken(2, 1)
        result = grid.getDiagonalRight(4, 1)
        self.assertEqual(result, [0, 2, 1])



class TestGetDiagonalLeft(unittest.TestCase):


    def testSanity(self):
        grid = Grid()
        grid.insertToken(4, 1)
        grid.insertToken(5, 1)
        grid.insertToken(5, 2)
        result = grid.getDiagonalLeft(4, 5)
        self.assertEqual(result, [1, 2, 0])



class TestFourAdjacentTiles(unittest.TestCase):


    def setUp(self):
        self.grid = Grid()


    def testThreeInARow(self):
        row = [0, 1, 0, 1, 1, 1, 0]
        self.assertFalse(self.grid.isFourAdjacent(row))


    def testFourInARow(self):
        row = [0, 0, 1, 1, 1, 1, 0]
        self.assertTrue(self.grid.isFourAdjacent(row))
