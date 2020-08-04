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

    def test__init___1(self):
        # check the len of the deck cards
        self.assertEqual(52, (len(self.d_card.pack)))

    def test_shuffle_dec(self):
        # check the shuffle of the deck cards after "shuffle_dec"

        # var_1 = self.d_card.pack[1]
        # self.d_card.shuffle_dec()
        # var_2 = self.d_card.pack[1]
        # self.assertNotEqual(var_1, var_2)

        temp_list = self.d_card.pack.copy()
        self.d_card.shuffle_dec()
        self.assertNotEqual(self.d_card.pack, temp_list)

    def test_deal_one(self):
        # check the deck cards after "deal_one" and check the number of card after that
        self.assertNotIn(self.d_card.deal_one(), self.d_card.pack)
        self.assertEqual(51, (len(self.d_card.pack)))

    def test_new_game_1(self):
        # check the creation of the pack cards after "new_game" with the number of card in the pack
        self.d_card.new_game()
        self.assertEqual(52, len(self.d_card.pack))

    def test_new_game_2(self):
        # check the shuffle of the pack cards after "new_game"
        temp_list = self.d_card.pack.copy()
        self.d_card.new_game()
        self.assertNotEqual(temp_list, self.d_card.pack)

    def test_print(self):
        # check the print of the pack
        show_pack = "pack- [ 1 Diamond,  2 Diamond,  3 Diamond,  4 Diamond,  5 Diamond,  6 Diamond,  7 Diamond,  8 Diamond,  9 Diamond, 10 Diamond, 11 Diamond, 12 Diamond, 13 Diamond,  1 Spade  ,  2 Spade  ,  3 Spade  ,  4 Spade  ,  5 Spade  ,  6 Spade  ,  7 Spade  ,  8 Spade  ,  9 Spade  , 10 Spade  , 11 Spade  , 12 Spade  , 13 Spade  ,  1 Heart  ,  2 Heart  ,  3 Heart  ,  4 Heart  ,  5 Heart  ,  6 Heart  ,  7 Heart  ,  8 Heart  ,  9 Heart  , 10 Heart  , 11 Heart  , 12 Heart  , 13 Heart  ,  1 Club   ,  2 Club   ,  3 Club   ,  4 Club   ,  5 Club   ,  6 Club   ,  7 Club   ,  8 Club   ,  9 Club   , 10 Club   , 11 Club   , 12 Club   , 13 Club   ]"
        self.assertEqual(show_pack, self.d_card.__repr__())

