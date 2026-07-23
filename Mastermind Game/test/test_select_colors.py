import unittest
import random
from src.master_mind import select_colors, Colors

class Test_select_colors(unittest.TestCase):
    def test_randomize_selected_colors_given(self):
        selected_colors = select_colors(None)
        allowed_colors = [Colors.RED, Colors.BLUE, Colors.BROWN, Colors.DARKBLUE, Colors.DARKGREEN, Colors.GREEN, Colors.ORANGE, Colors.PINK, Colors.PURPLE, Colors.YELLOW]
        
        self.assertEqual(len(selected_colors), 6)
        self.assertTrue(all(color in allowed_colors for color in selected_colors))
    
    def test_randomized_selected_colors_different_when_called_twice(self):
        seed = 1
        seed2 = 2
        
        selected_colors_call1 = select_colors(seed)
        selected_colors_call2 = select_colors(seed2)
        
        self.assertNotEqual(selected_colors_call1, selected_colors_call2)
       
if __name__ == '__main__':
    unittest.main()
    