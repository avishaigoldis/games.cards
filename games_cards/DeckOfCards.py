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

