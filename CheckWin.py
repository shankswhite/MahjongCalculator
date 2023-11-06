import InputHandler

class CheckWin:
    def is_valid_group(group):
        """
        Checks if a group of tiles is a valid sequence (chii) or triplet (pon).
        """
        if len(group) == 3:
            if all(tile == group[0] for tile in group):  # All tiles are the same
                return True
            if sorted(group) == list(range(min(group), max(group) + 1)):  # Sequential tiles
                return True
        return False

    def can_win(hand):
        """
        Checks if the given hand can win. This is a simplified check and does not cover all cases.
        """
        # Parse the hand
        parsed_hand = InputHandler.InputHandler.input_handler(hand)
        
        # Check for 4 groups and a pair
        groups = []
        pair_found = False
        for suit, tiles in parsed_hand.items():
            tiles.sort()
            i = 0
            while i < len(tiles):
                if i <= len(tiles) - 3 and CheckWin.is_valid_group(tiles[i:i+3]):
                    groups.append(tiles[i:i+3])
                    i += 3
                elif tiles.count(tiles[i]) >= 2 and not pair_found:
                    pair_found = True
                    i += 2
                else:
                    i += 1

        return len(groups) == 4 and pair_found

    # Test the function with the provided hand
test_hand = "m123456s123p123z54"
print(CheckWin.can_win(test_hand))