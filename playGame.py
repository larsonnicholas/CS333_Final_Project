from game import Game
from player import Player
from time import sleep

def main():
    game = Game()
    print("Wecome to Uno! You should already know the rules. If you don't, better learn fast!")
    game.startGame()
    round = 0
    while True:
        print()
        if round % 2 == 0:
            currentPlayer = game.player1
            otherPlayer = game.player2
            print("Player 1's Turn!")
        else:
            currentPlayer = game.player2
            otherPlayer = game.player1
            print("Player 2's Turn!")

        print(f"Current Top Card:\t{game.getTopCard()}")
        print()
        print("Your Cards:") 

        for i in range(0,currentPlayer.countCards()):
            print(f"{i}. {currentPlayer.hand[i]}")

        if game.checkPlayerHand(currentPlayer) == 1:
            print()
            userSelection = ""
            while True:
                userSelection = input("Which card would you like to put down? (Enter a number): ")
                if int(userSelection) >= 0 and int(userSelection) < currentPlayer.countCards():
                    break
                print("Invalid number! Put in a new one\n")

            userSelection = int(userSelection)
            valid = game.checkValidPlay(userSelection, currentPlayer)

            if valid == 1:
                #Colored card, add to stack and perform any actions if necessary
                usedCard = game.playCard(userSelection, currentPlayer)
                if "Skip" in usedCard:
                    round += 1
                elif "+2" in usedCard:
                    if len(game.deck.deck) < 2:
                        game.deck.shuffle()
                    game.drawPlayer(otherPlayer, 2)
                
            elif valid == 2:
                #Wild card, get color from player
                userColor = ""
                while True:
                    userColor = input("What color would you like to change to?\n1. Blue\n2. Red\n3. Yellow\n4. Green\n\n")
                    if int(userColor) >= 1 and int(userColor) <= 4:
                        break
                    print("Invalid number! Put in a new one\n")
                match userColor:
                    case "1":
                        game.playWild(userSelection, currentPlayer, "Blue")
                    case "2":
                        game.playWild(userSelection, currentPlayer, "Red")
                    case "3":
                        game.playWild(userSelection, currentPlayer, "Yellow")   
                    case "4":
                        game.playWild(userSelection, currentPlayer, "Green")                                             
            else:
                print("You can't put that card down! Try again...\n\n")
                round += 1

        else:
            print("You don't have a card you can use! Automatically drawing one card...")
            sleep(2)
            if len(game.deck.deck) < 1:
                game.deck.shuffle()
            game.drawPlayer(currentPlayer, 1)
        if currentPlayer.countCards() == 0:
            print(f"Congratulations Player {round%2 + 1}! You've won!")
            break
        round += 1
    game.gameOver()


if __name__ == "__main__":
    main()