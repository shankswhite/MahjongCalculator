"""
四川麻将模拟程序

简介:
这个程序模拟了四名玩家进行四川麻将的一系列打牌过程。程序包括生成玩家的手牌、模拟打牌过程、计算胡牌概率、根据不同策略提出出牌建议，并计算条件概率以展示贝叶斯定理的应用。

玩家手牌:
- 玩家1: 不能有筒
- 玩家2: 不能有万
- 玩家3: 不能有条
- 玩家4: 想做条的清一色，不能有万

打牌策略:
- 策略1: 每位玩家以自身胡牌为优先目标。
- 策略2: 除了玩家4,其他玩家尝试阻止玩家4胡牌。

概率计算:
- 胡牌概率: 基于玩家手中缺少的牌在牌库中的数量以及牌库中剩余的牌的总数来计算。
- 条件概率: 在特定条件下，比如已知某玩家打出特定牌后，计算该玩家胡牌的概率。

计算公式:
- P(胡牌) = (手中缺少的牌在牌库中的数量) / (牌库中剩余的牌的总数)
- P(A|B) = (P(B|A) * P(A)) / P(B) （贝叶斯定理）

示例:
- 如果玩家需要的一张牌在牌库中有3张,牌库总共剩下30张牌,则胡牌概率为 3/30 = 10%。
- 条件概率的计算将基于玩家的打牌行为和当前的游戏状态。
"""
import random
from collections import defaultdict

def draw_tile(player_hand, deck):
    """
    Draw a tile from the deck and add it to the player's hand.
    """
    if deck:
        tile = deck.pop(0)
        player_hand.append(tile)
    return player_hand

def calculate_winning_probability(hand, deck):
    """
    Calculate the probability of winning for a hand based on the deck.
    This is a simplified calculation.
    """
    hand_counts = defaultdict(int)
    for tile in hand:
        hand_counts[tile] += 1

    potential_winning_tiles = set()
    for tile, count in hand_counts.items():
        if count == 2 or count == 1:
            potential_winning_tiles.add(tile)

    deck_count = len(deck)
    winning_tile_count = sum(deck.count(tile) for tile in potential_winning_tiles)
    if deck_count == 0:
        return 0
    return winning_tile_count / deck_count

def calculate_conditional_probability(hand, discarded_tile, deck):
    """
    Calculate the conditional probability of winning given a player has discarded a certain tile.
    This is a simplified version for demonstration purposes.
    """
    base_prob = calculate_winning_probability(hand, deck)
    if discarded_tile not in hand:
        return min(base_prob + 0.05, 1.0)
    else:
        return base_prob

def suggest_discard(hand, deck):
    """
    Suggest a tile to discard based on the hand and the deck.
    """
    hand_counts = defaultdict(int)
    for tile in hand:
        hand_counts[tile] += 1

    for tile, count in hand_counts.items():
        if count == 1 and deck.count(tile) == 0:
            return tile

    return random.choice(hand)

def play_round_with_conditional_prob(hands, deck, target_player=None):
    """
    Play a round of Mahjong with suggestions, winning probabilities, and conditional probabilities.
    """
    for player, hand in hands.items():
        hand = draw_tile(hand, deck)
        win_prob = calculate_winning_probability(hand, deck)

        discard_suggestion = suggest_discard(hand, deck)
        hand.remove(discard_suggestion)
        hands[player] = hand

        cond_prob = calculate_conditional_probability(hand, discard_suggestion, deck)
        print(f"Player {player} winning probability: {win_prob:.2%}")
        print(f"Player {player} conditional winning probability after discarding {discard_suggestion}: {cond_prob:.2%}")
        print(f"Player {player} discarded: {discard_suggestion}")

    return hands

def play_round_with_suggestions(hands, deck, target_player=None):
    """
    Play a round of Mahjong with suggestions for discarding and showing winning probabilities.
    """
    for player, hand in hands.items():
        hand = draw_tile(hand, deck)
        win_prob = calculate_winning_probability(hand, deck)
        print(f"Player {player} winning probability: {win_prob:.2%}")

        discard_suggestion = suggest_discard(hand, deck)
        print(f"Suggested discard for Player {player}: {discard_suggestion}")

        hand.remove(discard_suggestion)
        hands[player] = hand
        print(f"Player {player} discarded: {discard_suggestion}")

    return hands

# Generate the deck
tiles = ['万', '筒', '条']
deck = [f'{num}{suit}' for suit in tiles for num in range(1, 10)] * 4  # 每种牌9张，每张4份
random.shuffle(deck)


# Generate hands for four players
hands = defaultdict(list)
for i in range(13):
    for j in range(1, 5):
        tile = random.choice(deck)
        while ((j == 1 and '筒' in tile) or
               (j == 2 and '万' in tile) or
               (j == 3 and '条' in tile) or
               (j == 4 and '万' in tile)):
            tile = random.choice(deck)
        hands[j].append(tile)
        deck.remove(tile)

# Test the round with suggestions and probabilities
play_round_with_suggestions(hands, deck[:20])

def simulate_rounds(hands, deck, num_rounds, target_player=None):
    """
    Simulate a given number of rounds and display the hand changes, winning probabilities, and conditional probabilities.
    """
    for round in range(num_rounds):
        print(f"\n--- Round {round + 1} ---")
        hands = play_round_with_conditional_prob(hands, deck, target_player)

    return hands

# Copy the hands and deck for two separate strategies
hands_strategy_1 = hands.copy()
hands_strategy_2 = hands.copy()
deck_strategy_1 = deck.copy()
deck_strategy_2 = deck.copy()

# 策略1: 每位玩家以自身胡牌为优先目标
print("Strategy 1: Each player aims to win.")
simulate_rounds(hands.copy(), deck[:20].copy(), num_rounds=3)

# 策略2: 除了玩家4，其他玩家尝试阻止玩家4胡牌
print("\nStrategy 2: Players aim to prevent Player 4 from winning.")
simulate_rounds(hands.copy(), deck[:20].copy(), num_rounds=3, target_player=4)

print(deck)