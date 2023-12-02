import random
from tile_mapping import TileMapping
from utility import Utility
import tkinter as tk
import input_handler
import check_win
import discard_tile
from collections import Counter, defaultdict



class Game:
    def __init__(self):
        self.river_whole = []
        self.river_player1 = []
        self.river_player2 = []
        self.river_player3 = []
        self.river_player4 = []

        self.hand_player1 = []
        self.hand_player2 = []
        self.hand_player3 = []
        self.hand_player4 = []

        self.mountain = []
        self.dead_wall = []

        self.round = 0 # 1-70 round
        self.current_player = 1
    
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

        self.player1_message = tk.Label(self.root, text="", font=('Arial Unicode MS', 24))
        self.player2_message = tk.Label(self.root, text="", font=('Arial Unicode MS', 24))
        self.player3_message = tk.Label(self.root, text="", font=('Arial Unicode MS', 24))
        self.player4_message = tk.Label(self.root, text="", font=('Arial Unicode MS', 24))

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

        self.hand_list = [self.hand1, self.hand2, self.hand3, self.hand4, self.hand5, self.hand6, self.hand7, self.hand8, self.hand9, self.hand10, self.hand11, self.hand12, self.hand13, self.hand14]

        self.waiting_message = ''

        self.known_tiles = []

        
        

    
        


    def start_game(self, way="random"):

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
            self.hand_player1 = input_handler.InputHandler.input_handler("123456789m123s1z")
            self.hand_player2 = input_handler.InputHandler.input_handler("123456789m123s1z")
            self.hand_player3 = input_handler.InputHandler.input_handler("123456789m123s1z")
            self.hand_player4 = input_handler.InputHandler.input_handler("123456789m123s1z")
            self.mountain = input_handler.InputHandler.input_handler("123456789m123s1z123456789m123s1z123456789m123s1z123456789m123s1z")
            self.dead_wall = input_handler.InputHandler.input_handler("123456789m123s1z")
        elif way == "test":
            self.hand_player1 = self.get_player1_hand
            self.hand_player2 = self.get_player2_hand
            self.hand_player3 = self.get_player3_hand
            self.hand_player4 = self.get_player4_hand
            self.mountain = self.get_mountain
            self.dead_wall = self.get_dead_wall

            temp_list_filled = []
            temp_list_unfilled = []
            for i in [self.hand_player1, self.hand_player2, self.hand_player3, self.hand_player4, self.mountain, self.dead_wall]:
                if len(i) != 0:
                    temp_list_filled.append(i)
    
            removal_counter = Counter(item for sublist in temp_list_filled for item in sublist)

            new_list = []
            for item in tiles:
                if removal_counter[item] > 0:
                    removal_counter[item] -= 1
                else:
                    new_list.append(item)
            
            # print(new_list)
            
            if len(self.hand_player1) == 0:
                self.hand_player1 = new_list[:14]
                new_list = new_list[14:]
            if len(self.hand_player2) == 0:
                # print(new_list)
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
        mountain_str = "Mountain: " + ' '.join(str(tile) for tile in self.mountain)
        player1_hand = "Player 1: " + ' '.join(str(tile) for tile in self.hand_player1)
        player2_hand = "Player 2: " + ' '.join(str(tile) for tile in self.hand_player2)
        player3_hand = "Player 3: " + ' '.join(str(tile) for tile in self.hand_player3)
        player4_hand = "Player 4: " + ' '.join(str(tile) for tile in self.hand_player4)
        player1_river = "Player 1: " + ' '.join(str(tile) for tile in self.river_player1)
        player2_river = "Player 2: " + ' '.join(str(tile) for tile in self.river_player2)
        player3_river = "Player 3: " + ' '.join(str(tile) for tile in self.river_player3)
        player4_river = "Player 4: " + ' '.join(str(tile) for tile in self.river_player4)


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
        hand_player1_sorted = sorted(self.hand_player1)
        hand_player2_sorted = sorted(self.hand_player2)
        hand_player3_sorted = sorted(self.hand_player3)
        hand_player4_sorted = sorted(self.hand_player4)
        # print(hand_player1_sorted)

        hand_player1_display = ''.join(TileMapping.tile_mapping[tile] for tile in hand_player1_sorted)
        hand_player2_display = ''.join(TileMapping.tile_mapping[tile] for tile in hand_player2_sorted)
        hand_player3_display = ''.join(TileMapping.tile_mapping[tile] for tile in hand_player3_sorted)
        hand_player4_display = ''.join(TileMapping.tile_mapping[tile] for tile in hand_player4_sorted)

        river_player1_display = ''.join(TileMapping.tile_mapping[tile] for tile in self.river_player1)
        river_player2_display = ''.join(TileMapping.tile_mapping[tile] for tile in self.river_player2)
        river_player3_display = ''.join(TileMapping.tile_mapping[tile] for tile in self.river_player3)
        river_player4_display = ''.join(TileMapping.tile_mapping[tile] for tile in self.river_player4)



        for i, tile in enumerate(hand_player1_display):
            label = tk.Label(self.root, text=tile, font=('Arial Unicode MS', 24))
            label.bind('<Button-1>', lambda event, t=tile, l=label: self.next_round_auto(l, t, manual=True))

            self.label1_id.append(self.canvas.create_window(300 + i*35, 600, window=label))
            self.selected_tiles[tile] = False

        for i, value in enumerate(self.hand_list):
            label = tk.Label(self.root, text=value, font=('Arial Unicode MS', 15))
            self.canvas.create_window(300 + i*35, 650, window=label)

        for i, tile in enumerate(hand_player2_display):
            label = tk.Label(self.root, text=tile, font=('Arial Unicode MS', 24))
            self.label2_id.append(self.canvas.create_window(850, 150 + i*36, window=label))

        for i, tile in enumerate(hand_player3_display):
            label = tk.Label(self.root, text=tile, font=('Arial Unicode MS', 24))
            self.label3_id.append(self.canvas.create_window(700 - i*35, 50, window=label))

        for i, tile in enumerate(hand_player4_display):
            label = tk.Label(self.root, text=tile, font=('Arial Unicode MS', 24))
            self.label4_id.append(self.canvas.create_window(150, 550 - i*35, window=label))


        for i, tile in enumerate(river_player1_display):
            label = tk.Label(self.root, text=tile, font=('Arial Unicode MS', 24))
            if i >= 12:
                self.canvas.create_window(450 + (i-12)*21, 520, window=label)
            elif i >= 6:
                self.canvas.create_window(450 + (i-6)*21, 485, window=label)
            else:
                self.canvas.create_window(450 + i*21, 450, window=label)

        for i, tile in enumerate(river_player2_display):
            label = tk.Label(self.root, text=tile, font=('Arial Unicode MS', 24))
            if i >= 12:
                self.canvas.create_window(650, 240 + (i-12)*35, window=label)
            elif i >= 6:
                self.canvas.create_window(615, 240 + (i-6)*35, window=label)
            else:
                self.canvas.create_window(580, 240 + i*35, window=label)

        for i, tile in enumerate(river_player4_display):
            label = tk.Label(self.root, text=tile, font=('Arial Unicode MS', 24))
            if i >= 12:
                self.canvas.create_window(345, 240 + (i-12)*35, window=label)
            elif i >= 6:
                self.canvas.create_window(380, 240 + (i-6)*35, window=label)
            else:
                self.canvas.create_window(415, 240 + i*35, window=label)

        for i, tile in enumerate(river_player3_display):
            label = tk.Label(self.root, text=tile, font=('Arial Unicode MS', 24))
            if i >= 12:
                self.canvas.create_window(550 - (i-12)*21, 130, window=label)
            elif i >= 6:
                self.canvas.create_window(550 - (i-6)*21, 165, window=label)
            else:
                self.canvas.create_window(550 - i*21, 200, window=label)
        
        self.next_round_auto_button = tk.Button(self.root, text="Next   Round   Auto", command=self.next_round_auto)
        self.canvas.create_window(1000, 200, window=self.next_round_auto_button)

        def get_input():
            self.get_player1_hand = input_handler.InputHandler.input_handler(entry1.get())  # Get the text from the entry
            self.get_player2_hand = input_handler.InputHandler.input_handler(entry2.get())  # Get the text from the entry
            self.get_player3_hand = input_handler.InputHandler.input_handler(entry3.get())  # Get the text from the entry
            self.get_player4_hand = input_handler.InputHandler.input_handler(entry4.get())  # Get the text from the entry
            self.get_mountain = input_handler.InputHandler.input_handler(entry5.get())  # Get the text from the entry
            self.get_dead_wall = input_handler.InputHandler.input_handler(entry6.get())  # Get the text from the entry
            

            # self.hand_player1 = get_player1_hand
            # self.hand_player2 = get_player2_hand
            # self.hand_player3 = get_player3_hand
            # self.hand_player4 = get_player4_hand
            # self.mountain = get_mountain
            # self.dead_wall = get_dead_wall
            Game.start_game(self, way="test")
            # for i in [self.hand_player1, self.hand_player2, self.hand_player3, self.hand_player4, self.mountain, self.dead_wall]:
            #     if len(i) == 0:
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

        # entry_discard = tk.Entry(self.root, width=20)

        self.canvas.create_window(1000, 400, window=entry1)
        self.canvas.create_window(1000, 450, window=entry2)
        self.canvas.create_window(1000, 500, window=entry3) 
        self.canvas.create_window(1000, 550, window=entry4)
        self.canvas.create_window(1000, 600, window=entry5)
        self.canvas.create_window(1000, 650, window=entry6)
        label = tk.Label(self.root, text="player1", font=('Arial Unicode MS', 18))
        self.canvas.create_window(1150, 400, window=label)
        label = tk.Label(self.root, text="player2", font=('Arial Unicode MS', 18))
        self.canvas.create_window(1150, 450, window=label)
        label = tk.Label(self.root, text="player3", font=('Arial Unicode MS', 18))
        self.canvas.create_window(1150, 500, window=label) 
        label = tk.Label(self.root, text="player4", font=('Arial Unicode MS', 18))
        self.canvas.create_window(1150, 550, window=label)
        label = tk.Label(self.root, text="mountain", font=('Arial Unicode MS', 18))
        self.canvas.create_window(1150, 600, window=label)
        label = tk.Label(self.root, text="wall", font=('Arial Unicode MS', 18))
        self.canvas.create_window(1150, 650, window=label)




        # self.canvas.create_window(1000, 250, window=entry_discard)
        # Create a button to trigger the input retrieval
        update_button = tk.Button(self.root, text='Set Table', command=get_input)
        self.canvas.create_window(1050, 700, window=update_button)

        waiting_message = tk.Label(self.root, text=self.waiting_message, font=('Arial Unicode MS', 24), anchor='w')
        self.canvas.create_window(400, 800, window=waiting_message)


        # print(self.label1_id)




    def next_round_auto(self, l=0, t=0, manual=False):

        evaluated_hand = discard_tile.evaluate_hand(sorted(getattr(self, f'hand_player{self.current_player}')))
        
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
        


  

        # print(self.tile_labels)

        self.display_layout()

    def next_round_manual(self, tile):

        self.discard_tile(self.current_player, tile)

        self.draw_tile(self.current_player)

        self.display_layout()

    def toggle_tile_selection(self, tile, label):
        if self.selected_tiles[tile]:  # If the tile is already selected
            # Proceed to discard the tile
            self.discard_tile(self.current_player, TileMapping.reverse_mapping[tile])
            label.config(bg='SystemButtonFace')  # Reset the background color
            self.selected_tiles[tile] = False  # Reset the selection state
        else:
            # Select the tile
            label.config(bg='yellow')  # Change the background color to yellow
            self.selected_tiles[tile] = True  # Set the selection state to True
                
    def draw_tile(self, player):
        if player == 1:
            self.hand_player1.append(self.mountain.pop(0))
            self.waiting_message = ''
            self.update_known_tiles()
            if check_win.CheckWin.check_win(self.hand_player1):
                print("Player 1 wins!")
                self.player1_message.config(text="Player 1 Ron!")
            elif check_win.CheckWin.find_waiting_tiles(self.hand_player1):
                self.player1_message.config(text="Player 1 Waiting!")
                self.waiting_message = ""
                waiting_tiles = check_win.CheckWin.find_waiting_tiles(self.hand_player1)
                result_tiles = defaultdict(set)
                for i, j in waiting_tiles:
                    result_tiles[i].add(j)
                result_tiles = dict(result_tiles) # got dict type of waiting tiles
                
                for i in result_tiles:
                    tzumo_prob_list = []
                    waiting_list_num = []
                    waiting_list_display = []
                    waiting_tiles_set = []
  
                    for j in result_tiles[i]:
                        waiting_list_num.append(j)
                        waiting_list_display.append(TileMapping.tile_mapping[j])
                        waiting_tiles_set.append(j)

                    waiting_count = len(waiting_tiles_set) * 4
                    # print(waiting_tiles_set)
                    # print(self.known_tiles)
                    for k in self.known_tiles:
                        if k in waiting_tiles_set:
                            waiting_count -= 1
                    print(i)
                    print(waiting_tiles_set)
                    print(self.known_tiles)
                    left_tiles_count = len(self.mountain)

                    for l in range(0, len(self.mountain), 4):
                        left_tiles_count -= 4
                        normalized_waiting_count = waiting_count * left_tiles_count / ((13*3) + left_tiles_count + len(self.dead_wall))
                        tzumo_prob_list.append(round(normalized_waiting_count / len(self.mountain), 4))
                        print(tzumo_prob_list)
                    # normalized_waiting_count = waiting_count * len(self.mountain) / ((13*3) + len(self.mountain) + len(self.dead_wall))
                    cumulative_prob = 0  # Initialize the cumulative probability
                    remaining_prob = 1  # Start with a 100% remaining probability

                    for prob in tzumo_prob_list:
                        prob_decimal = prob  # Convert percentage to decimal
                        cumulative_prob += remaining_prob * prob_decimal  # Add the probability of winning this round
                        remaining_prob *= (1 - prob_decimal)  # Update the remaining probability


                    tzumo_prob = cumulative_prob * 100
                    self.waiting_message += f"discard {TileMapping.tile_mapping[i]} to wait for {waiting_list_display}, {waiting_count} left, P(Tzumo): {round(tzumo_prob, 2)}% P(Ron): 15%\n"
        
                
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
                tile_index = self.hand_player1.index(TileMapping.reverse_mapping[tile])
                print(self.hand_player1)
                print(self.river_player1)
                tile = self.hand_player1.pop(tile_index)
                self.river_player1.append(tile)
                print(self.hand_player1)
                print(self.river_player1)

        
                # for i in [self.label1_id, self.label2_id, self.label3_id, self.label4_id]:
                #     for j in i:
                #         self.canvas.delete(j)
                # self.display_layout()


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
    game.start_game(way="1")
    # print(game.round)
    # print(len(game.hand_player1))
    # print(game.hand_player2)
    # print(game.hand_player3)
    # print(game.hand_player4)

    game.display_layout()
    game.root.mainloop()


if __name__ == "__main__":
    main()

    

