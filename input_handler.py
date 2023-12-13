import re
import tkinter as tk
from tkinter import messagebox


class InputHandler:
    @staticmethod
    def input_handler(tiles, is_hand=True):
        if tiles == '':
            raise ValueError('Empty input')
        temp_list = []
        for i in tiles:
            if i.isdigit():
                temp_list.append(i)
        print(temp_list, tiles)
        if len(temp_list) != 13 and is_hand == True:
            raise ValueError('Invalid input, should be 13 tiles')

        m = list(map(int, ''.join(re.findall(r'\d+(?=m)', tiles))))
        p = list(map(str, ''.join(re.findall(r'\d+(?=p)', tiles))))
        for i in range(len(p)):
            p[i] = int('2' + p[i])
        s = list(map(str, ''.join(re.findall(r'\d+(?=s)', tiles))))
        for i in range(len(s)):
            s[i] = int('4' + s[i])
        z = list(map(str, ''.join(re.findall(r'\d+(?=z)', tiles))))
        for i in range(len(z)):
            z[i] = int('2' + z[i]) * 3
        return m + p + s + z
