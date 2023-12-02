from itertools import combinations
import numpy as np
import math

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
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Calculate the probability
probability = calculate_probability()
print(probability)
