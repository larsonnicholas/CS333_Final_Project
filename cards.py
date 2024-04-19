from random import randrange

class Cards():
    def __init__(self):
        self.colors = ["Blue", "Red", "Yellow", "Green"]
        self.cardTypes = ['0','1','2','3','4','5','6','7','8','9','Reverse','Skip','+2','Wild']
        self.deck = [ x + " " + y for x in self.colors for y in self.cardTypes]

    def drawCard(self):
        length = len(self.deck)
        randCard = self.deck[randrange(length)]
        self.deck.remove(randCard)
        return randCard
    
    def shuffle(self):
        self.deck = [ x + y for x in self.colors for y in self.cardTypes]

if __name__ == "__main__":
    newDeck = Cards()
    print(newDeck.deck)