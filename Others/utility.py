from math import comb


class Utility:
    def move_cursor(row, col):
        print(f"\033[{row};{col}H", end='')

    def clear_screen():
        print("\033[2J")

    def place_text(row, col, text):
        move_cursor(row, col)
        print(text, end='')

    @staticmethod
    def get_tile_prob():
        total_cards = 136
        tiles_of_interest = 4
        drawn_cards = 14

        probabilities = {}
        for k in range(tiles_of_interest + 1):
            prob = comb(tiles_of_interest, k) * comb(total_cards - tiles_of_interest, drawn_cards - k) / comb(total_cards, drawn_cards)
            probabilities[k] = prob

        return probabilities


if __name__ == '__main__':
    print(comb(14, 4))