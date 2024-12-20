from constants import RANKS, SUITS
import random


class Deck:
    deck = None

    def __init__(self):
        self.deck = self.generate_deck()

    def remove_from_deck(self, cards_to_remove):
        for card in cards_to_remove:
            self.deck.remove(card)
        return self.deck

    def generate_deck(self):
        """Creates a standard deck of 52 cards."""
        return [(rank, suit) for rank in RANKS for suit in SUITS]

    def pick_random_cards(self, card_amount=2):
        """Gera uma mão aleatória de um certo número de cartas."""
        sample = random.sample(self.deck, card_amount)
        self.remove_from_deck(sample)
        return sample
