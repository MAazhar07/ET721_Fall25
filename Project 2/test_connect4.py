# Mohammed Azhar - Part 2: Unit Tests for Connect4
import unittest
from main import Connect4


class TestConnect4(unittest.TestCase):

    def setUp(self):
        """Create a new game before each test."""
        self.game = Connect4()

    # Win Condition Tests
    def test_horizontal_win(self):
        """Test horizontal win detection."""
        for col in range(1, 5):
            self.game.board[5][col - 1] = "X"
        self.assertTrue(self.game.check_win("X"))

    def test_vertical_win(self):
        """Test vertical win detection."""
        for row in range(3, -1, -1):
            self.game.board[row][0] = "O"
        self.assertTrue(self.game.check_win("O"))

    def test_diagonal_down_right_win(self):
        """Test diagonal (top-left to bottom-right) win detection."""
        for i in range(4):
            self.game.board[i][i] = "X"
        self.assertTrue(self.game.check_win("X"))

    def test_diagonal_up_right_win(self):
        """Test diagonal (bottom-left to top-right) win detection."""
        for i in range(4):
            self.game.board[5 - i][i] = "O"
        self.assertTrue(self.game.check_win("O"))

    def test_no_win(self):
        """Test no win condition."""
        self.game.drop_chip(1)
        self.game.drop_chip(2)
        self.assertFalse(self.game.check_win("X"))
        self.assertFalse(self.game.check_win("O"))

    # Chip Dropping Tests
    def test_successful_chip_drop(self):
        """Test dropping a chip successfully."""
        result = self.game.drop_chip(3)
        self.assertTrue(result)
        self.assertEqual(self.game.board[5][2], "X")

    def test_full_column(self):
        """Test dropping into a full column."""
        col = 1
        for _ in range(self.game.ROWS):
            self.game.drop_chip(col)
        result = self.game.drop_chip(col)
        self.assertFalse(result)

    def test_invalid_column(self):
        """Test invalid column input."""
        self.assertFalse(self.game.drop_chip(0))
        self.assertFalse(self.game.drop_chip(8))

    def test_full_board(self):
        """Test that board is detected as full."""
        for col in range(1, self.game.COLS + 1):
            for _ in range(self.game.ROWS):
                self.game.drop_chip(col)
        self.assertTrue(self.game.is_full())

    # Switch Player Test
    def test_switch_player(self):
        """Test player switching logic."""
        self.assertEqual(self.game.current_player, "X")
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "O")
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "X")


if __name__ == "__main__":
    unittest.main()


"""

Summary of Tests:
All of the unit tests ran successfully. The win condition tests correctly identified horizontal,
vertical, and both diagonal victories. The 'no win' test confirmed that the game continues
when there’s no winning combination on the board.

The chip dropping logic also worked as expected. Chips were placed correctly in available
columns, the game properly handled attempts to drop chips in full or invalid columns, and the
board correctly reported as full once all spaces were filled.

The switch_player test confirmed that the player alternates correctly between 'X' and 'O'
after each turn.

Overall, all tests passed without any issues. The game logic appears to be functioning
correctly, and no bugs were found during testing.
"""
