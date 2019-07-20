# simulate 3 decks of cards

import random


class Cards:
    def __init__(self):
        """Initialise card deck"""
        self.deck = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"] * 4 * 3

    def get_deck(self):
        """Return deck"""
        return self.deck

    def shuffle(self):
        """Shuffle deck"""
        random.shuffle(self.deck)

    def draw(self, i):
        """Return card at specific index"""
        return self.deck[i]
