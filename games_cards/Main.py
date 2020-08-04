from games_cards.Card import Card
from games_cards.DeckOfCards import DeckOfCards
from games_cards.Player import Player
from games_cards.CardGame import CardGame

# d = DeckOfCards()
# my_game = CardGame(5)
# my_game.new_game()
# print(my_game)
# for i in range(5):
#     for player in my_game.players:
#         player.reduce_amount(100 * i)

# pack = []
# suits = ["Diamond", "Spade", "Heart", "Club"]
# for suit in suits:
#     for num in range(1, 14):
#         c = Card(num, suit)
#         pack.append(c)
#
# print(pack)
#
# p = pack[1]

# print(p.value)



my_game = CardGame(5)
my_game.new_game_n()
for i in range(1, 5):
    my_game.game_move(i)
print(f"the whiner are- {my_game.win()[0]} with {my_game.win()[1]} dollars")
