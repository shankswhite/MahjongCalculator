import unittest
import game
import input_handler


class TestGame(unittest.TestCase):
    def test_game(self):
        ''' TEST 1: different way to start game
        '''

        test = game.Game()
        test.start_game(way = '1')
        self.assertNotEqual(test.hand_player1, input_handler.InputHandler.input_handler(
                "4566777m234s666p"))
        self.assertEqual(test.hand_player2, input_handler.InputHandler.input_handler(
                "123456789m123s1z"))

        # next_round_check
        test.next_round_auto()
        self.assertEqual(test.hand_player1, input_handler.InputHandler.input_handler(
                "4566777m234s666p"))


def main():
    unittest.main()


if __name__ == '__main__':
    unittest.main()
