import self

from games_cards.Card import Card
from games_cards.DeckOfCards import DeckOfCards
from games_cards.Player import Player
from random import *


class CardGame:

    def __init__(self, number_of_cards = 5):
        if number_of_cards > 13:
            raise ValueError("the number of cards need to be lost of 13 and big of 5")
        if  number_of_cards < 5:
            raise ValueError("the number of cards need to be lost of 13 and big of 5")

        self.number_of_cards = number_of_cards
        self.deckOfCards = DeckOfCards()
        self.players = []

    def deal_cards(self):
        # Distribution cards to players
        if self.number_of_cards > 0:
            for player in self.players:
                for i in range(0, self.number_of_cards):
                    player.add_card(self.deckOfCards.deal_one())
        else:
            print("error - Need to deal more cards than the number of rounds")

    def create_players(self, money):
        # Create 4 players
        for i in range(0, 4):
            name = f"p_{i}"
            self.players.append(Player(name, money, self.number_of_cards))

    def new_game_n(self):
        # Create a deck of cards, hadar money, create players and deal cards to the players
        self.deckOfCards.new_game()
        money = randrange(5000, 10001)
        self.create_players(money)
        self.deal_cards()

    def game_move(self, move_number):
        # Performs a game round (draws, compares, adds and returns a winner)
        self.reduce_players_money(move_number)
        move_cards = self.get_move_cards()
        # print(f" R O U N D -  -  -  {i} \n p_1- {move_cards[0]} p_2- {move_cards[1]} p_3- {move_cards[2]} p_4- {move_cards[3]}")

        self.print_players_cards(move_cards, move_number)
        winning_card = self.compare_cards(move_cards)
        winning_player = self.players[move_cards.index(winning_card)]
        winning_player.add_amount(move_number * 100 * 4)
        print(f"The wining in this round is {winning_player.name}")
        print(f" -- E N D   R O U N D -- \n\n\n")


    def reduce_players_money(self, i):
        # Attracting money from all players
        for player in self.players:
            player.reduce_amount(i * 100)

    def get_move_cards(self):
        # Gets a list of cards for a game round
        listt = []
        for i in range(0, 4):
            varr = self.players[i].get_card()
            # varr = self.players[i].get_card()
            listt.append(varr)
        return listt

    def compare_cards(self, cards_to_compare):
        # Compare cards and return a list from the big to the small
        temp_list = cards_to_compare.copy()
        temp_list.sort(reverse=True)
        return temp_list[0]
    # m


    def win(self):
        # return the players with most money
        # m
        win = 0
        win_player = []
        for player in self.players:
            if player.money >= win:
                win = player.money
                win_player.append(player.name)
        return win_player, win
    # m


    def __repr__(self):
        # Print card game
        return f"players - {self.players}\n cards - {self.deckOfCards}\n number_of_cards - {self.number_of_cards}"

    def print_players_cards(self, move_cards, move_number):
        # Print players, money and card of the round
        i = 0
        print(f"R O U N D -  -  -  {move_number} \n")
        for player in self.players:
            print(player.name, "-", move_cards[i], player.money)
            i = i + 1




