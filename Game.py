import random


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
        z_tiles = [i for i in range(61, 70) for _ in range(4)]
        
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
        return f"Round: {self.round}\n{mountain_str}\n{player1_hand}\n{player2_hand}\n{player3_hand}\n{player4_hand}"



def main():
    game = Game()
    game.start_game()
    print(game.round)
    print(len(game.hand_player1))
    print(game.hand_player2)
    print(game.hand_player3)
    print(game.hand_player4)
    print(game)





if __name__ == "__main__":
    main()
    tile_symbols = {
    1: "🀇",  # 一万
    2: "🀈",  # 二万
    3: "🀉",  # 三万
    4: "🀊",  # 四万
    5: "🀋",  # 五万
    6: "🀌",  # 六万
    7: "🀍",  # 七万
    8: "🀎",  # 八万
    9: "🀏",  # 九万
    }
    # 示例列表
    tiles_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 转换整数列表到符号并打印
    tiles_symbols = [tile_symbols[tile] for tile in tiles_int]
    print(" ".join(tiles_symbols))

