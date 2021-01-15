"""
File: blackjack.py
Author: Cameron Poole
Date: December 20, 2020
Summary:
    This program will play Blackjack with you
in a GUI!!!!
"""
from cards import Deck, Card
from breezypythongui import EasyFrame
from tkinter import *

class Player(object):
    """This class represents a player in
    a blackjack game."""
    def __init__(self, cards):
        self.cards = cards
        self.deck = Deck

        
    def __str__(self):
        """Returns string rep of cards and points."""
        result = ", ".join(map(str, self.cards))
        result += "\n  " + str(self.getPoints()) + " points"
        return result

    def hit(self, card):
        self.cards.append(card)
        

    def getPoints(self):
        """Returns the number of points in the hand."""
        count = 0
        i = 0
        for card in self.cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        # Deduct 10 if Ace is available and needed as 1
        for card in self.cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count -= 10
        return count

    def hasBlackjack(self):
        """Dealt 21 or not."""
        return len(self.cards) == 2 and self.getPoints() == 21 


class Dealer(Player):
    """Like a Player, but with some restrictions."""

    def __init__(self, cards):
        """Initial state: show one card only."""
        Player.__init__(self, cards)
        self.showOneCard = True

    def __str__(self):
        """Return just one card if not hit yet."""
        if self.showOneCard:
            return str(self.cards[0])
        else:
            return Player.__str__(self)

    def hit(self, deck):
        """Add cards while points < 17,
        then allow all to be shown."""
        self.showOneCard = False
        while self.getPoints() < 17:
            self.cards.append(deck.deal())

class Blackjack(object):

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player([self.deck.deal(), self.deck.deal()])
        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])

    def play(self):
        print("Player:\n", self.player)
        print("Dealer:\n", self.dealer)
        while True:
            choice = input("Do you want a hit? [y/n]: ")
            """if self.player.getPoints() == 21:
                secondChance = input("Are you sure you want a hit? You're at 21. [y/n]: ")"""
            if choice in ("Y", "y"):
                self.player.hit(self.deck.deal())
                points = self.player.getPoints()
                print("Player:\n", self.player)
                if points >= 21:
                    break
            else:
                break
        playerPoints = self.player.getPoints()
        if playerPoints > 21:
            print("You bust and lose")
        else:
            self.dealer.hit(self.deck)
            print("Dealer:\n", self.dealer)
            dealerPoints = self.dealer.getPoints()
            if dealerPoints > 21:
                print("Dealer busts and you win")
            elif dealerPoints > playerPoints:
                print("Dealer wins")
            elif dealerPoints < playerPoints and playerPoints <= 21:
                print("You win")
            elif dealerPoints == playerPoints:
                if self.player.hasBlackjack() and not self.dealer.hasBlackjack():
                    print("You win")
                elif not self.player.hasBlackjack() and self.dealer.hasBlackjack():
                    print("Dealer wins")
                else:
                    print("There is a tie")
                          
class CardGUI(EasyFrame):
    i = 1
    a = 1
    o = 1
    wins = 0
    loss = 0
    ties = 0
    twentyOnes = 0
    """Provides our game a GUI"""
    def __init__(self, game):
        """Set up Players Hands"""
        self.game = game

        self.hands = [str(self.game.player.cards[0]), str(self.game.player.cards[1]), "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        self.dealerHands = [str(self.game.dealer.cards[0]), "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        
        """Sets up window and widgets."""
        EasyFrame.__init__(self, title = "Blackjack")
        gamePanel = self.addPanel(row = 0, column = 0, background = "grey")
        gamePanel.addLabel(text = "Your hand", row = 0, column = 0, background = "grey")
        gamePanel.addLabel(text = "Dealer's hand", row = 2, column = 0, background = "grey")

        """Creates spots for cards to be displayed in the GUI"""
        self.playerCard1 = gamePanel.addLabel(text = "", row = 1, column = 0, background = "grey", sticky = "NSEW")
        self.playerCard2 = gamePanel.addLabel(text = "", row = 1, column = 1, background = "grey", sticky = "NSEW") 
        self.playerCard3 = gamePanel.addLabel(text = "", row = 1, column = 2, background = "grey", sticky = "NSEW")
        self.playerCard4 = gamePanel.addLabel(text = "", row = 1, column = 3, background = "grey", sticky = "NSEW")
        self.playerCard5 = gamePanel.addLabel(text = "", row = 1, column = 4, background = "grey", sticky = "NSEW")
        self.playerCard6 = gamePanel.addLabel(text = "", row = 1, column = 5, background = "grey", sticky = "NSEW")
        self.playerCard7 = gamePanel.addLabel(text = "", row = 1, column = 6, background = "grey", sticky = "NSEW")
        self.playerCard8 = gamePanel.addLabel(text = "", row = 1, column = 7, background = "grey", sticky = "NSEW")
        self.playerCard9 = gamePanel.addLabel(text = "", row = 1, column = 8, background = "grey", sticky = "NSEW")
        self.playerCard10 = gamePanel.addLabel(text = "", row = 1, column = 9, background = "grey", sticky = "NSEW")
        self.playerCard11 = gamePanel.addLabel(text = "", row = 1, column = 10, background = "grey", sticky = "NSEW")
        self.dealerCard1 = gamePanel.addLabel(text = "", row = 3, column = 0, background = "grey", sticky = "NSEW")
        self.dealerCard2 = gamePanel.addLabel(text = "", row = 3, column = 1, background = "grey", sticky = "NSEW")
        self.dealerCard3 = gamePanel.addLabel(text = "", row = 3, column = 2, background = "grey", sticky = "NSEW")
        self.dealerCard4 = gamePanel.addLabel(text = "", row = 3, column = 3, background = "grey", sticky = "NSEW")
        self.dealerCard5 = gamePanel.addLabel(text = "", row = 3, column = 4, background = "grey", sticky = "NSEW")
        self.dealerCard6 = gamePanel.addLabel(text = "", row = 3, column = 5, background = "grey", sticky = "NSEW")
        self.dealerCard7 = gamePanel.addLabel(text = "", row = 3, column = 6, background = "grey", sticky = "NSEW")
        self.dealerCard8 = gamePanel.addLabel(text = "", row = 3, column = 7, background = "grey", sticky = "NSEW")
        self.dealerCard9 = gamePanel.addLabel(text = "", row = 3, column = 8, background = "grey", sticky = "NSEW")
        self.dealerCard10 = gamePanel.addLabel(text = "", row = 3, column = 9, background = "grey", sticky = "NSEW")
        self.dealerCard11 = gamePanel.addLabel(text = "", row = 3, column = 10, background = "grey", sticky = "NSEW")

        """Creates control buttons for game functionality like stand, hit, and end game"""
        buttonPanel = self.addPanel(row = 1,            
                                    column = 0,
                                    background = "White")
        buttonPanel.addButton(text = "Stand", row = 0, column = 0, command = self.stand)
        buttonPanel.addButton(text = "Hit", row = 0, column = 1, command = self.GUIhit) # Command button for player.hit
        buttonPanel.addButton(text = "Game Over", row = 0, column = 2, command = self.quit)
        
        self.mapCards(self.hands[0], self.hands[1], self.hands[2], self.hands[3], self.hands[4],
                      self.hands[5], self.hands[6], self.hands[7], self.hands[8], self.hands[9], self.hands[10]) #Calls on the mapCards function and places each index in hands array
        self.mapDealerCards(self.dealerHands[0], self.dealerHands[1], self.dealerHands[2], self.dealerHands[3], self.dealerHands[4],
                            self.dealerHands[5], self.dealerHands[6], self.dealerHands[7], self.dealerHands[8], self.dealerHands[9],
                            self.dealerHands[10])

    def mapCards(self, PlayerCard1, PlayerCard2, PlayerCard3, PlayerCard4, PlayerCard5, PlayerCard6,
                 PlayerCard7, PlayerCard8, PlayerCard9, PlayerCard10, PlayerCard11):
        
        """Take card string as input and finds corresponding .gif for GUI"""
        self.cardImage = "DECK/" + PlayerCard1 + ".gif"
        self.cardImage2 = "DECK/" + PlayerCard2 + ".gif"
        self.cardImage3 = "DECK/" + PlayerCard3 + ".gif"
        self.cardImage4 = "DECK/" + PlayerCard4 + ".gif"
        self.cardImage5 = "DECK/" + PlayerCard5 + ".gif"
        self.cardImage6 = "DECK/" + PlayerCard6 + ".gif"
        self.cardImage7 = "DECK/" + PlayerCard7 + ".gif"
        self.cardImage8 = "DECK/" + PlayerCard8 + ".gif"
        self.cardImage9 = "DECK/" + PlayerCard9 + ".gif"
        self.cardImage10 = "DECK/" + PlayerCard10 + ".gif"
        self.cardImage11 = "DECK/" + PlayerCard11 + ".gif"
        self.image1 = PhotoImage(file = self.cardImage)
        self.image2 = PhotoImage(file = self.cardImage2)
        self.image3 = PhotoImage(file = self.cardImage3)
        self.image4 = PhotoImage(file = self.cardImage4)
        self.image5A = PhotoImage(file = self.cardImage5)
        self.image6A = PhotoImage(file = self.cardImage6)
        self.image7A = PhotoImage(file = self.cardImage7)
        self.image8A = PhotoImage(file = self.cardImage8)
        self.image9A = PhotoImage(file = self.cardImage9)
        self.image10A = PhotoImage(file = self.cardImage10)
        self.image11A = PhotoImage(file = self.cardImage11)
        self.playerCard1["image"] = self.image1
        self.playerCard2["image"] = self.image2
        self.playerCard3["image"] = self.image3
        self.playerCard4["image"] = self.image4
        self.playerCard5["image"] = self.image5A
        self.playerCard6["image"] = self.image6A
        self.playerCard7["image"] = self.image7A
        self.playerCard8["image"] = self.image8A
        self.playerCard9["image"] = self.image9A
        self.playerCard10["image"] = self.image10A
        self.playerCard11["image"] = self.image11A

    def mapDealerCards(self, DealerCard1, DealerCard2, DealerCard3, DealerCard4, DealerCard5,
                       DealerCard6, DealerCard7, DealerCard8, DealerCard9, DealerCard10, DealerCard11):
        """Take the dealer card and display on screen"""
        self.dealercardImage = "DECK/" + DealerCard1 + ".gif"
        self.dealercardImage2 = "DECK/" + DealerCard2 + ".gif"
        self.dealercardImage3 = "DECK/" + DealerCard3 + ".gif"
        self.dealercardImage4 = "DECK/" + DealerCard4 + ".gif"
        self.dealercardImage5 = "DECK/" + DealerCard5 + ".gif"
        self.dealercardImage6 = "DECK/" + DealerCard5 + ".gif"
        self.dealercardImage7 = "DECK/" + DealerCard5 + ".gif"
        self.dealercardImage8 = "DECK/" + DealerCard5 + ".gif"
        self.dealercardImage9 = "DECK/" + DealerCard5 + ".gif"
        self.dealercardImage10 = "DECK/" + DealerCard5 + ".gif"
        self.dealercardImage11 = "DECK/" + DealerCard5 + ".gif"
        self.image1B = PhotoImage(file = self.dealercardImage)
        self.image2B = PhotoImage(file = self.dealercardImage2)
        self.image3B = PhotoImage(file = self.dealercardImage3)
        self.image4B = PhotoImage(file = self.dealercardImage4)
        self.image5B = PhotoImage(file = self.dealercardImage5)
        self.image6B = PhotoImage(file = self.dealercardImage5)
        self.image7B = PhotoImage(file = self.dealercardImage5)
        self.image8B = PhotoImage(file = self.dealercardImage5)
        self.image9B = PhotoImage(file = self.dealercardImage5)
        self.image10B = PhotoImage(file = self.dealercardImage5)
        self.image11B = PhotoImage(file = self.dealercardImage5)
        self.dealerCard1["image"] = self.image1B
        self.dealerCard2["image"] = self.image2B
        self.dealerCard3["image"] = self.image3B
        self.dealerCard4["image"] = self.image4B
        self.dealerCard5["image"] = self.image5B
        self.dealerCard6["image"] = self.image6B
        self.dealerCard7["image"] = self.image7B
        self.dealerCard8["image"] = self.image8B
        self.dealerCard9["image"] = self.image9B
        self.dealerCard10["image"] = self.image10B
        self.dealerCard11["image"] = self.image11B
        
    def seti(self):
        """Increments i"""
        self.i += 1
        self.a += 1
        self.o += 1
 
    def getHit(self, game):
        """Let's hit the player. This will be used in GUIhit"""
        k = 0
        if self.i >= 10:
            hitString = str(self.game.player.cards[10])     #This line cost me 3+ hours of my life.......
            return hitString
        else:
            self.game.player.hit(self.game.deck.deal())
            card = self.game.player.cards[self.i]
            hitString = str(self.game.player.cards[self.i + 1])
            self.game.player.cards[self.i] = card
        self.seti()
        return hitString
         
    def GUIhit(self):
        """Hits the player with a new card in our GUI"""
        if self.game.player.getPoints() == 21:
           self.stand()
        elif self.game.player.getPoints() > 21:
            self.stand()
        else:
            nextCard = self.getHit(self.game)
            self.hands[self.a] = nextCard #Applies the hit card to the following hands index for GUI
            self.mapCards(self.hands[0], self.hands[1], self.hands[2], self.hands[3], self.hands[4],
                          self.hands[5], self.hands[6], self.hands[7], self.hands[8], self.hands[9], self.hands[10])
            if self.game.player.getPoints() >= 21:
                self.stand()
               
    def stand(self):
        """Player doesn't get hit and time to compare scores"""
        dealerPoints = self.game.dealer.getPoints()
        playerPoints = self.game.player.getPoints()
        
        if playerPoints > 21:
            self.messageBox(title = "BUST!", message = "You bust and loose")
            self.loss += 1
            self.refGame()
        else:
            self.game.dealer.hit(self.game.deck)
            i = 0
            for count in range (len(self.game.dealer.cards)):
                self.dealerHands[i] = str(self.game.dealer.cards[i])
                i += 1
            self.mapDealerCards(self.dealerHands[0], self.dealerHands[1], self.dealerHands[2], self.dealerHands[3], self.dealerHands[4],
                                self.dealerHands[5], self.dealerHands[6], self.dealerHands[7], self.dealerHands[8], self.dealerHands[9], self.dealerHands[10])
            if dealerPoints > 21:
                self.messageBox(title = "BUST!", message = "Dealer busts, you win!")
                self.wins += 1
                self.refGame()
            elif dealerPoints > playerPoints:
                self.messageBox(title = "OOF!", message = "Dealer wins this one my guy")
                self.loss += 1
                self.refGame()
            elif dealerPoints < playerPoints and playerPoints <= 21:
                if playerPoints == 21:
                    self.messageBox(title = "YAY", message = "YOU WIN")
                    self.twentyOnes += 1
                    self.wins += 1
                    self.refGame()
                else:
                    self.messageBox(title = "YAY", message = "YOU WIN")
                    self.wins += 1
                    self.refGame()
            elif dealerPoints == playerPoints:
                if self.game.player.hasBlackjack() and not self.game.dealer.hasBlackjack():
                    self.messageBox(title = "YAY", message = "YOU WIN")
                    self.wins += 1
                    self.refGame()
                elif not self.game.player.hasBlackjack() and self.game.dealer.hasBlackjack():
                    self.messageBox(title = "OOF", message = "Dealer wins this one")
                    self.loss += 1
                    self.refGame()
                else:
                    self.messageBox(title = "TIE", message = "There's been a TIE")
                    self.ties += 1
                    self.refGame()
            

    def refGame(self):
        """This function will refresh the game after the stand function has been called"""
        self.game.__init__()
        self.hands = [str(self.game.player.cards[0]), str(self.game.player.cards[1]), "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        self.dealerHands = [str(self.game.dealer.cards[0]), "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        self.mapCards(self.hands[0], self.hands[1], self.hands[2], self.hands[3], self.hands[4],
                      self.hands[5], self.hands[6], self.hands[7], self.hands[8], self.hands[9], self.hands[10])
        self.mapDealerCards(self.dealerHands[0], self.dealerHands[1], self.dealerHands[2], self.dealerHands[3], self.dealerHands[4],
                            self.dealerHands[5], self.dealerHands[6], self.dealerHands[7], self.dealerHands[8], self.dealerHands[9], self.dealerHands[10])
        self.i = 1   #Important to refresh indexing variables for new rounds
        self.a = 1
        self.o = 1
        
    def quit(self): #Will need game.play to restart. This requires game to be passed as an argument after self
        """When user presses 'Game Over' the game will quit with
        information regarding how many games won and how many 21's we've accumulated"""
        self.messageBox(title = "SUMMARY", width = 30, height = 10, message = ("Cameron Poole\nITD-2313\n",
                                                                                 "Games: ", self.wins + self.loss + self.ties,"\nWins: ", self.wins,
                                                                                 "\nLosses: ", self.loss,"\nTies: ", self.ties,
                                                                                 "\nTwenty-ones: ", self.twentyOnes))
        quit()

def main():
    """Instantiate the model and play the game."""
    game = Blackjack()
    CardGUI(game).mainloop()
    
if __name__ == "__main__":
    main()
