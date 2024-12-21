import unittest

from app import get_winner_index
from Deck import Deck
from Game import Game

game = Game()


class TestGenerateDeck(unittest.TestCase):

    def test_length(self):
        deck = Deck()
        self.assertEqual(len(deck.deck), 52)


class TestPickRandomCards(unittest.TestCase):

    def test_length(self):
        deck = Deck()
        self.assertEqual(len(deck.pick_random_cards()), 2)

    def test_pick_cards(self):
        deck = Deck()
        cards = deck.pick_random_cards()
        for card in cards:
            self.assertNotIn(card, deck.deck)


class TestEvaluateHand(unittest.TestCase):

    def test_high_card(self):
        self.assertEqual(game.get_combination(
            [('A', 'C'), ('7', 'H'), ('Q', 'S'), ('2', 'H'), ('T', 'D')]), 'High Card')

    def test_one_pair(self):
        self.assertEqual(game.get_combination(
            [('A', 'H'), ('A', 'D'), ('K', 'H'), ('Q', 'H'), ('J', 'H')]), 'One Pair')

    def test_two_pair(self):
        self.assertEqual(game.get_combination(
            [('A', 'H'), ('A', 'D'), ('K', 'H'), ('K', 'D'), ('J', 'H')]), 'Two Pair')

    def test_three_of_a_kind(self):
        self.assertEqual(game.get_combination(
            [('A', 'H'), ('A', 'D'), ('A', 'C'), ('K', 'H'), ('J', 'H')]), 'Three of a Kind')

    def test_straight(self):
        self.assertEqual(game.get_combination(
            [('6', 'D'), ('2', 'H'), ('3', 'H'), ('4', 'C'), ('5', 'H')]), 'Straight')

    def test_flush(self):
        self.assertEqual(game.get_combination(
            [('2', 'H'), ('2', 'H'), ('3', 'H'), ('6', 'H'), ('5', 'H')]), 'Flush')

    def test_full_house(self):
        self.assertEqual(game.get_combination(
            [('A', 'H'), ('A', 'D'), ('A', 'C'), ('K', 'H'), ('K', 'D')]), 'Full House')

    def test_four_of_a_kind(self):
        self.assertEqual(game.get_combination(
            [('A', 'H'), ('A', 'D'), ('A', 'C'), ('A', 'S'), ('K', 'H')]), 'Four of a Kind')

    def test_straight_flush(self):
        self.assertEqual(game.get_combination(
            [('6', 'H'), ('2', 'H'), ('3', 'H'), ('4', 'H'), ('5', 'H')]), 'Straight Flush')


class TestEvaluate(unittest.TestCase):

    def test_high_card(self):
        self.assertEqual(game.evaluate([('A', 'H'), ('K', 'S')], [
                         ('2', 'D'), ('3', 'D'), ('Q', 'D'), ('6', 'C'), ('T', 'D')]), 'High Card')

    def test_one_pair(self):
        self.assertEqual(game.evaluate([('Q', 'H'), ('J', 'H')], [
                         ('8', 'S'), ('A', 'S'), ('K', ' '), ('Q', 'H'), ('6', 'S')]), 'One Pair')

    def test_two_pair(self):
        self.assertEqual(game.evaluate([('A', 'C'),  ('K', 'H')], [
                         ('A', 'H'), ('2', 'D'), ('K', 'S'), ('6', 'D'), ('J', 'H')]), 'Two Pair')

    def test_three_of_a_kind(self):
        self.assertEqual(game.evaluate([('A', 'H'), ('A', 'D')], [
                         ('A', 'H'), ('2', 'S'), ('9', 'C'), ('K', 'H'), ('J', 'C')]), 'Three of a Kind')

    def test_straight(self):
        self.assertEqual(game.evaluate([('2', 'D'), ('3', 'H')], [
                         ('A', 'S'), ('6', 'H'), ('3', 'C'), ('4', 'H'), ('5', 'C')]), 'Straight')

    def test_flush(self):
        self.assertEqual(game.evaluate([('2', 'H'), ('7', 'H')], [
                         ('A', 'H'), ('9', 'H'), ('3', 'H'), ('4', 'C'), ('5', 'S')]), 'Flush')

    def test_full_house(self):
        self.assertEqual(game.evaluate([('A', 'H'), ('A', 'D')], [
                         ('A', 'S'), ('8', 'D'), ('8', 'S'), ('4', 'C'), ('6', 'H')]), 'Full House')

    def test_four_of_a_kind(self):
        self.assertEqual(game.evaluate([('A', 'H'), ('A', 'D')], [
                         ('A', 'S'), ('A', 'C'), ('3', 'C'), ('5', 'S'), ('K', 'H')]), 'Four of a Kind')

    def test_straight_flush(self):
        self.assertEqual(game.evaluate([('3', 'H'), ('2', 'H')], [
                         ('A', 'S'), ('2', 'S'), ('6', 'H'), ('4', 'H'), ('5', 'H')]), 'Straight Flush')


class TestGetWinner(unittest.TestCase):

    def test_high_card_against_high_card(self):
        player_1 = [('A', 'H'), ('3', 'S')]
        player_2 = [('5', 'D'), ('7', 'H')]
        board = [('8', 'S'), ('K', 'H'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(game.get_combination(player_1 + board), 'High Card')
        self.assertEqual(game.get_combination(player_2 + board), 'High Card')
        self.assertEqual(get_winner_index([player_1, player_2,], board), 0)

    def test_tie_of_high_card(self):
        player_1 = [('8', 'H'), ('3', 'S')]
        player_2 = [('8', 'C'), ('3', 'D')]
        board = [('A', 'S'), ('5', 'H'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(game.get_combination(player_1), 'High Card')
        self.assertEqual(game.evaluate(player_1, board), 'High Card')
        self.assertEqual(game.get_combination(player_2), 'High Card')
        self.assertEqual(game.evaluate(player_2, board), 'High Card')
        self.assertEqual(get_winner_index([player_1, player_2,], board), None)

    def test_one_agains_bigger_one_pair_tie(self):
        player_1 = [('8', 'H'), ('3', 'S')]
        player_2 = [('8', 'C'), ('3', 'D')]
        board = [('8', 'S'), ('5', 'H'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(game.evaluate(player_1, board), 'One Pair')
        self.assertEqual(game.evaluate(player_2, board), 'One Pair')
        self.assertEqual(get_winner_index([player_1, player_2,], board), None)

    def test_one_agains_bigger_one_pair(self):
        player_1 = [('8', 'H'), ('3', 'S')]
        player_2 = [('9', 'C'), ('3', 'D')]
        board = [('8', 'S'), ('5', 'H'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(game.evaluate(player_1, board), 'One Pair')
        self.assertEqual(game.evaluate(player_2, board), 'One Pair')
        self.assertEqual(get_winner_index([player_1, player_2,], board), 1)

    def test_two_pair_tie(self):
        player_1 = [('8', 'H'), ('3', 'S')]
        player_2 = [('8', 'C'), ('3', 'D')]
        player_3 = [('4', 'C'), ('3', 'D')]
        board = [('8', 'S'), ('3', 'H'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(game.evaluate(player_1, board), 'Two Pair')
        self.assertEqual(game.evaluate(player_2, board), 'Two Pair')
        self.assertEqual(game.evaluate(player_3, board), 'One Pair')
        self.assertEqual(get_winner_index(
            [player_1, player_2, player_3], board), None)

    def test_two_pair(self):
        player_1 = [('9', 'C'), ('A', 'D')]
        player_2 = [('8', 'H'), ('3', 'S')]
        board = [('8', 'S'), ('3', 'H'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(game.evaluate(player_2, board), 'Two Pair')
        self.assertEqual(game.evaluate(player_1, board), 'One Pair')
        self.assertEqual(get_winner_index([player_1, player_2,], board), 1)

    def test_three_of_a_kind_tie(self):
        player_1 = [('8', 'H'), ('3', 'S')]
        player_2 = [('8', 'C'), ('3', 'D')]
        player_3 = [('K', 'C'), ('7', 'D')]
        board = [('8', 'S'), ('8', 'D'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(game.evaluate(player_1, board), 'Three of a Kind')
        self.assertEqual(game.evaluate(player_2, board), 'Three of a Kind')
        self.assertEqual(game.evaluate(player_3, board), 'One Pair')
        self.assertEqual(get_winner_index(
            [player_1, player_2, player_3], board), None)

    def test_three_of_a_kind(self):
        player_1 = [('8', 'H'), ('3', 'S')]
        player_2 = [('K', 'C'), ('3', 'D')]
        board = [('8', 'S'), ('8', 'D'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(game.evaluate(player_1, board), 'Three of a Kind')
        self.assertEqual(game.evaluate(player_2, board), 'One Pair')
        self.assertEqual(get_winner_index([player_1, player_2,], board), 0)

    def test_full_house(self):
        player_1 = [('8', 'H'), ('3', 'S')]
        player_2 = [('K', 'C'), ('Q', 'D')]
        board = [('8', 'S'), ('8', 'D'), ('2', 'S'), ('3', 'H'), ('9', 'C')]
        self.assertEqual(game.evaluate(player_1, board), 'Full House')
        self.assertEqual(game.evaluate(player_2, board), 'One Pair')
        self.assertEqual(get_winner_index([player_1, player_2,], board), 0)

    def test_four_of_a_kind(self):
        player_1 = [('8', 'H'), ('8', 'S')]
        player_2 = [('K', 'C'), ('Q', 'D')]
        board = [('8', 'D'), ('8', 'C'), ('2', 'S'), ('8', 'H'), ('9', 'C')]
        self.assertEqual(game.evaluate(player_1, board), 'Four of a Kind')
        self.assertEqual(game.evaluate(player_2, board), 'Three of a Kind')
        self.assertEqual(get_winner_index([player_1, player_2,], board), 0)

    def test_straight_flush(self):
        player_1 = [('3', 'S'), ('5', 'S')]
        player_2 = [('K', 'C'), ('Q', 'D')]
        board = [('4', 'S'), ('6', 'S'), ('7', 'S'), ('8', 'H'), ('9', 'C')]
        self.assertEqual(game.evaluate(player_1, board), 'Straight Flush')
        self.assertEqual(game.evaluate(player_2, board), 'High Card')
        self.assertEqual(get_winner_index([player_1, player_2,], board), 0)

    def test_best_straight(self):
        player_1 = [('3', 'C'), ('4', 'C')]
        player_2 = [('8', 'C'), ('9', 'D')]
        board = [('5', 'S'), ('6', 'S'), ('7', 'S'), ('T', 'H'), ('Q', 'C')]
        self.assertEqual(game.evaluate(player_1, board), 'Straight')
        self.assertEqual(game.evaluate(player_2, board), 'Straight')
        self.assertEqual(get_winner_index([player_1, player_2,], board), 1)

    def test_straight_tie(self):
        player_1 = [('3', 'C'), ('4', 'C')]
        player_2 = [('3', 'S'), ('4', 'D')]
        board = [('5', 'S'), ('6', 'S'), ('7', 'S'), ('T', 'H'), ('Q', 'C')]
        self.assertEqual(game.evaluate(player_1, board), 'Straight')
        self.assertEqual(game.evaluate(player_2, board), 'Straight')
        self.assertEqual(get_winner_index([player_1, player_2,], board), None)


if __name__ == '__main__':
    unittest.main()
