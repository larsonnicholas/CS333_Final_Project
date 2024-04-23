from cards import Cards
from player import Player

class Game():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.deck = Cards()
        self.playedCards = []

    def startGame(self):
        #Give both players 7 cards each
        for i in range(0,7):
            self.player1.addCard(self.deck.drawCard())
            self.player2.addCard(self.deck.drawCard())
        while True:
            self.playedCards.append(self.deck.drawCard())
            if self.playedCards[0] != "Wild":
                break
            else:
                self.deck.deck.append("Wild")
                self.playedCards = []


    def gameOver(self):
        self.player1 = Player()
        self.player2 = Player()
        self.deck.shuffle()
        self.playedCards = []

    def getTopCard(self):
        if len(self.playedCards) > 0:
            return self.playedCards[-1]
        else: raise Exception

    def checkValidPlay(self, cardIndex, player):
        if cardIndex < player.countCards() and cardIndex >= 0:
            topCard = self.playedCards[-1]
            playerCard = player.hand[cardIndex]
            topCard = topCard.split()
            playerCard = playerCard.split()
            if playerCard[0] == "Wild":
                return 2 #Always a Valid Card, and Wild
            elif playerCard[0] == topCard[0] or playerCard[1] == topCard[1]:
                return 1 #Valid Card
            else: return 0

    def playCard(self, cardIndex, player):
        playerCard = player.hand[cardIndex]
        self.playedCards.append(playerCard)
        player.removeCard(playerCard)
        return playerCard

    def playWild(self, cardIndex, player, pickedColor):
        originalCard = "Wild"
        playerCard = pickedColor + " " + originalCard
        self.playedCards.append(playerCard)
        player.removeCard(originalCard)
        return originalCard
    
    def checkPlayerHand(self, player):
        #Check if the player has a move to make
        topCard = self.playedCards[-1]
        topCard = topCard.split()
        playersCards = "".join(player.hand)
        if topCard[0] in playersCards or topCard[1] in playersCards or "Wild" in player.hand:
            return 1 #Player has a move they can make.
        
        else: return 0 #Player does not have a move they can make, they need to draw.

    def drawPlayer(self, player, count):
        for i in range (0, count):
            player.addCard(self.deck.drawCard())


