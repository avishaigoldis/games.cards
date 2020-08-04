# from games_cards.Card import Card
from games_cards.DeckOfCards import DeckOfCards
from random import *
# from games_cards.CardGame import CardGame


class Player:

    def __init__(self, name, money, number_of_cards=5):
        self.name = name
        self.money = money
        self.cards = []
        self.number_of_cards = number_of_cards

    def set_hand(self, DeckOfCards):
        # Pulling a cards from a deck of cards
        for i in range(0, self.number_of_cards):
            self.cards.append(DeckOfCards.deal_one())

    def get_card(self):
        # Pulling a card from a player deck
        if len(self.cards)>0:
            card = self.cards[randrange(0, len(self.cards))]
            self.cards.remove(card)
            return card
        else:
            return "ERROR"

    def add_card(self, card):
        # Adds a card to the player's deck
        self.cards.append(card)

    def reduce_amount(self, sum_reduce):
        # Reduces the amount of money from a player
        if sum_reduce > self.money:
            print("To the player do not have enough money to play")
        else:
            self.money = self.money - sum_reduce

    def add_amount(self, sum_add = 0):
        # Add the amount of money to the player
        self.money = self.money + sum_add

    def __repr__(self):
        # Print player
        return f"name- {self.name} money- {self.money} \n  cards- {self.cards} \n"
