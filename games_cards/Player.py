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


