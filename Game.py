import random
from tile_mapping import TileMapping
from utility import Utility
import tkinter as tk


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

    def start_game(self):

        m_tiles = [i for i in range(1, 10) for _ in range(4)]
        p_tiles = [i for i in range(21, 30) for _ in range(4)]
        s_tiles = [i for i in range(41, 50) for _ in range(4)]
        z_tiles = [i for i in range(61, 68) for _ in range(4)]
        
        tiles = m_tiles + p_tiles + s_tiles + z_tiles
        random.shuffle(tiles)

        self.round = 0
        self.mountain = tiles[:70]  # First 70 tiles for the wall
        self.dead_wall = tiles[70:84]  # Next 4 tiles for dora indicators
        self.hand_player1 = tiles[84:97]
        self.hand_player2 = tiles[97:110]
        self.hand_player3 = tiles[110:123]
        self.hand_player4 = tiles[123:136]

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

        hand_player1_display = ''.join(TileMapping.tile_mapping[tile] for tile in hand_player1_sorted)
        hand_player2_display = ''.join(TileMapping.tile_mapping[tile] for tile in hand_player2_sorted)
        hand_player3_display = ''.join(TileMapping.tile_mapping[tile] for tile in hand_player3_sorted)
        hand_player4_display = ''.join(TileMapping.tile_mapping[tile] for tile in hand_player4_sorted)

        river_player1_display = ''.join(TileMapping.tile_mapping[tile] for tile in self.river_player1)
        river_player2_display = ''.join(TileMapping.tile_mapping[tile] for tile in self.river_player2)
        river_player3_display = ''.join(TileMapping.tile_mapping[tile] for tile in self.river_player3)
        river_player4_display = ''.join(TileMapping.tile_mapping[tile] for tile in self.river_player4)


        root = tk.Tk()
        root.title("Mahjong Layout")
        root.geometry('1200x800')

        canvas = tk.Canvas(root, width=800, height=600)
        canvas.pack()

        for i, tile in enumerate(hand_player1_display):
            label = tk.Label(root, text=tile, font=('Arial Unicode MS', 24))
            canvas.create_window(200 + i*35, 600, window=label)

        for i, tile in enumerate(hand_player2_display):
            label = tk.Label(root, text=tile, font=('Arial Unicode MS', 24))
            canvas.create_window(750, 150 + i*35, window=label)

        for i, tile in enumerate(hand_player3_display):
            label = tk.Label(root, text=tile, font=('Arial Unicode MS', 24))
            canvas.create_window(600 - i*35, 50, window=label)

        for i, tile in enumerate(hand_player4_display):
            label = tk.Label(root, text=tile, font=('Arial Unicode MS', 24))
            canvas.create_window(50, 550 - i*35, window=label)


        for i, tile in enumerate(hand_player1_display):
            label = tk.Label(root, text=tile, font=('Arial Unicode MS', 24))
            if i >= 12:
                canvas.create_window(350 + (i-12)*20, 520, window=label)
            elif i >= 6:
                canvas.create_window(350 + (i-6)*20, 485, window=label)
            else:
                canvas.create_window(350 + i*20, 450, window=label)

        for i, tile in enumerate(hand_player2_display):
            label = tk.Label(root, text=tile, font=('Arial Unicode MS', 24))
            if i >= 12:
                canvas.create_window(550, 240 + (i-12)*35, window=label)
            elif i >= 6:
                canvas.create_window(515, 240 + (i-6)*35, window=label)
            else:
                canvas.create_window(480, 240 + i*35, window=label)

        for i, tile in enumerate(hand_player3_display):
            label = tk.Label(root, text=tile, font=('Arial Unicode MS', 24))
            if i >= 12:
                canvas.create_window(245, 240 + (i-12)*35, window=label)
            elif i >= 6:
                canvas.create_window(280, 240 + (i-6)*35, window=label)
            else:
                canvas.create_window(315, 240 + i*35, window=label)

        for i, tile in enumerate(hand_player4_display):
            label = tk.Label(root, text=tile, font=('Arial Unicode MS', 24))
            if i >= 12:
                canvas.create_window(450 - (i-12)*20, 130, window=label)
            elif i >= 6:
                canvas.create_window(450 - (i-6)*20, 165, window=label)
            else:
                canvas.create_window(450 - i*20, 200, window=label)


        root.mainloop()

        



def main():
    game = Game()
    game.start_game()
    # print(game.round)
    # print(len(game.hand_player1))
    # print(game.hand_player2)
    # print(game.hand_player3)
    # print(game.hand_player4)
    game.display_layout()
    





if __name__ == "__main__":
    main()

    

