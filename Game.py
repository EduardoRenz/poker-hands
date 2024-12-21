from constants import RANKS, STRENGTH_ORDER, NUMERAL_RANKS
from collections import Counter


class Game:

    def evaluate(self, mao_jogador, board):
        """Avalia a melhor mão de 5 cartas combinando a mão do jogador e o board."""
        from itertools import combinations
        todas_as_cartas = mao_jogador + board
        melhor_combinacao = "High Card"  # Valor inicial
        combinacoes = combinations(todas_as_cartas, 5)

        def valor_combinacao(combinacao_str):
            ordem = STRENGTH_ORDER
            return ordem.index(combinacao_str)

        for combinacao in combinacoes:
            resultado = self.get_combination(list(combinacao))
            if valor_combinacao(resultado) > valor_combinacao(melhor_combinacao):
                melhor_combinacao = resultado
        return melhor_combinacao

    def get_combination(self, mao):
        """Avalia uma mão de poker e retorna a melhor combinação."""
        ranks_mao = sorted([RANKS.index(carta[0])
                           for carta in mao], reverse=True)
        suits_mao = [carta[1] for carta in mao]

        # Funções auxiliares para verificar combinações
        def is_flush():
            return len(set(suits_mao)) == 1

        def is_straight():
            unique_ranks = sorted(list(set(ranks_mao)), reverse=True)
            if len(unique_ranks) < 5:
                return False
            # Verifica sequências normais
            for i in range(len(unique_ranks) - 4):
                if all(unique_ranks[i+j] == unique_ranks[i] - j for j in range(5)):
                    return True

        rank_counts = Counter(ranks_mao)
        counts = sorted(rank_counts.values(), reverse=True)

        if is_flush() and is_straight():
            return "Straight Flush"
        if counts[0] == 4:
            return "Four of a Kind"
        if counts[0] == 3 and counts[1] == 2:
            return "Full House"
        if is_flush():
            return "Flush"
        if is_straight():
            return "Straight"
        if counts[0] == 3:
            return "Three of a Kind"
        if counts[0] == 2 and counts[1] == 2:
            return "Two Pair"
        if counts[0] == 2:
            return "One Pair"
        return "High Card"

    def get_winner(self, players_hands, board):
        """Returns the player with the best hand."""

        results = []
        for hand in players_hands:
            results.append(self.evaluate(hand, board))

        best_hand = -1
        best_match = None
        for i, result in enumerate(results):
            if (best_hand == -1 and best_match is None):
                best_hand = i
                best_match = result
                continue
            if STRENGTH_ORDER.index(result) > STRENGTH_ORDER.index(results[best_hand]):
                best_hand = i
                best_match = result
                continue

            if STRENGTH_ORDER.index(best_match) > STRENGTH_ORDER.index(result):
                continue

            if (STRENGTH_ORDER.index(result) == STRENGTH_ORDER.index(results[best_hand])):
                current_only_numbers_sum = sum([NUMERAL_RANKS[RANKS.index(first)] for first,
                                                second in players_hands[i]])
                best_only_numbers_sum = sum([NUMERAL_RANKS[RANKS.index(first)] for first,
                                            second in players_hands[best_hand]])

                if (current_only_numbers_sum > best_only_numbers_sum):
                    best_hand = i
                    best_match = result
                    continue
                if (current_only_numbers_sum == best_only_numbers_sum):
                    best_hand = -1
                    continue

        if (best_hand == -1):
            return None
        return players_hands[best_hand]

    def get_winner_index(self, players_hands, board):
        winner = self.get_winner(players_hands, board)
        if winner is None:
            return None
        return players_hands.index(winner)
