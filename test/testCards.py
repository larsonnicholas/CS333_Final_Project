import unittest
from cards import Cards

class testInitialize(unittest.TestCase):
    def setUp(self):
        self.decks = Cards()

    def testDeckQuantity(self):
        self.assertEqual(len(self.decks.deck), 56)

    def testCardTypeCount(self):
        self.assertEqual(sum("Blue" in card for card in self.decks.deck), 13)
        self.assertEqual(sum("0" in card for card in self.decks.deck), 4)

class testDraw(unittest.TestCase):
    def setUp(self):
        self.decks = Cards()

    def testDeckDrawOne(self):
        drawn = self.decks.drawCard()
        self.assertEqual(len(self.decks.deck), 55)
        self.assertNotIn(drawn, self.decks.deck)

    def testDeckDrawFour(self):
        for i in range(0,4):
            self.decks.drawCard()
        self.assertEqual(len(self.decks.deck), 52)

class testShuffle(unittest.TestCase):
    def setUp(self):
        self.decks = Cards()

    def testShuffleFull(self):
        self.decks.shuffle()
        self.assertEqual(len(self.decks.deck), 56)

    def testShuffleEmpty(self):
        self.decks.deck = []
        self.decks.shuffle()
        self.assertEqual(len(self.decks.deck), 56)
        self.assertEqual(sum("Blue" in card for card in self.decks.deck), 13)

if __name__ == "__main__":
    unittest.main()