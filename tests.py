import unittest

from app import generate_deck, pick_random_cards, evaluate_hand, evaluate, get_winner


class TestGenerateDeck(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(generate_deck()), 52)


class TestPickRandomCards(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(pick_random_cards(generate_deck())), 2)

    def test_cards(self):
        deck = generate_deck()
        cards = pick_random_cards(deck)
        for card in cards:
            self.assertIn(card, deck)


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
            [('A', 'D'), ('2', 'H'), ('3', 'H'), ('4', 'C'), ('5', 'H')]), 'Straight')

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
        self.assertEqual(evaluate([('A', 'H'), ('2', 'H'), ('3', 'H'), ('4', 'H'), ('5', 'H')], [
                         ('A', 'H'), ('2', 'H'), ('3', 'H'), ('4', 'H'), ('5', 'H')]), 'Straight Flush')


# class TestGetWinner(unittest.TestCase):

#     def test_high_card(self):
#         self.assertEqual(get_winner([(['A', 'H'], ['K', 'H'], ['Q', 'H'], ['J', 'H'], [
#                          'T', 'H'])], [(['A', 'D'], ['K', 'D'], ['Q', 'D'], ['J', 'D'], ['T', 'D'])]), 0)

#     def test_one_pair(self):
#         self.assertEqual(get_winner([(['A', 'H'], ['A', 'D'], ['K', 'H'], ['Q', 'H'], [
#                          'J', 'H'])], [(['A', 'H'], ['A', 'D'], ['K', 'H'], ['Q', 'H'], ['J', 'H'])]), 0)

#     def test_two_pair(self):
#         self.assertEqual(get_winner([(['A', 'H'], ['A', 'D'], ['K', 'H'], ['K', 'D'], [
#                          'J', 'H'])], [(['A', 'H'], ['A', 'D'], ['K', 'H'], ['K', 'D'], ['J', 'H'])]), 0)

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
