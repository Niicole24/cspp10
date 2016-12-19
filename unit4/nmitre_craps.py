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


def roll_result(player_sum,house_sum,point_number):
    if player_sum == 2 or player_sum == 3 or player_sum == 12:
        return "Player loose"
    elif house_sum == 7 or house_sum == 11:
        return "House wins"
    elif point_number == 4 or point_number == 5 or point_number == 6 or point_number == 8 or point_number == 9 or point_number == 10:
        print ("Point number is {}.".format(point_number))

def 
    
#def point_roll(get_bet,roll_result,bet):
# roll_result()