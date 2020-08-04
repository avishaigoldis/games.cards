from unittest import TestCase
from games_cards.DeckOfCards import DeckOfCards
from games_cards.Card import Card


class TestDeckOfCards(TestCase):

    def setUp(self):
        print("Set_up")
        self.d_card = DeckOfCards()
        self.c1 = Card(1, "Diamond")

    def tearDown(self):
        print("Tear_down")

