from unittest import TestCase
from unittest.mock import patch
from games_cards.Player import Player
from games_cards.Card import Card
from games_cards.DeckOfCards import DeckOfCards



class TestPlayer(TestCase):

    def setUp(self):
        print("Set_up")
        self.c1 = Card(1, "Diamond")
        self.c2 = Card(2, "Diamond")
        self.c3 = Card(3, "Diamond")
        self.c4 = Card(4, "Diamond")
        self.p_1 = Player("p_1", 5000, 5)
        self.list = [self.c1, self.c2, self.c3, self.c4]
        self.dc = DeckOfCards()


    def tearDown(self):
        print("Tear_down")


    def test_set_hand(self):
        # check that after "set_hand" the card in player's cards
        with patch('games_cards.DeckOfCards.DeckOfCards.deal_one') as mocked_deal_one:
            mocked_deal_one.return_value = self.c1
            self.p_1.set_hand(self.dc)
            self.assertIn(self.c1, self.p_1.cards)

    def test_get_card_1(self):
        # check that the card from the list
        self.p_1.cards = [self.c1, self.c2, self.c3, self.c4]
        temp_list = self.p_1.cards.copy()
        card = self.p_1.get_card()
        self.assertIn(card, temp_list)

    def test_get_card_2(self):
        # check that after "get_card" the card not in player's cards
        self.p_1.cards = [self.c1, self.c2, self.c3, self.c4]
        card = self.p_1.get_card()
        self.assertNotIn(card, self.p_1.cards)

    def test_get_card_3(self):
        # check that "get_card" with list empty is ERROR
        self.p_1.cards = []
        self.assertEqual("ERROR", self.p_1.get_card())

    def test_add_card(self):
        # check that after "add_card" the card in player's cards
        self.p_1.add_card(self.c1)
        self.assertIn(self.c1, self.p_1.cards)

    def test_reduce_amount_1(self):
        # check tha change after "reduce_amount"
        self.p_1.reduce_amount(100)
        self.assertEqual(self.p_1.money, 4900)

    def test_reduce_amount_2(self):
        # check tha change after "reduce_amount"
        self.p_1.reduce_amount(100000)
        print(self.p_1.money)
        self.assertEqual(self.p_1.money, 5000)

    def test_add_amount_1(self):
        # check tha change after "reduce_amount"
        self.p_1.add_amount(100)
        self.assertEqual(self.p_1.money, 5100)

    def test_add_amount_2(self):
        # check tha change after "reduce_amount"
        self.p_1.add_amount(100000)
        self.assertEqual(self.p_1.money, 105000)

