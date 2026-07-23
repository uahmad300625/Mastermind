from enum import Enum
from collections import Counter
import random

RANGE_END: int = 6

class Colors(Enum):
  RED = 1
  ORANGE = 2
  YELLOW = 3
  GREEN = 4
  BLUE = 5
  PURPLE = 6
  BROWN = 7
  PINK = 8
  DARKGREEN = 9
  DARKBLUE = 10

class Match(Enum):
  EXACT = "Exact Match"
  PRESENT = "Non Positional Match"
  NO_MATCH = "Color and Position Do Not Match" 
  
class GameStatus(Enum):
  WON = "Player Guessed Correctly"
  IN_PROGRESS = "Player Guess not 100% Correct and Wants to Keep Playing"
  LOST = "Player Decides to Quit or Could not Guess Correctly in 20 Attempts"


def guess(selected_colors, user_provided_colors):
   def match_for_position(position):
     candicate_color = user_provided_colors[position]

     if candicate_color == selected_colors[position]:
       return Match.EXACT

     if candicate_color in user_provided_colors[0:position]:
       return Match.NO_MATCH

     index = selected_colors.index(candicate_color) if candicate_color in selected_colors else -1
     
     if index > -1 and selected_colors[index] != user_provided_colors[index]:
       return Match.PRESENT
 
     return Match.NO_MATCH

   return {**{Match.EXACT: 0, Match.PRESENT: 0, Match.NO_MATCH: 0}, **Counter(map(match_for_position, range(0, RANGE_END)))}

def play(selected_colors, user_provided_colors, number_of_attempts):
  if(number_of_attempts > 20):
    raise Exception("Attempts over 20 not allowed")

  response = guess(selected_colors, user_provided_colors)
  next_attempt_number = number_of_attempts + 1
  
  return (response, next_attempt_number, GameStatus.WON if response[Match.EXACT] == 6 and number_of_attempts <= 20 
          else GameStatus.LOST if next_attempt_number > 20 
          else GameStatus.IN_PROGRESS)
  
def select_colors(seed_value):
  random.seed(seed_value)
  colors_list = [Colors.RED, Colors.BLUE, Colors.BROWN, Colors.DARKBLUE, Colors.DARKGREEN, 
                Colors.GREEN, Colors.ORANGE, Colors.PINK, Colors.PURPLE, Colors.YELLOW]
  
  selected_colors = random.sample(colors_list, 6)
  
  return selected_colors
 