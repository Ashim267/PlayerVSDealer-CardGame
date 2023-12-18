# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.


hand_value= draw_starting_hand("YOUR TURN")

while  hand_value< 21:
  should_hit = input('You have ' +str(hand_value)+ ". Hit (y/n)? ")
  if should_hit == 'n':
    break
  elif should_hit == 'y':
    c=draw_card()
    hand_value = hand_value + c
print_end_turn_status(hand_value)

print_header("DEALER TURN")
a= dealer()

user_hand=hand_value
dealer_hand= a

print_end_game_status(user_hand, dealer_hand)





