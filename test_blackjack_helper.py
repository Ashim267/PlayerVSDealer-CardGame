from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.
  def test_print_card_name(self) :
    self.assertEqual(get_print(print_card_name,1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name,9), "Drew a 9\n")
    self.assertEqual(get_print(print_card_name,22), "BAD CARD\n")

  def test_draw_card(self) :
    self.assertEqual(mock_random([4],draw_card), 4)
    self.assertEqual(mock_random([1],draw_card), 11)
    self.assertEqual(mock_random([11],draw_card), 10)

  def test_print_header(self) :
    self.assertEqual(get_print(print_header,'ram'), '-----------\nram\n-----------\n')
    self.assertEqual(get_print(print_header,''), '-----------\n''\n-----------\n')
    self.assertEqual(get_print(print_header,'USER'), '-----------\nUSER\n-----------\n')

  def test_draw_starting_hand(self) :
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8) 
    self.assertEqual(mock_random([1, 11], draw_starting_hand, "USER"), 21)  
    self.assertEqual(mock_random([1, 5], draw_starting_hand, "DEALER"), 16)  

  def test_print_end_turn_status(self) :
    self.assertEqual(get_print(print_end_turn_status,21), 'Final hand: 21.\nBLACKJACK!\n')
    self.assertEqual(get_print(print_end_turn_status,23), 'Final hand: 23.\nBUST.\n')
    self.assertEqual(get_print(print_end_turn_status,10), 'Final hand: 10.\n')
  
  def test_print_end_game_status(self) :
    self.assertEqual(get_print(print_end_game_status,18,17), '-----------\nGAME RESULT\n-----------\nYou win!\n')
    self.assertEqual(get_print(print_end_game_status,17,18), '-----------\nGAME RESULT\n-----------\nDealer wins!\n')
    self.assertEqual(get_print(print_end_game_status,23,21), '-----------\nGAME RESULT\n-----------\nDealer wins!\n')
    self.assertEqual(get_print(print_end_game_status,21,21), '-----------\nGAME RESULT\n-----------\nPush.\n')

if __name__ == '__main__':
    unittest.main()
