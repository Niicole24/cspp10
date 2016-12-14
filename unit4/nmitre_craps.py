import random 
bank_amount = 100 
print("Welcome to craps where most of the time you loose your money but it's okay :)")

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
#   purpose: to get the amount to be bet from the user. Validate the amount and repeatedly ask them until they enter in something valid.
#   arguments: bank amounts
#   returns: The chosen valid bet amount 

def get_bet(bank_amount):
    bet = int(input("How much would you like to bet?"))
    while True:
        if bet < 0:
            print("There's no negative numbers allowed!")
            
        elif bet <= bank_amount:
            return bet
            
        elif bet > 100:
            print("You dont have that type of money with you!")
        
        
        
#   function name: roll_result
#   purpose: get the result of the roll
#   arguments: 
#       roll - the sum of the two dice rolled
#       is_first_roll - true/false depending on which roll it is
#   returns: the result
#       if player wins: return "win"
#       if player lost: return "lose"

def roll_result(dice_sum):
    if (dice_sum == 2) or (dice_sum == 3) or (dice_sum == 12):
        return "lose"
    elif (dice_sum == 7) or (dice_sum == 11):
        return "win"
    else: 
        return dice_sum
    
#   function name: Rounds():
#   purpose: the amount of rounds that the player wants to play
#   argument: none 
#   return: rounds chosen

def rounds():