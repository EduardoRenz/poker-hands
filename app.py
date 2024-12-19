# %%
import random
from collections import Counter
from constants import RANKS, SUITS


def generate_deck():
    """Cria um baralho padrão de 52 cartas."""
    return [(rank, suit) for rank in RANKS for suit in SUITS]


def pick_random_cards(baralho, card_amount=2):
    """Gera uma mão aleatória de um certo número de cartas."""
    return random.sample(baralho, card_amount)


def remove_from_deck(deck, cards_to_remove):
    for card in cards_to_remove:
        deck.remove(card)
    return deck


def evaluate_hand(mao):
    """Avalia uma mão de poker e retorna a melhor combinação."""
    ranks_mao = sorted([RANKS.index(carta[0]) for carta in mao], reverse=True)
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
        # Verifica a sequência especial A, 2, 3, 4, 5
        return unique_ranks == [RANKS.index('A'), RANKS.index('5'), RANKS.index('4'), RANKS.index('3'), RANKS.index('2')]

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


def evaluate(mao_jogador, board):
    """Avalia a melhor mão de 5 cartas combinando a mão do jogador e o board."""
    from itertools import combinations
    todas_as_cartas = mao_jogador + board
    melhor_combinacao = "High Card"  # Valor inicial
    combinacoes = combinations(todas_as_cartas, 5)

    def valor_combinacao(combinacao_str):
        ordem = ["High Card", "One Pair", "Two Pair", "Three of a Kind",
                 "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush"]
        return ordem.index(combinacao_str)

    for combinacao in combinacoes:
        resultado = evaluate_hand(list(combinacao))
        if valor_combinacao(resultado) > valor_combinacao(melhor_combinacao):
            melhor_combinacao = resultado
    return melhor_combinacao


def get_winner(players_hands, board):
    """Retorna o jogador com a melhor mão de poker."""
    return max(players_hands, key=lambda x: evaluate(x, board))


def get_winner_index(players_hands, board):
    return players_hands.index(get_winner(players_hands, board))


def exibir_carta(carta):
    """Exibe uma carta formatada."""
    return carta[0] + carta[1]


def exibir_mao(mao):
    """Exibe uma mão de cartas formatada."""
    return " ".join(exibir_carta(carta) for carta in mao)


# %%
deck = generate_deck()
# print(deck, len(deck))

mao_jogador = pick_random_cards([('A', 'H'), ('A', 'S')])
print("\nMinha mao")
print(mao_jogador)
deck = remove_from_deck(deck, mao_jogador)

player_2 = pick_random_cards(deck)
print("\nPlayer 2")
print(player_2)
deck = remove_from_deck(deck, player_2)

board = pick_random_cards(deck, 5)
deck = remove_from_deck(deck, board)

print("\nBoard")
print(board)

evaluation = evaluate(mao_jogador, board)
print("\nMatch")
print(evaluation)

winner = get_winner_index([mao_jogador, player_2], board)
print("\nWinner")
print("You" if winner == 0 else "Player 2")


# %%
