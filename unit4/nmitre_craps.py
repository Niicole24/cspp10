import random 
bank_amount = 100 
print("Welcome to craps where most of the time you loose your money but it's okay :)")

def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print ("Rolled 2 dice: {},{}".format(dice1,dice2))
    return dice_sum
    

def get_bet(bank_amount):
    bet = int(input("How much would you like to bet? "))
    while True:
        if bet < 0:
            print("There's no negative numbers allowed!")
            
        elif bet <= bank_amount:
            return bet
            
        elif bet > 100:
            print("You dont have that type of money with you!")


def first_roll(player_sum,point_roll):
    if player_sum == (2) or (3) or (12):
        return "Player loose"
    elif player_sum == (7) or (11):
        return "House wins"
    elif point_roll == 4 or point_roll == 5 or point_roll == 6 or point_roll == 8 or point_roll == 9 or point_roll == 10:
        print ("Point number is {}.".format(point_roll))
        
def point_number():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    new_dice = dice_1 + dice_2
        
    
    
    
    
#def point_roll(get_bet,roll_result,bet):
# roll_result()