import unittest
from src.master_mind import Colors, Match, guess

EXACT = Match.EXACT
PRESENT = Match.PRESENT
NO_MATCH = Match.NO_MATCH

class Test_guess(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)
      
  def test_guess_with_all_colors_match_in_position(self):
    selected_colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.BLUE, Colors.PURPLE]
    user_provided_colors = selected_colors
    
    response = guess(selected_colors, user_provided_colors)
    
    self.assertEqual(response[EXACT], 6) 
     
  def test_guess_with_all_colors_mismatch(self):
    selected_colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.BLUE, Colors.PURPLE]
    user_provided_colors = [Colors.BROWN, Colors.DARKGREEN, Colors.DARKBLUE, Colors.PINK, Colors.BROWN, Colors.DARKGREEN]
    
    response = guess(selected_colors, user_provided_colors)
    
    self.assertEqual(response[NO_MATCH], 6)
    
  def test_guess_with_all_colors_match_out_of_position(self):
    selected_colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.BLUE, Colors.PURPLE]
    user_provided_colors = [Colors.YELLOW, Colors.RED, Colors.ORANGE, Colors.PURPLE, Colors.GREEN, Colors.BLUE] 
    
    response = guess(selected_colors, user_provided_colors)
    
    self.assertEqual(response[PRESENT], 6)
    
  def test_guess_with_first_four_colors_match_in_position(self):
    selected_colors = [Colors.RED, Colors.BLUE, Colors.YELLOW, Colors.BROWN, Colors.DARKBLUE, Colors.DARKGREEN]
    user_provided_colors = [Colors.RED, Colors.BLUE, Colors.YELLOW, Colors.BROWN, Colors.PINK, Colors.PURPLE]
    
    response = guess(selected_colors, user_provided_colors)

    self.assertEqual(response, {EXACT: 4, PRESENT: 0, NO_MATCH: 2})
    
  def test_guess_with_last_four_colors_match_in_position(self):
    selected_colors = [Colors.ORANGE, Colors.BLUE, Colors.YELLOW, Colors.BROWN, Colors.PINK, Colors.RED]
    user_provided_colors = [Colors.DARKGREEN, Colors.PURPLE, Colors.YELLOW, Colors.BROWN, Colors.PINK, Colors.RED]
    
    response = guess(selected_colors, user_provided_colors)
    
    self.assertEqual(response, {EXACT: 4, PRESENT: 0, NO_MATCH: 2})
    
  def test_guess_3_exact_match_and_3_match_out_of_position(self):
    selected_colors = [Colors.RED, Colors.BLUE, Colors.YELLOW, Colors.PURPLE, Colors.BROWN, Colors.DARKGREEN]
    user_provided_colors = [Colors.RED, Colors.BLUE, Colors.YELLOW, Colors.BROWN, Colors.DARKGREEN, Colors.PURPLE]
    
    response = guess(selected_colors, user_provided_colors)
    
    self.assertEqual(response, {EXACT: 3, PRESENT: 3, NO_MATCH: 0})
    
  def test_guess_first_and_third_no_match_second_exact_match_and_others_match_out_of_position(self):
    selected_colors = [Colors.PINK, Colors.BLUE, Colors.DARKBLUE, Colors.BROWN, Colors.PURPLE, Colors.DARKGREEN]
    user_provided_colors = [Colors.RED, Colors.BLUE, Colors.YELLOW, Colors.DARKGREEN, Colors.BROWN, Colors.PURPLE]
    
    response = guess(selected_colors, user_provided_colors)
    
    self.assertEqual(response, {EXACT: 1, PRESENT: 3, NO_MATCH: 2}) 

  def test_guess_first_color_in_selected_repeated_five_times(self):
    selected_colors = [Colors.PINK, Colors.BLUE, Colors.DARKBLUE, Colors.BROWN, Colors.PURPLE, Colors.DARKGREEN]
    user_provided_colors = [Colors.PINK, Colors.PINK, Colors.PINK, Colors.PINK, Colors.PINK, Colors.RED]
    
    response = guess(selected_colors, user_provided_colors)
    
    self.assertEqual(response, {EXACT: 1, PRESENT: 0, NO_MATCH: 5})

  def test_guess_last_color_in_selected_repeated(self):
    selected_colors = [Colors.PINK, Colors.BLUE, Colors.DARKBLUE, Colors.BROWN, Colors.PURPLE, Colors.DARKGREEN]
    user_provided_colors = [Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.DARKGREEN, Colors.DARKGREEN, Colors.DARKGREEN]
    
    response = guess(selected_colors, user_provided_colors)
    
    self.assertEqual(response, {EXACT: 1, PRESENT: 0, NO_MATCH: 5})
   
  def test_guess_first_in_selected_repeated_from_two_to_six_first_in_guess_is_second_color_in_selection(self):
    selected_colors = [Colors.BLUE, Colors.PINK, Colors.DARKBLUE, Colors.BROWN, Colors.PURPLE, Colors.DARKGREEN]
    user_provided_colors = [Colors.PINK, Colors.BLUE, Colors.BLUE, Colors.BLUE, Colors.BLUE, Colors.BLUE]
    
    response = guess(selected_colors, user_provided_colors)
    
    self.assertEqual(response, {EXACT: 0, PRESENT: 2, NO_MATCH: 4})
   
  def test_guess_first_in_selected_repeated_from_two_to_six_first_in_guess_no_match(self):
    selected_colors = [Colors.BLUE, Colors.PINK, Colors.DARKBLUE, Colors.BROWN, Colors.PURPLE, Colors.DARKGREEN]
    user_provided_colors = [Colors.RED, Colors.BLUE, Colors.BLUE, Colors.BLUE, Colors.BLUE, Colors.BLUE]
    
    response = guess(selected_colors, user_provided_colors)
    
    self.assertEqual(response, {EXACT: 0, PRESENT: 1, NO_MATCH: 5})  
  
if __name__ == '__main__':
  unittest.main()
