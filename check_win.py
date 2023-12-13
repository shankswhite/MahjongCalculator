import input_handler
import tkinter as tk
import input_handler
from tile_mapping import TileMapping
from collections import Counter, defaultdict


class CheckWin:
    @staticmethod
    def check_win(hand):
        '''
        check_win -- checks if a hand is a winning hand
        Using recursion
        Parameters:
            hand -- the hand to check
        Returns True if the hand is a winning hand, False otherwise
        '''
        hand = sorted(hand)

        def is_set_or_pair(lst):
            if len(lst) == 3:
                return lst[0] == lst[1] == lst[2] or lst[0] + 1 == lst[1] and lst[1] + 1 == lst[2]
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
                            new_lst = lst[:i] + lst[i+1:j] + \
                                lst[j+1:k] + lst[k+1:]
                            if recursive_check(new_lst):
                                return True
            return False

        # Check for a pair and then try to form sets with the remaining tiles.
        for i in range(len(hand)):
            for j in range(i+1, len(hand)):
                if hand[i] == hand[j]:
                    if recursive_check(hand[:i] + hand[i+1:j] + hand[j+1:]):
                        return True
        return False

    @staticmethod
    def find_waiting_tiles(hand):
        '''
        recursion method to get waiting tiles
        Parameters:
            hand -- the hand to check
        Returns a list of waiting tiles
        '''
        waiting_tiles = []
        for i in range(len(hand)):
            test_hand = hand[:i] + hand[i+1:]
            for tile in tile_range:
                if CheckWin.check_win(test_hand + [tile]):
                    waiting_tiles.append((hand[i], tile))
        return waiting_tiles

    @staticmethod
    def find_1away_waiting_tiles(hand):
        waiting_tiles = []
        for i in range(len(hand)):
            test_hand = hand[:i] + hand[i+1:]
            for tile in tile_range:
                if CheckWin.find_waiting_tiles(test_hand + [tile]):
                    waiting_tiles.append((hand[i], tile))
        return waiting_tiles

    @staticmethod
    def find_2away_waiting_tiles(hand):
        waiting_tiles = []
        for i in range(len(hand)):
            test_hand = hand[:i] + hand[i+1:]
            for tile in tile_range:
                if CheckWin.find_1away_waiting_tiles(test_hand + [tile]):
                    waiting_tiles.append((hand[i], tile))
        return waiting_tiles

    @staticmethod
    def left_(tiles):
        complete = []
        temp = []
        multi_pairs = False
        tiles = sorted(tiles)
        for i in set(tiles):
            if tiles.count(i) >= 2:
                tiles.remove(i)
                tiles.remove(i)
                temp.append((i, i))
                for j in range(int(len(tiles) / 3)):
                    if tiles.count(tiles[0]) >= 3:
                        complete.append((tiles[0], tiles[0], tiles[0]))
                        tiles = tiles[3:]
                    elif tiles[0] in tiles and tiles[0] + 1 in tiles and tiles[0] + 2 in tiles:
                        complete.append((tiles[0], tiles[0] + 1, tiles[0] + 2))
                        tiles.remove(tiles[0] + 2)
                        tiles.remove(tiles[0] + 1)
                        tiles.remove(tiles[0])
        if len(temp) > 1:
            for i in temp:
                if i[0] in tiles:
                    tiles.remove(i[0])
                    temp.remove(i)
                    complete.append((i, i, i))
        if len(temp) > 1:
            for i in temp:
                tiles.append(i)
            multi_pairs = True
        else:
            complete.append(temp[0])
        return [tiles, complete, multi_pairs]

    @staticmethod
    def left__(cards):
        complete = []
        cards = sorted(cards)
        for i in set(cards):
            if cards.count(i) >= 2:
                cards.remove(i)
                cards.remove(i)
                complete.append((i, i))
                for j in range(int(len(cards)/3)):
                    if cards.count(cards[0]) >= 3:
                        complete.append((cards[0], cards[0], cards[0]))
                        cards = cards[3:]
                    elif cards[0] in cards and cards[0]+1 in cards and cards[0]+2 in cards:
                        complete.append((cards[0], cards[0]+1, cards[0]+2))
                        cards.remove(cards[0]+2)
                        cards.remove(cards[0]+1)
                        cards.remove(cards[0])

        return [cards, complete]

# Below is the test code for the above functions.
tile_range = list(range(1, 10)) + list(range(21, 30)) + \
    list(range(41, 50)) + list(range(63, 82, 3))

example_hand_2away = [1, 2, 3, 22, 23, 47, 48, 42, 43, 63, 63, 66, 69, 72]
example_hand_0away = [1, 2, 3, 21, 22, 23, 41, 42, 43, 47, 47, 63, 63, 69]
example_hand_1away = [1, 2, 3, 21, 22, 23, 42, 69, 47, 48, 63, 63, 66, 66]


test = [1, 2, 3, 21, 22, 23, 41, 42, 43, 47, 47, 63, 66, 69]
test2 = [1, 1, 22, 22, 43, 43, 4, 4, 25, 25, 46, 46, 67, 67]
test3 = [1, 1, 2, 2, 3, 3, 43, 63, 63, 66, 66, 47, 48]
test4 = [1, 2, 3, 21, 22, 23, 41, 42, 43, 47, 47, 63, 63, 66]


def main():
    root = tk.Tk()
    root.geometry("1200x800")
    canvas = tk.Canvas(root, width=1200, height=800)
    canvas.pack()
    test1 = input_handler.InputHandler.input_handler("44m667p123678s111z")
    waiting_tiles = CheckWin.find_waiting_tiles(test1)
    result_tiles = defaultdict(set)
    for i, j in waiting_tiles:
        result_tiles[i].add(j)
    result_tiles = dict(result_tiles)

    waiting_message = ''
    for i in result_tiles:

        waiting_list_num = []
        waiting_list_display = []
        waiting_tiles_set = []
        print(i)

        for j in result_tiles[i]:

            waiting_list_num.append(j)
            waiting_list_display.append(TileMapping.tile_mapping[j])
            waiting_tiles_set.append(j)

            waiting_count = len(waiting_tiles_set) * 4

            for tile in []:
                if tile in waiting_tiles_set:
                    waiting_count -= 1

        print(waiting_list_display)
        waiting_message += f"discard {TileMapping.tile_mapping[i]} to wait for {waiting_list_display}, {waiting_count} left, P(Tzumo): 17.59%\n"

        waiting_message_label = tk.Label(
            root, text=waiting_message, font=('Arial Unicode MS', 32), anchor='w')
        canvas.create_window(500, 500, window=waiting_message_label)

    test1_display = ''.join(TileMapping.tile_mapping[tile] for tile in test1)
    x_start = 200
    y_position = 400
    x_offset = 50

    for i, tile in enumerate(test1_display):
        label = tk.Label(root, text=tile, font=('Arial Unicode MS', 48))
        canvas.create_window(x_start + i * x_offset, y_position, window=label)

    root.mainloop()


if __name__ == '__main__':
    main()
