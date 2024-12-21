import unittest

from app import get_winner_index, evaluate_hand, evaluate, get_winner
from Deck import Deck


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
        self.assertEqual(evaluate_hand(
            [('A', 'C'), ('7', 'H'), ('Q', 'S'), ('2', 'H'), ('T', 'D')]), 'High Card')

    def test_one_pair(self):
        self.assertEqual(evaluate_hand(
            [('A', 'H'), ('A', 'D'), ('K', 'H'), ('Q', 'H'), ('J', 'H')]), 'One Pair')

    def test_two_pair(self):
        self.assertEqual(evaluate_hand(
            [('A', 'H'), ('A', 'D'), ('K', 'H'), ('K', 'D'), ('J', 'H')]), 'Two Pair')

    def test_three_of_a_kind(self):
        self.assertEqual(evaluate_hand(
            [('A', 'H'), ('A', 'D'), ('A', 'C'), ('K', 'H'), ('J', 'H')]), 'Three of a Kind')

    def test_straight(self):
        self.assertEqual(evaluate_hand(
            [('6', 'D'), ('2', 'H'), ('3', 'H'), ('4', 'C'), ('5', 'H')]), 'Straight')

    def test_flush(self):
        self.assertEqual(evaluate_hand(
            [('2', 'H'), ('2', 'H'), ('3', 'H'), ('6', 'H'), ('5', 'H')]), 'Flush')

    def test_full_house(self):
        self.assertEqual(evaluate_hand(
            [('A', 'H'), ('A', 'D'), ('A', 'C'), ('K', 'H'), ('K', 'D')]), 'Full House')

    def test_four_of_a_kind(self):
        self.assertEqual(evaluate_hand(
            [('A', 'H'), ('A', 'D'), ('A', 'C'), ('A', 'S'), ('K', 'H')]), 'Four of a Kind')

    def test_straight_flush(self):
        self.assertEqual(evaluate_hand(
            [('6', 'H'), ('2', 'H'), ('3', 'H'), ('4', 'H'), ('5', 'H')]), 'Straight Flush')


class TestEvaluate(unittest.TestCase):

    def test_high_card(self):
        self.assertEqual(evaluate([('A', 'H'), ('K', 'S')], [
                         ('2', 'D'), ('3', 'D'), ('Q', 'D'), ('6', 'C'), ('T', 'D')]), 'High Card')

    def test_one_pair(self):
        self.assertEqual(evaluate([('Q', 'H'), ('J', 'H')], [
                         ('8', 'S'), ('A', 'S'), ('K', ' '), ('Q', 'H'), ('6', 'S')]), 'One Pair')

    def test_two_pair(self):
        self.assertEqual(evaluate([('A', 'C'),  ('K', 'H')], [
                         ('A', 'H'), ('2', 'D'), ('K', 'S'), ('6', 'D'), ('J', 'H')]), 'Two Pair')

    def test_three_of_a_kind(self):
        self.assertEqual(evaluate([('A', 'H'), ('A', 'D')], [
                         ('A', 'H'), ('2', 'S'), ('9', 'C'), ('K', 'H'), ('J', 'C')]), 'Three of a Kind')

    def test_straight(self):
        self.assertEqual(evaluate([('2', 'D'), ('3', 'H')], [
                         ('A', 'S'), ('6', 'H'), ('3', 'C'), ('4', 'H'), ('5', 'C')]), 'Straight')

    def test_flush(self):
        self.assertEqual(evaluate([('2', 'H'), ('7', 'H')], [
                         ('A', 'H'), ('9', 'H'), ('3', 'H'), ('4', 'C'), ('5', 'S')]), 'Flush')

    def test_full_house(self):
        self.assertEqual(evaluate([('A', 'H'), ('A', 'D')], [
                         ('A', 'S'), ('8', 'D'), ('8', 'S'), ('4', 'C'), ('6', 'H')]), 'Full House')

    def test_four_of_a_kind(self):
        self.assertEqual(evaluate([('A', 'H'), ('A', 'D')], [
                         ('A', 'S'), ('A', 'C'), ('3', 'C'), ('5', 'S'), ('K', 'H')]), 'Four of a Kind')

    def test_straight_flush(self):
        self.assertEqual(evaluate([('3', 'H'), ('2', 'H')], [
                         ('A', 'S'), ('2', 'S'), ('6', 'H'), ('4', 'H'), ('5', 'H')]), 'Straight Flush')


class TestGetWinner(unittest.TestCase):

    def test_high_card_against_high_card(self):
        player_1 = [('A', 'H'), ('3', 'S')]
        player_2 = [('5', 'D'), ('7', 'H')]
        board = [('8', 'S'), ('K', 'H'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(evaluate_hand(player_1 + board), 'High Card')
        self.assertEqual(evaluate_hand(player_2 + board), 'High Card')
        self.assertEqual(get_winner_index([player_1, player_2,], board), 0)

    def test_tie_of_high_card(self):
        player_1 = [('8', 'H'), ('3', 'S')]
        player_2 = [('8', 'C'), ('3', 'D')]
        board = [('A', 'S'), ('5', 'H'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(evaluate_hand(player_1), 'High Card')
        self.assertEqual(evaluate(player_1, board), 'High Card')
        self.assertEqual(evaluate_hand(player_2), 'High Card')
        self.assertEqual(evaluate(player_2, board), 'High Card')
        self.assertEqual(get_winner_index([player_1, player_2,], board), None)

    def test_one_agains_bigger_one_pair_tie(self):
        player_1 = [('8', 'H'), ('3', 'S')]
        player_2 = [('8', 'C'), ('3', 'D')]
        board = [('8', 'S'), ('5', 'H'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(evaluate(player_1, board), 'One Pair')
        self.assertEqual(evaluate(player_2, board), 'One Pair')
        self.assertEqual(get_winner_index([player_1, player_2,], board), None)

    def test_one_agains_bigger_one_pair(self):
        player_1 = [('8', 'H'), ('3', 'S')]
        player_2 = [('9', 'C'), ('3', 'D')]
        board = [('8', 'S'), ('5', 'H'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(evaluate(player_1, board), 'One Pair')
        self.assertEqual(evaluate(player_2, board), 'One Pair')
        self.assertEqual(get_winner_index([player_1, player_2,], board), 1)

    def test_two_pair_tie(self):
        player_1 = [('8', 'H'), ('3', 'S')]
        player_2 = [('8', 'C'), ('3', 'D')]
        player_3 = [('4', 'C'), ('3', 'D')]
        board = [('8', 'S'), ('3', 'H'), ('2', 'S'), ('T', 'H'), ('9', 'C')]
        self.assertEqual(evaluate(player_1, board), 'Two Pair')
        self.assertEqual(evaluate(player_2, board), 'Two Pair')
        self.assertEqual(evaluate(player_3, board), 'One Pair')
        self.assertEqual(get_winner_index(
            [player_1, player_2, player_3], board), None)

#     def test_three_of_a_kind(self):
#         self.assertEqual(get_winner([(['A', 'H'], ['A', 'D'], ['A', 'C'], ['K', 'H'], [
#                          'J', 'H'])], [(['A', 'H'], ['A', 'D'], ['A', 'C'], ['K', 'H'], ['J', 'H'])]), 0)

#     def test_straight(self):
#         self.assertEqual(get_winner([(['A', 'H'], ['2', 'H'], ['3', 'H'], ['4', 'H'], [
#                          '5', 'H'])], [(['A', 'H'], ['2', 'H'], ['3', 'H'], ['4', 'H'], ['5', 'H'])]), 0)

#     def test_flush(self):
#         self.assertEqual(get_winner([(['A', 'H'], ['2', 'H'], ['3', 'H'], ['4', 'H'], [
#                          '5', 'H'])], [(['A', 'H'], ['2', 'H'], ['3', 'H'], ['4', 'H'], ['5', 'H'])]), 0)

#     def test_full_house(self):
#         self.assertEqual(get_winner([(['A', 'H'], ['A', 'D'], ['A', 'C'], ['K', 'H'], [
#                          'K', 'D'])], [(['A', 'H'], ['A', 'D'], ['A', 'C'], ['K', 'H'], ['K', 'D'])]), 0)

#     def test_four_of_a_kind(self):
#         self.assertEqual(get_winner([(['A', 'H'], ['A', 'D'], ['A', 'C'], ['A', 'S'], [
#                          'K', 'H'])], [(['A', 'H'], ['A', 'D'], ['A', 'C'], ['A', 'S'], ['K', 'H'])]), 0)

#     def test_straight_flush(self):
#         self.assertEqual(get_winner([(['A', 'H'], ['2', 'H'], ['3', 'H'], ['4', 'H'], [
#                          '5', 'H'])], [(['A', 'H'], ['2', 'H'], ['3', 'H'], ['4', 'H'], ['5', 'H'])]), 0)


if __name__ == '__main__':
    unittest.main()
