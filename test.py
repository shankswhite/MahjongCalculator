from collections import defaultdict

# Given list of tuples
tuples_list = [(63,1), (63,4), (63,7), (64,1), (64,4), (64,7)]

# Convert list of tuples to dictionary format as requested
result_dict = defaultdict(list)
for k, v in tuples_list:
    result_dict[k].append(v)

# Convert defaultdict to regular dict if needed
result_dict = dict(result_dict)





from math import comb

# 总牌数和7筒的数量
total_cards = 136
tiles_of_interest = 4
drawn_cards = 14

# 计算每种情况的概率
probabilities = {}
for k in range(tiles_of_interest + 1):
    prob = comb(tiles_of_interest, k) * comb(total_cards - tiles_of_interest, drawn_cards - k) / comb(total_cards, drawn_cards)
    probabilities[k] = prob

data = {
    "key1": [1, 2, 3],
    "key2": [4, 5, 6],
    "key3": [7, 8, 9]
}
zipped_values = zip(*data.values())

# 对每一组相同位置的元素进行求和
summed_values = [sum(value_group) for value_group in zipped_values]

# 更新参数为新的问题
drawn_tile_times = 30  # 游戏过程中总共抽取的牌数
left_tike_mountain = 70

# 重新计算每种情况的概率
# probabilities_game = {}
# for k in range(tiles_of_interest + 1):
#     prob_game = comb(tiles_of_interest, k) * comb(total_cards - tiles_of_interest, drawn_cards_game - k) / comb(total_cards, drawn_cards_game)
#     probabilities_game[k] = prob_game

# print(probabilities_game)


# for k in range(0, min(tiles_of_interest + 1, 14 + 1)):
#     ron_prob = comb(tiles_of_interest, k) * comb(136 - tiles_of_interest, drawn_tile_times - k)


    # （牌山中还有多少张waiting_tile, 手牌中有多少张waiting_tile) * (牌山中除了waiting_tile还有多少张，)
    # (20, 1) * （136-20，


from itertools import combinations
import numpy as np

def calculate_probability():
    total_balls = 10
    red_balls = 3
    white_balls = total_balls - red_balls
    initial_draw = 3
    rounds = total_balls - initial_draw  # number of rounds after the initial draw

    # Calculate the probability of drawing 0, 1, 2, or 3 red balls initially
    comb_total = comb(total_balls, initial_draw)
    prob_initial = [comb(red_balls, i) * comb(white_balls, initial_draw - i) / comb_total for i in range(4)]

    # Function to calculate probability of discarding at least one red ball in subsequent rounds
    def prob_discard_at_least_one_red(initial_reds):
        # If already have at least one red ball, the probability is 1 (since we must discard at least one)
        if initial_reds > 0:
            return 1.0

        # If no red balls initially, calculate the probability of drawing and discarding at least one red
        prob_no_red_discarded = 1.0
        remaining_red = red_balls
        remaining_total = total_balls - initial_draw

        for r in range(rounds):
            # Probability of not drawing a red ball in this round
            prob_not_draw_red = (remaining_total - remaining_red) / remaining_total
            # Update the probability of no red ball being discarded up to this round
            prob_no_red_discarded *= prob_not_draw_red

            # Update remaining balls
            remaining_total -= 1
            if prob_not_draw_red < 1:
                remaining_red -= 1

        return 1 - prob_no_red_discarded

    # Calculate the overall probability
    overall_prob = sum(prob_initial[i] * prob_discard_at_least_one_red(i) for i in range(4))

    return overall_prob

# Function to calculate combinations
def comb(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

# Calculate the probability
probability = calculate_probability()

print([1,2] + [3,4])