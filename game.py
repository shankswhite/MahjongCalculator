import random
from tile_mapping import TileMapping
from tkinter import PhotoImage
from Others.utility import Utility
import tkinter as tk
import input_handler
import check_win
import discard_tile
from collections import Counter, defaultdict
import Others.utility as utility
from math import comb
from tkinter import messagebox


class Game:
    '''
    Create a Mahjong game object.
    Attributes:
        round: 
            Interger, from 1 to 70
        river_****, hand_****, mountain, dead_wall: 
            List, A list of tiles in the river, hand, mountain, and dead wall
        current_player: 
            Integer, from 1 to 4, the current player
        root: 
            Tkinter root object
        canvas: 
            Tkinter canvas object
        tile_labels: 
            Dictionary, a dictionary of tile labels
        label1_id, label2_id, label3_id, label4_id: 
            List, a list of tile label ids
        player1_message, player2_message, player3_message, player4_message: 
            Tkinter label objects, a label for each player's message
        selected_tiles: 
            Dictionary, a dictionary of selected tiles
        hand1, hand2, hand3, hand4, hand5, hand6, hand7, 
        hand8, hand9, hand10, hand11, hand12, hand13, hand14: 
            Tkinter PhotoImage objects, a list of images for each tile
        hand_list: 
            List, a list of hand images
    '''

    def __init__(self):
        '''
        Initialize the game object.
        Contains a majority of the game logic and data.
        '''
        # river: discraded tile on the table
        self.river_whole = []
        self.river_player1 = []
        self.river_player2 = []
        self.river_player3 = []
        self.river_player4 = []

        # hand: tiles in the hand
        self.hand_player1 = []
        self.hand_player2 = []
        self.hand_player3 = []
        self.hand_player4 = []

        # mountain: tiles in the mountain, which be drawn by each player in each round
        # dead_wall: tiles in the dead wall is valued tile, which cannot be drawn
        self.mountain = []
        self.dead_wall = []

        self.round = 0  # 1-70 round
        self.current_player = 1

        # GUI part
        self.root = tk.Tk()
        self.root.title("Mahjong Layout")
        self.root.geometry('1200x1000')
        self.canvas = tk.Canvas(self.root, width=1200, height=800)
        self.canvas.pack()
        self.tile_labels = {}

        self.get_player1_hand = []
        self.get_player2_hand = []
        self.get_player3_hand = []
        self.get_player4_hand = []
        self.get_mountain = []
        self.get_dead_wall = []

        self.label1_id = []
        self.label2_id = []
        self.label3_id = []
        self.label4_id = []

        self.player1_message = tk.Label(
            self.root, text="", font=('Arial Unicode MS', 24))
        self.player2_message = tk.Label(
            self.root, text="", font=('Arial Unicode MS', 24))
        self.player3_message = tk.Label(
            self.root, text="", font=('Arial Unicode MS', 24))
        self.player4_message = tk.Label(
            self.root, text="", font=('Arial Unicode MS', 24))

        self.selected_tiles = {}

        self.hand1 = 0.0
        self.hand2 = 0.0
        self.hand3 = 0.0
        self.hand4 = 0.0
        self.hand5 = 0.0
        self.hand6 = 0.0
        self.hand7 = 0.0
        self.hand8 = 0.0
        self.hand9 = 0.0
        self.hand10 = 0.0
        self.hand11 = 0.0
        self.hand12 = 0.0
        self.hand13 = 0.0
        self.hand14 = 0.0

        self.hand_list = [self.hand1, self.hand2, self.hand3, self.hand4, 
                          self.hand5, self.hand6, self.hand7, self.hand8, 
                          self.hand9, self.hand10, self.hand11, self.hand12, 
                          self.hand13, self.hand14]

        self.waiting_message = ''

        self.known_tiles = []

    def start_game(self, way="random"):
        '''
        Start the game. 
        '''

        m_tiles = [i for i in range(1, 10) for _ in range(4)]
        p_tiles = [i for i in range(21, 30) for _ in range(4)]
        s_tiles = [i for i in range(41, 50) for _ in range(4)]
        z_tiles = [i for i in range(63, 82, 3) for _ in range(4)]

        tiles = m_tiles + p_tiles + s_tiles + z_tiles
        random.shuffle(tiles)

        self.round = 0
        if way == "random":
            self.hand_player1 = tiles[1:14]
            self.hand_player2 = tiles[14:27]
            self.hand_player3 = tiles[27:40]
            self.hand_player4 = tiles[40:53]
            self.mountain = tiles[53:123]
            self.dead_wall = tiles[123:136]
        elif way == "1":
            self.hand_player1 = input_handler.InputHandler.input_handler(
                "4566777m234s666p")
            self.hand_player2 = input_handler.InputHandler.input_handler(
                "123456789m123s1z")
            self.hand_player3 = input_handler.InputHandler.input_handler(
                "123456789m123s1z")
            self.hand_player4 = input_handler.InputHandler.input_handler(
                "123456789m123s1z")
            self.mountain = input_handler.InputHandler.input_handler(
                "123446785mz1234", is_hand=False)
            self.dead_wall = input_handler.InputHandler.input_handler(
                "123456789m123s1z", is_hand=False)
        elif way == "2":
            self.hand_player1 = input_handler.InputHandler.input_handler(
                "123456789p778s2s")
            self.hand_player2 = input_handler.InputHandler.input_handler(
                "44m667p123678s11z")
            self.hand_player3 = input_handler.InputHandler.input_handler(
                "44m667p123678s11z")
            self.hand_player4 = input_handler.InputHandler.input_handler(
                "44m667p123678s11z")
            self.mountain = input_handler.InputHandler.input_handler(
                "2s111111111111111111z", is_hand=False)
            self.dead_wall = input_handler.InputHandler.input_handler(
                "123456789m123s1z", is_hand=False)
            self.river_player2 = input_handler.InputHandler.input_handler(
                "6699s", is_hand=False)
        elif way == "3":
            self.hand_player1 = input_handler.InputHandler.input_handler(
                "123456999p789s1z")
            self.hand_player2 = input_handler.InputHandler.input_handler(
                "2647589875612s")
            self.hand_player3 = input_handler.InputHandler.input_handler(
                "6475898152637m")
            self.hand_player4 = input_handler.InputHandler.input_handler(
                "4675920178642p")
            self.mountain = input_handler.InputHandler.input_handler(
                "2s456p111111111111111z", is_hand=False)
            self.dead_wall = input_handler.InputHandler.input_handler(
                "123456789m123s1z", is_hand=False)

        elif way == "test":
            self.hand_player1 = self.get_player1_hand
            self.hand_player2 = self.get_player2_hand
            self.hand_player3 = self.get_player3_hand
            self.hand_player4 = self.get_player4_hand
            self.mountain = self.get_mountain
            self.dead_wall = self.get_dead_wall

            temp_list_filled = []
            for i in [self.hand_player1, self.hand_player2, self.hand_player3, self.hand_player4, self.mountain, self.dead_wall]:
                if len(i) != 0:
                    temp_list_filled.append(i)

            removal_counter = Counter(
                item for sublist in temp_list_filled for item in sublist)

            new_list = []
            for item in tiles:
                if removal_counter[item] > 0:
                    removal_counter[item] -= 1
                else:
                    new_list.append(item)

            if len(self.hand_player1) == 0:
                self.hand_player1 = new_list[:14]
                new_list = new_list[14:]
            if len(self.hand_player2) == 0:
                self.hand_player2 = new_list[:14]
                new_list = new_list[14:]
            if len(self.hand_player3) == 0:
                self.hand_player3 = new_list[:14]
                new_list = new_list[14:]
            if len(self.hand_player4) == 0:
                self.hand_player4 = new_list[:14]
                new_list = new_list[14:]
            if len(self.mountain) == 0:
                self.mountain = new_list[:70]
                new_list = new_list[70:]
            if len(self.dead_wall) == 0:
                self.dead_wall = new_list[:14]
                new_list = new_list[14:]

        self.canvas.delete("all")
        self.tile_labels.clear()
        self.draw_tile(self.current_player)

        self.display_layout()

    def __str__(self):
        mountain_str = "Mountain: " + \
            ' '.join(str(tile) for tile in self.mountain)
        player1_hand = "Player 1: " + \
            ' '.join(str(tile) for tile in self.hand_player1)
        player2_hand = "Player 2: " + \
            ' '.join(str(tile) for tile in self.hand_player2)
        player3_hand = "Player 3: " + \
            ' '.join(str(tile) for tile in self.hand_player3)
        player4_hand = "Player 4: " + \
            ' '.join(str(tile) for tile in self.hand_player4)
        player1_river = "Player 1: " + \
            ' '.join(str(tile) for tile in self.river_player1)
        player2_river = "Player 2: " + \
            ' '.join(str(tile) for tile in self.river_player2)
        player3_river = "Player 3: " + \
            ' '.join(str(tile) for tile in self.river_player3)
        player4_river = "Player 4: " + \
            ' '.join(str(tile) for tile in self.river_player4)

        return (
            f"Round: {self.round}\n"
            f"{mountain_str}\n"
            f"{player1_hand}\n"
            f"{player2_hand}\n"
            f"{player3_hand}\n"
            f"{player4_hand}\n"
            f"{player1_river}\n"
            f"{player2_river}\n"
            f"{player3_river}\n"
            f"{player4_river}\n"
        )

    def display_layout(self):
        '''
        Display the layout by Tkinter.
        '''
        hand_player1_sorted = sorted(self.hand_player1)
        hand_player2_sorted = sorted(self.hand_player2)
        hand_player3_sorted = sorted(self.hand_player3)
        hand_player4_sorted = sorted(self.hand_player4)

        hand_player1_display = hand_player1_sorted
        hand_player2_display = hand_player2_sorted
        hand_player3_display = hand_player3_sorted
        hand_player4_display = hand_player4_sorted

        river_player1_display = self.river_player1
        river_player2_display = self.river_player2
        river_player3_display = self.river_player3
        river_player4_display = self.river_player4

        TileMapping.load_images()

        for i, tile in enumerate(hand_player1_display):
            label = tk.Label(self.root, image=TileMapping.loaded_images[tile], font=(
                'Arial Unicode MS', 18))
            label.bind('<Button-1>', lambda event, t=tile,
                       l=label: self.next_round_auto(l, t, manual=True))

            self.label1_id.append(self.canvas.create_window(
                300 + i*35, 600, window=label))
            self.selected_tiles[tile] = False

        # TODO: Another way to display possibilities for discarding tiles.
        # for i, value in enumerate(self.hand_list):
        #     label = tk.Label(self.root, image=value, font=('Arial Unicode MS', 15))
        #     self.canvas.create_window(300 + i*35, 650, window=label)

        for i, tile in enumerate(hand_player2_display):
            label = tk.Label(self.root, image=TileMapping.loaded_images[tile], font=(
                'Arial Unicode MS', 18))
            self.label2_id.append(self.canvas.create_window(
                850, 150 + i*36, window=label))

        for i, tile in enumerate(hand_player3_display):
            label = tk.Label(self.root, image=TileMapping.loaded_images[tile], font=(
                'Arial Unicode MS', 18))
            self.label3_id.append(self.canvas.create_window(
                700 - i*35, 50, window=label))

        for i, tile in enumerate(hand_player4_display):
            label = tk.Label(self.root, image=TileMapping.loaded_images[tile], font=(
                'Arial Unicode MS', 18))
            self.label4_id.append(self.canvas.create_window(
                150, 550 - i*35, window=label))

        for i, tile in enumerate(river_player1_display):
            label = tk.Label(self.root, image=TileMapping.loaded_images[tile], font=(
                'Arial Unicode MS', 18))
            if i >= 12:
                self.canvas.create_window(450 + (i-12)*21, 520, window=label)
            elif i >= 6:
                self.canvas.create_window(450 + (i-6)*21, 485, window=label)
            else:
                self.canvas.create_window(450 + i*21, 450, window=label)

        for i, tile in enumerate(river_player2_display):
            label = tk.Label(self.root, image=TileMapping.loaded_images[tile], font=(
                'Arial Unicode MS', 18))
            if i >= 12:
                self.canvas.create_window(650, 240 + (i-12)*35, window=label)
            elif i >= 6:
                self.canvas.create_window(615, 240 + (i-6)*35, window=label)
            else:
                self.canvas.create_window(580, 240 + i*35, window=label)

        for i, tile in enumerate(river_player4_display):
            label = tk.Label(self.root, image=TileMapping.loaded_images[tile], font=(
                'Arial Unicode MS', 18))
            if i >= 12:
                self.canvas.create_window(345, 240 + (i-12)*35, window=label)
            elif i >= 6:
                self.canvas.create_window(380, 240 + (i-6)*35, window=label)
            else:
                self.canvas.create_window(415, 240 + i*35, window=label)

        for i, tile in enumerate(river_player3_display):
            label = tk.Label(self.root, image=TileMapping.loaded_images[tile], font=(
                'Arial Unicode MS', 18))
            if i >= 12:
                self.canvas.create_window(550 - (i-12)*21, 130, window=label)
            elif i >= 6:
                self.canvas.create_window(550 - (i-6)*21, 165, window=label)
            else:
                self.canvas.create_window(550 - i*21, 200, window=label)

        self.next_round_auto_button = tk.Button(
            self.root, text="Next   Round   Auto", command=self.next_round_auto)
        self.canvas.create_window(
            1000, 200, window=self.next_round_auto_button)

        def get_input():
            try:
                self.get_player1_hand = input_handler.InputHandler.input_handler(
                    entry1.get())  # Get the text from the entry
                self.get_player2_hand = input_handler.InputHandler.input_handler(
                    entry2.get())  # Get the text from the entry
                self.get_player3_hand = input_handler.InputHandler.input_handler(
                    entry3.get())  # Get the text from the entry
                self.get_player4_hand = input_handler.InputHandler.input_handler(
                    entry4.get())  # Get the text from the entry
                self.get_mountain = input_handler.InputHandler.input_handler(
                    entry5.get())  # Get the text from the entry
                self.get_dead_wall = input_handler.InputHandler.input_handler(
                    entry6.get())  # Get the text from the entry
            except ValueError as e:
                messagebox.showerror('Error', e)

                Game.start_game(self)

            Game.start_game(self, way="test")

            self.display_layout()

        self.canvas.create_window(500, 700, window=self.player1_message)
        self.canvas.create_window(800, 350, window=self.player2_message)
        self.canvas.create_window(500, 20, window=self.player3_message)
        self.canvas.create_window(50, 350, window=self.player4_message)

        entry1 = tk.Entry(self.root, width=20)
        entry2 = tk.Entry(self.root, width=20)
        entry3 = tk.Entry(self.root, width=20)
        entry4 = tk.Entry(self.root, width=20)
        entry5 = tk.Entry(self.root, width=20)
        entry6 = tk.Entry(self.root, width=20)

        self.canvas.create_window(1000, 400, window=entry1)
        self.canvas.create_window(1000, 450, window=entry2)
        self.canvas.create_window(1000, 500, window=entry3)
        self.canvas.create_window(1000, 550, window=entry4)
        self.canvas.create_window(1000, 600, window=entry5)
        self.canvas.create_window(1000, 650, window=entry6)
        label = tk.Label(self.root, text="player1",
                         font=('Arial Unicode MS', 18))
        self.canvas.create_window(1150, 400, window=label)
        label = tk.Label(self.root, text="player2",
                         font=('Arial Unicode MS', 18))
        self.canvas.create_window(1150, 450, window=label)
        label = tk.Label(self.root, text="player3",
                         font=('Arial Unicode MS', 18))
        self.canvas.create_window(1150, 500, window=label)
        label = tk.Label(self.root, text="player4",
                         font=('Arial Unicode MS', 18))
        self.canvas.create_window(1150, 550, window=label)
        label = tk.Label(self.root, text="mountain",
                         font=('Arial Unicode MS', 18))
        self.canvas.create_window(1150, 600, window=label)
        label = tk.Label(self.root, text="wall", font=('Arial Unicode MS', 18))
        self.canvas.create_window(1150, 650, window=label)

        update_button = tk.Button(
            self.root, text='Set Table', command=get_input)
        self.canvas.create_window(1050, 700, window=update_button)

        waiting_message = tk.Label(self.root, text=self.waiting_message, font=(
            'Arial Unicode MS', 18), anchor='w')
        self.canvas.create_window(400, 800, window=waiting_message)

    def next_round_auto(self, l=0, t=0, manual=False):
        '''
        Automatically play game by discard_tile.py 's logic. a basic AI for playing Mahjong.
        '''

        evaluated_hand = discard_tile.evaluate_hand(
            sorted(getattr(self, f'hand_player{self.current_player}')))
        print(evaluated_hand)

        min_score_tile = min(evaluated_hand, key=lambda x: x[1])[0]
        if manual == False:
            self.discard_tile(self.current_player, min_score_tile)
            for i in [self.label1_id, self.label2_id, self.label3_id, self.label4_id]:
                for j in i:
                    self.canvas.delete(j)
        else:

            self.discard_tile(self.current_player, t, manual=True)

            for i in [self.label1_id, self.label2_id, self.label3_id, self.label4_id]:
                for j in i:
                    self.canvas.delete(j)

        self.display_layout()

    def next_round_manual(self, tile):
        '''
        Manually play game by tapping certain tile.
        '''

        self.discard_tile(self.current_player, tile)

        self.draw_tile(self.current_player)

        self.display_layout()

    # TODO: add a color for selected tiles
    def toggle_tile_selection(self, tile, label):
        if self.selected_tiles[tile]:
            self.discard_tile(self.current_player,
                              TileMapping.reverse_mapping[tile])
            label.config(bg='SystemButtonFace')
            self.selected_tiles[tile] = False
        else:
            label.config(bg='yellow')
            self.selected_tiles[tile] = True

    def draw_tile(self, player):
        '''
        2 functionailities:
            1. Draw a tile from the mountain.
            2. Calculate the probability of winning.
        '''

        if player == 1:
            self.hand_player1.append(self.mountain.pop(0))
            self.waiting_message = ''
            self.update_known_tiles()
            if check_win.CheckWin.check_win(self.hand_player1):
                print("Player 1 wins!")
                self.player1_message.config(text="Player 1 Won!")
            elif check_win.CheckWin.find_waiting_tiles(self.hand_player1):
                self.player1_message.config(text="Player 1 Waiting!")
                self.waiting_message = ""
                waiting_tiles = check_win.CheckWin.find_waiting_tiles(
                    self.hand_player1)
                result_tiles = defaultdict(set)
                for i, j in waiting_tiles:
                    result_tiles[i].add(j)
                # got dict type of waiting tiles
                result_tiles = dict(result_tiles)

                for i in result_tiles:
                    tzumo_prob_list = []
                    ron_prob_list = []
                    ron_prob_dict = {}
                    ron_prob_dict2 = {}
                    waiting_list_num = []
                    waiting_list_display = []
                    waiting_tiles_set = []

                    for j in result_tiles[i]:
                        waiting_list_num.append(j)
                        waiting_list_display.append(
                            TileMapping.tile_mapping[j])
                        waiting_tiles_set.append(j)

                    waiting_count = len(waiting_tiles_set) * 4
                    for tile in self.known_tiles:
                        if tile in waiting_tiles_set:
                            waiting_count -= 1

                    left_tiles_count = len(self.mountain)

                    for l in range(0, len(self.mountain), 4):
                        left_tiles_count -= 4
                        normalized_waiting_count = waiting_count * left_tiles_count / \
                            ((13*3) + left_tiles_count + len(self.dead_wall))
                        tzumo_prob_list.append(
                            round(normalized_waiting_count / len(self.mountain), 4))

                    cumulative_prob_tzumo = 0
                    remaining_prob_tzumo = 1
                    for prob in tzumo_prob_list:
                        cumulative_prob_tzumo += remaining_prob_tzumo * prob
                        remaining_prob_tzumo *= (1 - prob)

                    for waiting_tile_ron in waiting_tiles_set:
                        waiting_count_ron = 4

                        for tile in self.known_tiles:
                            if tile in waiting_tiles_set and tile == waiting_tile_ron:
                                waiting_count_ron -= 1
                        left_tiles_count_ron = len(self.mountain)
                        for m in range(0, len(self.mountain), 4):
                            left_tiles_count_ron -= 4
                            normalized_waiting_count = waiting_count_ron * left_tiles_count_ron / \
                                ((13*3) + left_tiles_count + len(self.dead_wall))
                            ron_prob_list.append(
                                round(normalized_waiting_count / len(self.mountain), 4))

                        ron_prob_dict[waiting_tile_ron] = ron_prob_list

                        cumulative_prob_ron = 0
                        remaining_prob_ron = 1

                        ron_prob_list = []

                    all_left_tiles = 136 - len(self.known_tiles)
                    for k in range(0, min(14 + 1, waiting_count + 1)):
                        prob_waiting_tile_ron = comb(
                            waiting_count, k) * comb(all_left_tiles -
                                                     waiting_count, 14 - k) / comb(all_left_tiles, 14)
                        ron_prob_dict2[k] = prob_waiting_tile_ron

                    ron_prob_dict3 = {}
                    ron_prob_dict4 = {}
                    for element in ron_prob_dict2.items():
                        discard_waiting_tile = 0
                        for tile in waiting_tiles_set:
                            if tile in self.river_player2:
                                discard_waiting_tile += 1
                                break
                        for tile in waiting_tiles_set:
                            if tile in self.river_player3:
                                discard_waiting_tile += 1
                                break
                        for tile in waiting_tiles_set:
                            if tile in self.river_player4:
                                discard_waiting_tile += 1
                        ron_prob_dict3[element[0]] = (
                            element[1] * element[0] / 14 * 3)

                        ron_prob_dict4[element[0]] = (element[1] * element[0] / 14 * (3 - discard_waiting_tile) +
                                                      element[1] * discard_waiting_tile) / len(waiting_tiles_set)

                    del ron_prob_dict4[0]

                    ron_prob_total = sum(ron_prob_dict3.values())

                    ron_prob_dict5 = {}
                    ron_prob_dict6 = {}
                    all_left_tiles = 136 - len(self.known_tiles)
                    for k in range(0, min(14 + 1, waiting_count + 1)):
                        prob_waiting_tile_ron = comb(
                            waiting_count, k) * comb(all_left_tiles - waiting_count, 14 - k) / comb(all_left_tiles, 14)
                        ron_prob_dict5[k] = prob_waiting_tile_ron
                    for element in ron_prob_dict5.items():
                        discard_waiting_tile = 0
                        for tile in waiting_tiles_set:
                            if tile in self.river_player2:
                                discard_waiting_tile += 1
                                break
                        for tile in waiting_tiles_set:
                            if tile in self.river_player3:
                                discard_waiting_tile += 1
                                break
                        for tile in waiting_tiles_set:
                            if tile in self.river_player4:
                                discard_waiting_tile += 1
                        ron_prob_dict6[element[0]] = (
                            element[1] * element[0] / 14 * 3)

                    ron_prob_total2 = sum(ron_prob_dict6.values())

                    ron_prob_list2 = [ron_prob_total2] * \
                        (len(self.mountain) // 4)

                    ron_prob_list3 = [1 - (1 - ron_prob_total2) ** (((len(self.mountain) // 4) + 1) - round + 1)
                                      for round in range(1, (len(self.mountain) // 4) + 1)]
                    ron_prob_list3 = ron_prob_list3[1:]
                    ron_prob_list3.append(ron_prob_total2)

                    tzumo_prob_list2 = tzumo_prob_list[:-1]

                    ron_prob_list = [ron_prob_total] * \
                        (len(self.mountain) // 4)

                    final_prob = []
                    if discard_waiting_tile == 0:
                        final_prob = ron_prob_list2
                    elif discard_waiting_tile == 1:
                        final_prob = [tzumo + ron - tzumo * ron for tzumo,
                                      ron in zip(tzumo_prob_list2, ron_prob_list2)]
                    elif discard_waiting_tile == 2:
                        final_prob = [tzumo1 + tzumo2 + ron - tzumo1*tzumo2 - tzumo1*ron - tzumo2*ron + tzumo1 *
                                      tzumo2*ron for tzumo1, tzumo2, ron in zip(tzumo_prob_list2, tzumo_prob_list2, ron_prob_list2)]
                    elif discard_waiting_tile == 3:
                        final_prob = [tzumo1 + tzumo2 + tzumo3 + ron - tzumo1*tzumo2 - tzumo1*tzumo3 - tzumo2*tzumo3 - tzumo1*ron - tzumo2*ron - tzumo3*ron + tzumo1*tzumo2*ron + tzumo1 *
                                      tzumo3*ron + tzumo2*tzumo3*ron - tzumo1*tzumo2*tzumo3*ron for tzumo1, tzumo2, tzumo3, ron in zip(tzumo_prob_list2, tzumo_prob_list2, tzumo_prob_list2, ron_prob_list2)]

                    cumulative_prob_ron = 0
                    remaining_prob_ron = 1
                    for prob in ron_prob_list:
                        cumulative_prob_ron += remaining_prob_ron * prob
                        remaining_prob_ron *= (1 - prob)

                    cumulative_prob_ron2 = 0
                    remaining_prob_ron2 = 1
                    for prob in final_prob:
                        cumulative_prob_ron2 += remaining_prob_ron2 * prob
                        remaining_prob_ron2 *= (1 - prob)

                    tzumo_prob = cumulative_prob_tzumo * 100
                    ron_prob = cumulative_prob_ron * 100
                    ron_prob2 = cumulative_prob_ron2 * 100

                    self.waiting_message += f"discard {TileMapping.tile_mapping[i]} to wait for {waiting_list_display}, {waiting_count} left, P(Tzumo): {round(tzumo_prob, 2)}% P(Ron): {round(ron_prob, 2)}% P(Ron_Plus):{round(ron_prob2, 2)}%\n"

                    print(self.waiting_message)

        elif player == 2:
            self.hand_player2.append(self.mountain.pop(0))
            if check_win.CheckWin.check_win(self.hand_player2):
                self.player2_message.config(text="Ron!")
            if check_win.CheckWin.find_waiting_tiles(self.hand_player2):
                self.player2_message.config(text="Waiting!")

        elif player == 3:
            self.hand_player3.append(self.mountain.pop(0))
            if check_win.CheckWin.check_win(self.hand_player3):
                self.player3_message.config(text="Player 3 Ron!")
            if check_win.CheckWin.find_waiting_tiles(self.hand_player3):
                self.player3_message.config(text="Waiting!")

        elif player == 4:
            self.hand_player4.append(self.mountain.pop(0))
            if check_win.CheckWin.check_win(self.hand_player4):
                self.player4_message.config(text="Player 4 Ron!")
            if check_win.CheckWin.find_waiting_tiles(self.hand_player4):
                self.player4_message.config(text="Waiting!")
        else:
            print("Player number is invalid!")

    def discard_tile(self, player, tile, manual=False):
        if player == 1:
            if manual == False:
                self.hand_player1.remove(tile)
                self.river_player1.append(tile)
            else:
                # tile_index = self.hand_player1.index(
                #     TileMapping.reverse_mapping[tile])
                tile_index = self.hand_player1.index(tile)
                print(self.hand_player1)
                print(self.river_player1)
                tile = self.hand_player1.pop(tile_index)
                self.river_player1.append(tile)
                print(self.hand_player1)
                print(self.river_player1)

        elif player == 2:
            self.hand_player2.remove(tile)
            self.river_player2.append(tile)

        elif player == 3:
            self.hand_player3.remove(tile)
            self.river_player3.append(tile)

        elif player == 4:
            self.hand_player4.remove(tile)
            self.river_player4.append(tile)

        else:
            print("Player number is invalid!")
        self.current_player = (self.current_player % 4) + 1
        self.draw_tile(self.current_player)

    def update_known_tiles(self):
        self.known_tiles = (self.hand_player1 + self.river_player1 + self.river_player2 +
                            self.river_player3 + self.river_player4)


def main():
    game = Game()
    game.start_game(way='1')
    # print(game.round)
    # print(len(game.hand_player1))
    # print(game.hand_player2)
    # print(game.hand_player3)
    # print(game.hand_player4)

    game.display_layout()
    game.root.mainloop()


if __name__ == "__main__":
    main()
