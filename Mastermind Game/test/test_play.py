import unittest
from src.master_mind import Colors, Match, GameStatus, play

EXACT = Match.EXACT
PRESENT = Match.PRESENT
NO_MATCH = Match.NO_MATCH

WON = GameStatus.WON
IN_PROGRESS = GameStatus.IN_PROGRESS
LOST = GameStatus.LOST

class Test_play(unittest.TestCase): 
  def test_play_1st_attempt_with_exact_match(self):
    selected_colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.BLUE, Colors.PURPLE]
    user_provided_colors = selected_colors
    
    response = play(selected_colors, user_provided_colors, number_of_attempts = 1) 
   
    self.assertEqual(response, ({EXACT: 6, PRESENT: 0, NO_MATCH: 0}, 2, WON)) 
  
  def test_play_1st_attempt_with_no_match(self):
    selected_colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.BLUE, Colors.PURPLE]
    user_provided_colors = [Colors.BROWN, Colors.DARKBLUE, Colors.DARKGREEN, Colors.PINK, Colors.DARKBLUE, Colors.PINK]
    
    response = play(selected_colors, user_provided_colors, number_of_attempts = 1)

    self.assertEqual(response, ({EXACT: 0, PRESENT: 0, NO_MATCH: 6}, 2, IN_PROGRESS))

  def test_play_1st_attempt_with_matches_out_of_position_and_no_matches(self):   
    selected_colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.PINK, Colors.BROWN]
    user_provided_colors = [Colors.YELLOW, Colors.RED, Colors.ORANGE, Colors.PURPLE, Colors.GREEN, Colors.BLUE]
   
    response = play(selected_colors, user_provided_colors, number_of_attempts = 1)

    self.assertEqual(response, ({EXACT: 0, PRESENT: 4, NO_MATCH: 2}, 2, IN_PROGRESS))

  def test_play_2nd_attempt_with_exact_match(self):   
    selected_colors = [Colors.YELLOW, Colors.RED, Colors.GREEN, Colors.ORANGE, Colors.DARKBLUE, Colors.PINK]
    user_provided_colors = selected_colors
   
    response = play(selected_colors, user_provided_colors, number_of_attempts = 2)

    self.assertEqual(response, ({EXACT: 6, PRESENT: 0, NO_MATCH: 0}, 3, WON))
    
  def test_play_2nd_attempt_with_no_matches(self):   
    selected_colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.BLUE, Colors.PURPLE]
    user_provided_colors = [Colors.BROWN, Colors.DARKBLUE, Colors.DARKGREEN, Colors.PINK, Colors.DARKBLUE, Colors.PINK]
   
    response = play(selected_colors, user_provided_colors, number_of_attempts = 2)

    self.assertEqual(response, ({EXACT: 0, PRESENT: 0, NO_MATCH: 6}, 3, IN_PROGRESS))

  def test_play_20th_attempt_with_exact_match(self):
   
    selected_colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.BLUE, Colors.PURPLE]
    user_provided_colors = selected_colors
   
    response = play(selected_colors, user_provided_colors, number_of_attempts = 20)
   
    self.assertEqual(response, ({EXACT: 6, PRESENT: 0, NO_MATCH: 0}, 21, WON))
   
  def test_play_20th_attempt_with_no_match(self):   
    selected_colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.BLUE, Colors.PURPLE]
    user_provided_colors = [Colors.BROWN, Colors.DARKBLUE, Colors.DARKGREEN, Colors.PINK, Colors.DARKBLUE, Colors.PINK]
   
    response = play(selected_colors, user_provided_colors, number_of_attempts = 20)

    self.assertEqual(response, ({EXACT: 0, PRESENT: 0, NO_MATCH: 6}, 21, LOST))

  def test_play_21st_attempt_with_exact_match(self):   
    selected_colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.BLUE, Colors.PURPLE]
    user_provided_colors = selected_colors
   
    with self.assertRaisesRegex(Exception, "Attempts over 20 not allowed"): 
      play(selected_colors, user_provided_colors, number_of_attempts = 21)
     
  def test_play_21st_attempt_with_no_match(self):   
    selected_colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.BLUE, Colors.PURPLE]
    user_provided_colors = [Colors.BROWN, Colors.DARKBLUE, Colors.DARKGREEN, Colors.PINK, Colors.DARKBLUE, Colors.PINK]

    with self.assertRaisesRegex(Exception, "Attempts over 20 not allowed"): 
      play(selected_colors, user_provided_colors, number_of_attempts = 21)

if __name__ == '__main__':
  unittest.main()
