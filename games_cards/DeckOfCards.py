from games_cards.Card import Card
from random import *


class DeckOfCards:

    def __init__(self):
        # Create a deck of cards
        self.pack = []
        suits = ["Diamond", "Spade", "Heart", "Club"]
        for suit in suits:
            for num in range(1, 14):
                c = Card(num, suit)
                self.pack.append(c)

    def shuffle_dec(self):
        # Shuffling a deck of cards
        shuffle(self.pack)

    def deal_one(self):
        # deal card from deck of cards
        return self.pack.pop(0)

    def new_game(self):
        # Create a deck of cards and shuffle the deck
        self.pack = []
        suits = ["Diamond", "Spade", "Heart", "Club"]
        for suit in suits:
            for num in range(1, 14):
                c = Card(num, suit)
                self.pack.append(c)
        shuffle(self.pack)

    def show(self):
        # Print a deck of card
        return f"pack- {self.pack}"

    def __repr__(self):
        # Print a deck of card
        return self.show()
