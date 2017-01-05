import random
 
# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
   dice1 = random.randit(1,6)    # generate a random number from 1 to 6
   dice2 = random.randit(1,6)    # generate another random number from 1 to 6
   dice_sum = dice1 + dice2      # get the sum of the two rolls
   print("Roll 2 dice: {}, {}".format(dice1,dice2))     #print the sum 
   return dice_sum  #return the sum
   
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank):
    # ask the player how much they want to bet
   bet = input("How much would like to bet.")
    # if player's bet is more than they have
    #   available in bank, then get new bet
   
    # if player's bet is valid, then return
    #   the bet
 
# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range(dice_sum):
    if dice_sum < 7: # if the sum is over 7, return "over7"
    return "under 7"
    if dice_sum > 7: # if the sum is under 7, return "under7"
    return "over 7"
    if dice_sum == 7: # if the sum is 7, return "equal7"
    return "equal 7"
 
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
    # present user with choices "over7", "under7",
    #   or "equal7"
   
    # return their choice
 
# function for the main game