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


# player1_hand = ['🀇', '🀈', '🀉']
# player2_hand = ['🀙', '🀚', '🀛']
# player3_hand = ['🀐', '🀑', '🀒']
# player4_hand = ['🀀', '🀁', '🀂']

# # 反转字符串表示的函数
# def reverse_string(s):
#     return s[::-1]

# # 玩家上家的牌（竖着）
# player4_vertical = '\n'.join(player4_hand)
# # 玩家下家的牌（竖着）
# player2_vertical = '\n'.join(player2_hand)

# # 使用多行f-string来格式化输出
# mahjong_layout = f"""
#     {reverse_string('  '.join(player3_hand))}
    
# {player4_vertical}             {player2_vertical}

#     {'  '.join(player1_hand)}
# """

# print(mahjong_layout)


import tkinter as tk

# 初始化Tkinter窗口
root = tk.Tk()
root.title("麻将手牌布局")

# 设置窗口的大小
root.geometry('800x600')

# 创建Canvas来绘制手牌
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# 定义手牌的表示
player1_hand = ['🀇', '🀈', '🀉']
player2_hand = ['🀙', '🀚', '🀛']
player3_hand = ['🀐', '🀑', '🀒']
player4_hand = ['🀀', '🀁', '🀂']

# 为每个玩家创建一个标签和布局
# 自家手牌
for i, tile in enumerate(player1_hand):
    label = tk.Label(root, text=tile, font=('Arial Unicode MS', 24))
    canvas.create_window(200 + i*50, 550, window=label)

# 下家手牌
for i, tile in enumerate(player2_hand):
    label = tk.Label(root, text=tile, font=('Arial Unicode MS', 24))
    canvas.create_window(750, 200 + i*50, window=label)

# 对家手牌
for i, tile in enumerate(player3_hand):
    label = tk.Label(root, text=tile, font=('Arial Unicode MS', 24))
    canvas.create_window(600 - i*50, 50, window=label)

# 上家手牌
for i, tile in enumerate(player4_hand):
    label = tk.Label(root, text=tile, font=('Arial Unicode MS', 24))
    canvas.create_window(50, 400 - i*50, window=label)

# 运行Tkinter事件循环
root.mainloop()