from unittest import TestCase
from games_cards.Card import Card


class TestCard(TestCase):
    pass

    def setUp(self):
        print("Set_up")
        self.c1 = Card(5, "Heart")
        self.c2 = Card(13, "Spade")
        self.c3 = Card(7, "Heart")
        self.c4 = Card(5, "Diamond")

    def tearDown(self):
        print("Tear_down")

    def test_print(self):
        # check the print of the card
        self.assertEqual(" 5 Diamond", self.c4.__repr__())
        print(self.c4)

    def test_invalid_value_1(self):
        # check card with error value (value = 0)
        self.assertRaises(ValueError, Card, 0, "Diamond")

    def test_invalid_value_2(self):
        # check card with error value (value = 14)
        self.assertRaises(ValueError, Card, 14, "Diamond")

    def test_invalid_value_3(self):
        # check card with error suit (suit = assd)
        self.assertRaises(ValueError, Card, 1, "assd")

    def test__gt__1(self):
        # check "__gt__" with list of 4 cards
        list_cards = [self.c1, self.c2, self.c3, self.c4]
        print(list_cards)
        print(list_cards[0])
        print(type(list_cards[0]))
        self.assertEqual(self.c2 > self.c1, True)
