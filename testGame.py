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
        

if __name__ == "__main__":
    unittest.main()