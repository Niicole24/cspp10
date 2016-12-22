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
#   purpose: get the amount of money the players wants to play.
#   arguments: none 
#   returns: the amount of money the player betted


def get_bet(bank_amount):
    bet = int(input("How much would you like to bet? "))
    while True:
        if bet < 0:
            print("There's no negative numbers allowed!")
        elif bet <= bank_amount:
            return bet
        elif bet > 100:
            print("You dont have that type of money with you!")

#   function name: first_roll
#   purpose: get the result of the roll
#   arguments: 
#       roll - the sum of the two dice rolled
#       is_first_roll - true/false depending on which roll it is
#   returns: the result
#       if player wins: return "win"
#       if player lost: return "lose"

def first_roll(player_sum,point_roll):
    if player_sum == 2 or 3 or 12:
        return "Player loses"
    elif player_sum == 7 or 11:
        return "House wins"
    elif point_roll == 4 or point_roll == 5 or point_roll == 6 or point_roll == 8 or point_roll == 9 or point_roll == 10:
        print ("Point number is {}.".format(point_roll))
        
def point_number():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    new_dice = dice_1 + dice_2
    new