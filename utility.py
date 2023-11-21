class Utility:
    def move_cursor(row, col):
        print(f"\033[{row};{col}H", end='')

    def clear_screen():
        print("\033[2J")

    def place_text(row, col, text):
        move_cursor(row, col)
        print(text, end='')