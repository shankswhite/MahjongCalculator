class InputHandler:
    @staticmethod
    def input_handler(hand_string):
        hand_dict = {'m': [], 's': [], 'p': [], 'z': []}
        current_type = ''
        for i in range(0, len(hand_string)):
            if hand_string[i] in hand_dict:
                current_type = hand_string[i]
            else:
                hand_dict[current_type].append(int(hand_string[i]))
                
        return hand_dict


tiles = InputHandler.input_handler("m123456s123p123z55")
print(tiles)




