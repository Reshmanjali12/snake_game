import unittest
from unittest.mock import MagicMock
import sys

# Mocking turtle for headless Jenkins environments
sys.modules["turtle"] = MagicMock()

from Snake import Snake  # Import after mocking

class TestSnake(unittest.TestCase):

    def setUp(self):
        """Setup a fresh snake instance before each test."""
        self.snake = Snake()

    def test_initial_snake_length(self):
        """Test if the snake starts with 3 segments."""
        self.assertEqual(len(self.snake.segments), 3)

    def test_snake_grows(self):
        """Test if snake extends when growing."""
        initial_length = len(self.snake.segments)
        self.snake.extend()
        self.assertEqual(len(self.snake.segments), initial_length + 1)

    def test_snake_resets(self):
        """Test if the snake resets properly after collision."""
        self.snake.extend()
        self.snake.reset()
        self.assertEqual(len(self.snake.segments), 3)

if __name__ == "__main__":
    unittest.main()
