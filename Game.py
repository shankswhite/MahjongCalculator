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


    def draw_tile(self):

        self.round += 1
        pass
        


def main():
    game = Game()
    game.start_game()
    



if __name__ == "__main__":
    main()