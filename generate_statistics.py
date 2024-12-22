# %%
from constants import RANKS, STRENGTH_ORDER, NUMERAL_RANKS
from Deck import Deck
from Game import Game
from utils import show_cards
import pandas as pd

game = Game()
deck = Deck()
all_two_hands_combinations = []
for first_card in deck.deck:
    for second_card in deck.deck:
        if first_card == second_card:
            continue
        all_two_hands_combinations.append([first_card, second_card])


number_of_games = 100  # How many games to play with test hand
board_cards = 3  # 5 = Full game, 3 = Flop
statistics = []

if __name__ == "__main__":

    for combination in all_two_hands_combinations:

        win_counts = {
            'you': {'wins': 0},
            'player_2': {'wins': 0},
            'player_3': {'wins': 0},
            'player_4': {'wins': 0},
            'player_5': {'wins': 0},
            'player_6': {'wins': 0},
        }

        players_hands = {
            'you': [],
            'player_2': [],
            'player_3': [],
            'player_4': [],
            'player_5': [],
            'player_6': [],
        }
        ties = 0

        for i in range(number_of_games):
            print(f"---------- Rodada {i + 1}------------")
            deck = Deck()

            player_1 = combination
            players_hands['you'] = player_1
            deck.remove_from_deck(player_1)

            print(f"Player  You : {show_cards(player_1)}")
            # pick a card for each player
            for i, player in enumerate(players_hands.keys()):
                if i == 0:
                    continue
                player_hand = deck.pick_random_cards()
                print(f"Player  {player} : {show_cards(player_hand)}")
                players_hands[player] = player_hand

            board = deck.pick_random_cards(board_cards)
            print(f"Board {show_cards(board)}\n")

            # Evaluate each player
            for i, player in enumerate(players_hands.keys()):
                evaluation = game.evaluate(players_hands[player], board)
                print(f"Player  {player}: {evaluation}")

            winner_index = game.get_winner_index(
                [hand for hand in players_hands.values()], board)

            winner_hand = game.get_winner(
                [hand for hand in players_hands.values()], board)

            if (winner_index is None):
                print("Tie")
                ties += 1
                continue

            winner_name = list(players_hands.keys())[winner_index]
            print(f"""\nWinner: {winner_name} with {
                game.evaluate(winner_hand, board)} ({show_cards(winner_hand)}) \n""")

            win_counts[winner_name]['wins'] += 1

        # Statistics of win counts
        for player, win_count in win_counts.items():
            print(f"{player} won {win_count['wins']} times")

        print(f"Ties: {ties}")

        combination_statistic = {
            'card': show_cards(player_1),
            'wins': win_counts['you']['wins']
        }

        statistics.append(combination_statistic)

# %%
df = pd.DataFrame(statistics)
df.to_csv('data/flop_game_statistics.csv', index=False)
# %%
