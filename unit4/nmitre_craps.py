import random 
#   function name: roll2dice 
#   purpose: generating two random dice rolls and prints out, and returns the sum 
#   arguments: none 
#   returns: the sum of the two dice

def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print ("Rolled 2 dice: {},{}".format(dice1,dice2))
    return dice_sum
    
#   function name: get_bet 
#   purpose: get the amount of money the players wants to play.
#   arguments: none 
#   returns: the amount of money the player betted

def get_bet():

#   function name: roll_result
#   purpose: get the result of the roll
#   arguments: 
#       roll - the sum of the two dice rolled
#       is_first_roll - true/false depending on which roll it is
#   returns: the result
#       if player wins: return "win"
#       if player lost: return "lose"

def roll_result():