import unittest
from connect4 import Connect4



class TestInputValidation(unittest.TestCase):


    def setUp(self):
        self.game = Connect4()


    def testValidNumber(self):
        self.assertTrue(self.game.isValidInput("2"))


    def testInvalidNumber(self):
        self.assertFalse(self.game.isValidInput("10"))


    def testInvalidString(self):
        self.assertFalse(self.game.isValidInput("foo"))
