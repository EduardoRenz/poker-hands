# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")

LETTERS_TO_NUMBERS = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

df_flop = pd.read_csv('data/flop_game_statistics.csv', index_col=0)
df_river = pd.read_csv('data/full_game_statistics.csv', index_col=0)
# Merge two dataframes
df = pd.merge(df_flop, df_river, on='card', suffixes=('_flop', '_river'))
df = df.sort_values(by='wins_river', ascending=False)
df['card_1_number'] = df.index.str[0]
df['card_1_suit'] = df.index.str[1]
df['card_2_number'] = df.index.str[3]
df['card_2_suit'] = df.index.str[4]
# df['only_numbers'] = df['card_1_number'] + df['card_2_number']


# %%
# Join Paired Cards together and remove sigles
df_ranks_grouped = df.query("card_1_number == card_2_number").groupby(['card_1_number', 'card_2_number']).aggregate(
    {'wins_river': 'mean', 'wins_flop': 'mean'}).sort_values(by='wins_river', ascending=False)

df_ranks_grouped.reset_index(inplace=True)
df_ranks_grouped.index = df_ranks_grouped['card_1_number'].astype(
    str) + df_ranks_grouped['card_2_number'].astype(str)

df_ranks_grouped['card_1_suit'] = 'diff'
df_ranks_grouped['card_2_suit'] = 'diff'

df = pd.concat([df, df_ranks_grouped], axis=0, ignore_index=False)

# %%
# Join different suits together
df_diff_suits = df.query("card_2_suit != card_1_suit and card_1_number != card_2_number").groupby(['card_1_number', 'card_2_number']).aggregate(
    {'wins_river': 'mean', 'wins_flop': 'mean'}).sort_values(by='wins_river', ascending=False)

df_diff_suits['card_1_suit'] = 'diff'
df_diff_suits['card_2_suit'] = 'diff'

df_diff_suits.reset_index(inplace=True)
df_diff_suits.index = df_diff_suits['card_1_number'].astype(
    str) + df_diff_suits['card_2_number'].astype(str)
df = pd.concat([df, df_diff_suits], axis=0, ignore_index=False)

# %%
# Join same suits together
df_same_suits = df.query("card_2_suit == card_1_suit and card_1_number != card_2_number").groupby(['card_1_number', 'card_2_number']).aggregate(
    {'wins_river': 'mean', 'wins_flop': 'mean'}).sort_values(by='wins_river', ascending=False)

df_same_suits['card_1_suit'] = 'same'
df_same_suits['card_2_suit'] = 'same'

df_same_suits.reset_index(inplace=True)
df_same_suits.index = df_same_suits['card_1_number'].astype(
    str) + df_same_suits['card_2_number'].astype(str)
df = pd.concat([df, df_same_suits], axis=0)

# %%
# Drop single combinations
df = df.loc[(df.card_1_suit.isin(['diff', 'same']))]


# %%
plt.figure(figsize=(35, 6))
sns.lineplot(data=df, x=df.index,   y='wins_river',
             hue='card_1_suit', palette='Set1')

# %%
plt.figure(figsize=(35, 6))
sns.scatterplot(data=df, x=df.index,   y='wins_river',
                hue='card_1_suit', palette='Set1', size='wins_flop')

# %%
my_cards = 'TK'
df.query(f"index=='{my_cards}' or index=='{my_cards[::-1]}'")
# %%
