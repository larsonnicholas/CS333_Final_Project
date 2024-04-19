import unittest
from player import Player

class testAddCard(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def testAddSingleCard(self):
        self.player.addCard("Blue Skip")
        self.assertEqual(len(self.player.hand), 1)
        self.assertIn("Blue Skip", self.player.hand)

    def testAddTwoCards(self):
        self.player.addCard("Blue Skip")
        self.player.addCard("Red 8")
        self.assertEqual(len(self.player.hand), 2)
        self.assertIn("Blue Skip", self.player.hand)
        self.assertIn("Red 8", self.player.hand)

class testRemoveCard(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def testRemoveEmptyHand(self):
        self.assertEqual(self.player.removeCard("Blue 2"), 1)
        self.assertEqual(self.player.hand, [])

    def testRemoveRedCard(self):
        self.player.hand = ["Red Skip"]
        self.assertEqual(self.player.removeCard("Red Skip", 1))
        self.assertEqual(self.player.hand, [])

class testCountCards(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def testCountEmptyHand(self):
        self.assertEqual(self.player.countCards(), 0)

    def testCountCardsInHand(self):
        self.player.hand = ["Green 3", "Yellow 4", "Red 2"]
        self.assertEqual(self.player.countCards(), 3)

if __name__ == "__main__":
    unittest.main()