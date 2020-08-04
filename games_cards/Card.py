

class Card:

    def __init__(self, value, suit):
        # Create a playing card
        self.value = value
        if self.value <= 0 or self.value > 13:
            self.value = 0
            raise ValueError("value should be between 1 and 13")
        self.suit = suit
        if self.suit not in ["Diamond", "Spade", "Heart", "Club"]:
            raise ValueError("value should be one of: Diamond Spade Heart Club")



    def __repr__(self):
        # Print a playing card
        return f"{self.value:>2} {self.suit:<7}"


