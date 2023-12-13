def evaluate_hand(hand):
    """
    Evaluate the hand and assign scores to each tile based on combinations.
    Scoring:
    - Each set of three consecutive or identical tiles: +1000 points for each tile
    - Each set of two consecutive tiles: +500 points for each tile if not 1 or 9
    - Each set of two consecutive tiles: +100 points for each tile if one of them is 1 or 9
    - Each set of two identical tiles: +500 points for each tile
    - Each set of two tiles with one tile in between: +300 points for each tile
    - All remaining tiles: +100 points minus the tile's value
    Returns a list of scores, each corresponding to the tile in the same position.
    """
    scores = [0] * len(hand)  # Initialize a list of scores with zeros
    pairs = []  # Initialize a list of pairs
    # Helper function to add scores to the list

    def add_score(indexes, score):
        for index in indexes:
            scores[index] += score

    # Step 1: Check for triplets and sequences
    for i in range(len(hand) - 2):
        if hand[i] == hand[i+1] == hand[i+2]:
            add_score([i, i+1, i+2], 1000)
        elif hand[i] + 1 == hand[i+1] and hand[i+1] + 1 == hand[i+2]:
            add_score([i, i+1, i+2], 1000)

    # Step 2: Check for pairs and close tiles
    for i in range(len(hand) - 1):
        if hand[i] == hand[i+1]:
            add_score([i, i+1], 200)
            pairs.append(i)
        elif hand[i] + 1 == hand[i+1]:
            if str(hand[i])[-1] in '19' or str(hand[i+1])[-1] in '19':
                add_score([i, i+1], 100)
            else:
                add_score([i, i+1], 500)
        elif hand[i] + 2 == hand[i+1]:
            add_score([i, i+1], 300)

    # Step 3: Add 100 points minus the tile's value for all remaining tiles
    for i, tile in enumerate(hand):
        if scores[i] == 0:
            scores[i] = 100 - tile

    return list(zip(hand, scores))


# Test the function with the provided example hand
sorted_hand = [1, 2, 3, 4, 5, 29, 29, 44, 44, 44, 47, 48, 64, 64]
hand_scores = evaluate_hand(sorted_hand)


print(hand_scores)
