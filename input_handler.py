import re


class InputHandler:
    @staticmethod
    def input_handler(cards):
        m = list(map(int, ''.join(re.findall(r'\d+(?=m)', cards))))
        p = list(map(str, ''.join(re.findall(r'\d+(?=p)', cards))))
        for i in range(len(p)):
            p[i] = int('2' + p[i])
        s = list(map(str, ''.join(re.findall(r'\d+(?=s)', cards))))
        for i in range(len(s)):
            s[i] = int('4' + s[i])
        z = list(map(str, ''.join(re.findall(r'\d+(?=z)', cards))))
        for i in range(len(z)):
            z[i] = int('2' + z[i]) * 3
        return m + p + s + z



# tiles = InputHandler.input_handler('1336p243m2p4578p77z')
# print(tiles)

