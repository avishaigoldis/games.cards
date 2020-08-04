from unittest import TestCase
from unittest.mock import patch
from games_cards.CardGame import CardGame
from games_cards.Card import Card
from games_cards.Player import Player


class TestCardGame(TestCase):

    def setUp(self):
        print("Set_up")
        self.my_game = CardGame(5)
        self.my_game.new_game_n()

    def tearDown(self):
        print("Tear_down")

    def test_create_players_1(self):
        # check that "create_players" create 4 players
        self.my_game.create_players(5000)
        self.assertTrue(4, len(self.my_game.players))


    def test_reduce_players_money_1(self):
        # check money after "reduce_players_money" in player 1 in game found 1 (the difference is 100)
        before_money = self.my_game.players[0].money
        self.my_game.reduce_players_money(1)
        after_money = self.my_game.players[0].money
        self.assertEqual(before_money, after_money+100)

    def test_reduce_players_money_2(self):
        # check money after "reduce_players_money" in player 1 in game found 3 (the difference is 300)
        before_money = self.my_game.players[0].money
        self.my_game.reduce_players_money(3)
        after_money = self.my_game.players[0].money
        self.assertEqual(before_money, after_money+300)

    def test_reduce_players_money_3(self):
        # check money after "reduce_players_money" in player 2 in game found 1 (the difference is 100)
        before_money = self.my_game.players[1].money
        self.my_game.reduce_players_money(1)
        after_money = self.my_game.players[1].money
        self.assertEqual(before_money, after_money+100)

    def test_reduce_players_money_4(self):
        # check money after "reduce_players_money" in player 2 in game found 3 (the difference is 300)
        before_money = self.my_game.players[1].money
        self.my_game.reduce_players_money(3)
        after_money = self.my_game.players[1].money
        self.assertEqual(before_money, after_money+300)

    def test_get_cards(self):
        # check "get_cards"
        list_test = self.my_game.get_move_cards()
        print(list_test)
        self.assertEqual(len(list_test), 4)

    def test_compare_cards_1(self):
        # check "compare_cards" to 4 cards in list (check value).
        self.c1 = Card(5, "Heart")
        self.c2 = Card(1, "Spade")
        self.c3 = Card(12, "Heart")
        self.c4 = Card(13, "Club")
        temp_list = [self.c1, self.c2, self.c3, self.c4]
        self.assertEqual(self.my_game.compare_cards(temp_list), self.c4)

    def test_compare_cards_2(self):
        # check "compare_cards" to 4 cards in list (check suit).
        self.c1 = Card(13, "Heart")
        self.c2 = Card(13, "Spade")
        self.c3 = Card(13, "Heart")
        self.c4 = Card(13, "Club")

        temp_list = [self.c1, self.c2, self.c3, self.c4]
        self.assertEqual(self.my_game.compare_cards(temp_list), self.c4)

    def test_compare_cards_3(self):
        # check "compare_cards" to 4 cards in list.
        self.c1 = Card(13, "Heart")
        self.c2 = Card(13, "Spade")
        self.c3 = Card(13, "Heart")
        self.c4 = Card(13, "Club")
        temp_list = [self.c1, self.c2, self.c3, self.c4]
        self.assertEqual(self.my_game.compare_cards(temp_list), self.c4)

    def test_win(self):
        # check that "win" return 4 player.
        self.assertEqual(len(self.my_game.win()[0]), 4)

    # def test_create_players_2(self):
    #     # check that "create_players" create 4 player.
    #     self.my_game.create_players(5000)
    #     self.assertEqual(len(self.my_game.players.money), 5000)

    # def test_deal_cards(self):
    #     self.list_cards= [self.c1, self.c2, self.c3, self.c4, self.c1, self.c2, self.c3, self.c4]
    #     with patch('games_cards.DeckOfCards.DeckOfCards.deal_one') as mocked_deal_one:
    #         mocked_deal_one.return_value = self.list_cards
    #         for i in range(0, 2):
    #             self.my_game.deal_cards()
    #             print(self.my_game)
