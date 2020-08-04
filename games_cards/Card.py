

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

    def __eq__(self, other):
        # Compar a playing card
        # =
        if self.value == other.value:
            if self.suit == other.suit:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        # Compar a playing card
        # >
        dict = {}
        if self.value > other.value:
            # print("T")
            return True
        elif other.value > self.value:
            # print("F")
            return False
        elif self.value == other.value:
            dict = {"Diamond": 1, "Spade": 2, "Heart": 3, "Club": 4}
            if dict[self.suit] > dict[other.suit]:
                # print("T")
                return True
            else:
                # print("F")
                return False

    def __repr__(self):
        # Print a playing card
        return f"{self.value:>2} {self.suit:<7}"


