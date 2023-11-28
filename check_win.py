import input_handler
class CheckWin:
    @staticmethod
    def check_win(list_):
        # Check for a winning hand in the given list of tiles.
        # This is a simplified version and may not cover all Mahjong rules.
        list_ = sorted(list_)
        
        def is_set_or_pair(lst):
            if len(lst) == 3:
                return lst[0] == lst[1] == lst[2] or lst[0] + 1 == lst[1] and lst[1] + 1 == lst[2]
            if len(lst) == 2:
                return lst[0] == lst[1]
            return False

        def recursive_check(lst):
            if len(lst) == 0:
                return True
            if len(lst) % 3 != 0:
                return False
            for i in range(len(lst)):
                for j in range(i+1, len(lst)):
                    for k in range(j+1, len(lst)):
                        if is_set_or_pair([lst[i], lst[j], lst[k]]):
                            new_lst = lst[:i] + lst[i+1:j] + lst[j+1:k] + lst[k+1:]
                            if recursive_check(new_lst):
                                return True
            return False

        # Check for a pair and then try to form sets with the remaining tiles.
        for i in range(len(list_)):
            for j in range(i+1, len(list_)):
                if list_[i] == list_[j]:
                    if recursive_check(list_[:i] + list_[i+1:j] + list_[j+1:]):
                        return True
        return False


    @staticmethod
    def find_waiting_tiles(hand):
        waiting_tiles = []
        for i in range(len(hand)):
            test_hand = hand[:i] + hand[i+1:]
            for tile in tile_range:
                if CheckWin.check_win(test_hand + [tile]):
                    waiting_tiles.append((hand[i], tile))
        return waiting_tiles

tile_range = list(range(1, 10)) + list(range(21, 30)) + list(range(41, 50)) + list(range(61, 82, 3))

# Example hand
# example_hand = [1, 2, 3, 21, 22, 23, 28, 27, 41, 42, 43, 63, 63, 66]
# waiting_tiles = CheckWin.find_waiting_tiles(example_hand)

# print(waiting_tiles)


# tiles = input_handler.InputHandler.input_handler('123m122337p123s11z')

# print(CheckWin.check_win(tiles))