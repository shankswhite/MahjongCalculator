def draw_tile(self):
        # Draw a tile from the mountain
        tile = self.mountain.pop()
        if self.current_player == 1:
            self.hand_player1.append(tile)
        elif self.current_player == 2:
            self.hand_player2.append(tile)
        elif self.current_player == 3:
            self.hand_player3.append(tile)
        elif self.current_player == 4:
            self.hand_player4.append(tile)

    def discard_tile(self, tile):
        # Check if the player has the tile in their hand
        if tile not in getattr(self, f'hand_player{self.current_player}'):
            raise ValueError("Player does not have the specified tile to discard.")
        # Remove the tile from the player's hand and add it to the river
        getattr(self, f'hand_player{self.current_player}').remove(tile)
        getattr(self, f'river_player{self.current_player}').append(tile)

    def move_to_next_round(self):
        
        
        self.current_player = (self.current_player % 4) + 1  # Rotate to the next player

        self.round += 1
        if self.round <= 70:
            self.draw_tile()