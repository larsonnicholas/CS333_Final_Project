class Player():
    def __init__(self):
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)
        return 1
    
    def removeCard(self, card):
        if card in self.hand:
            self.hand.remove(card)
            return 1
        else: return 0

    def countCards(self):
        return len(self.hand)
    