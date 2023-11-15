class InputHandler:
    @staticmethod
    def input_handler(hand_string, is_tsumo=False, is_riichi=False, is_menqing=False, is_zimo=False, 
                      is_lingshang=False, is_haidi=False, is_hedi=False, is_qianggang=False):
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

