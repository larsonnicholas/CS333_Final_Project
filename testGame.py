import unittest
from game import Game
from player import Player
from cards import Cards

class testStartGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.player1 = self.game.player1
        self.player2 = self.game.player2
        self.deck = self.game.deck

    def testStartGame(self):
        self.assertEqual(self.player1.hand, [])
        self.assertEqual(self.player2.hand, [])
        self.assertEqual(len(self.deck.deck), 56)
        self.assertEqual(len(self.game.playedCards), 0)
        self.game.startGame()
        self.assertEqual(len(self.player1.hand), 7)
        self.assertEqual(len(self.player2.hand), 7)
        self.assertEqual(len(self.deck.deck), 41)
        self.assertEqual(len(self.game.playedCards), 1)

class testGameOver(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.player1.hand = ["Red 5", "Wild", "Green Skip"]
        self.game.player2.hand = ["Blue 0"]
        self.game.deck.deck = []

    def testGameOver(self):
        self.assertNotEqual(self.game.player1.hand, [])
        self.assertNotEqual(self.game.player2.hand, [])
        self.assertNotEqual(len(self.game.deck.deck), 56)
        self.game.gameOver()
        self.assertEqual(self.game.player1.hand, [])
        self.assertEqual(self.game.player2.hand, [])
        self.assertEqual(len(self.game.deck.deck), 56)
        self.assertEqual(len(self.game.playedCards), 0)        

class testGetTopCard(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.playedCards = ["Yellow 8"]

    def testGetTopCardOne(self):
        self.assertEqual(self.game.getTopCard(), "Yellow 8")

    def testGetTopCardTwo(self):
        self.game.playedCards.append("Green 2")
        self.assertEqual(self.game.getTopCard(), "Green 2")

    def testGetTopCardNone(self):
        self.game.playedCards = []
        with self.assertRaises(Exception):
            self.game.getTopCard()

class testCheckValidPlay(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.player1 = self.game.player1
        self.player1.hand = ["Blue 5", "Red 9", "Wild", "Red 8", "Blue 9"]
        self.game.playedCards = ["Blue 9"]

    def testValidPlaySameColor(self):
        self.assertEqual(self.game.checkValidPlay(0, self.player1), 1)

    def testValidPlaySameNumber(self):
        self.assertEqual(self.game.checkValidPlay(1,self.player1), 1)

    def testValidPlayWildCard(self):
        self.assertEqual(self.game.checkValidPlay(2, self.player1), 2)

    def testValidPlayNotMatch(self):
        self.assertEqual(self.game.checkValidPlay(3, self.player1), 0)

    def testValidPlayPerfectMatch(self):
        self.assertEqual(self.game.checkValidPlay(4, self.player1), 1)
    
class testPlayCard(unittest.TestCase):
    def setUp(self):
        self.game = Game()

if __name__ == "__main__":
    unittest.main()