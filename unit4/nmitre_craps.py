import random 
bank_amount = 100 
print("Welcome to craps where most of the time you loose your money but it's okay :)")

#   function name: get_bet
#   purpose: to get the amount the player wants to bet
#   arguments: bank_amount
#   return: the amount the player betted 

def get_bet(bank_amount):
    bet = int(input("How much would you like to bet?: "))
    while True:
        if bet < 0:
            print("You're not allowed to but negative numbers !")
        elif bet <= bank_amount:
            return bet
        elif bet > 100:
            print("You dont have that type of money :\!")
    bet = int(input("How much would you like to bet?: "))

#   function name: roll2dice 
#   purpose: generating two random dice rolls and prints out, and returns the sum 
#   arguments: none 
#   returns: the sum of the two dice

def get_roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print ("\nRolled 2 dice: {},{}\nDice sum {}".format(dice1,dice2,dice_sum))
    if dice_sum == 2 or 3 or 12:
        return "Player lost"
    elif dice_sum == 7 or 11:
        return "Player won"
    else:
        return dice_sum
    
#   function name: update_of_bank 
#   purpose: update the bank amount he has when winning or losing 
#   arguments: bet, result, anf bank_amount 
#   returns: the amount of money the player won or lost

def update_of_bank(bet,result,bank_amount):
    if result == "Player won":
        bank_amount = bet + bank_amount
        return ("You have Won! Bank amount {}.".format(bank_amount))
    
    elif result == "Player lost":
        bank_amount = bet - bank_amount
        return ("\nYou have Lost! Bank amount {}.".format(bank_amount))
    return bank_amount



def second_roll(dice_sum):
    while True:
        new_dice1 = random.randint(1,6)
        new_dice2 = random.randint(1,6)
        new_dice_sum = new_dice1 + new_dice2
        if new_dice_sum != 7 or new_dice_sum != dice_sum:
            while new_dice_sum != 7 or new_dice_sum != dice_sum:
                return("Rolled 2 dice: {},{}\n Dice sum {}.".format(new_dice1,new_dice2,new_dice_sum))
                
        elif new_dice_sum == 7 or new_dice_sum == dice_sum:
            return ("You have won.")
    
def craps():
    bank_amount = 100
    
    while bank_amount > 0:
        bet = get_bet(bank_amount)
        roll2dice = get_roll2dice()
        dice_sum = roll2dice
        new_dice_sum = second_roll(dice_sum)
    
        if dice_sum == "Player won":
            bank_amount = bet + bank_amount
            print("You have Won :)! Bank amount {}.".format(bank_amount))
        elif dice_sum == "Player lost":
            bank_amount = bet - bank_amount
            print("\nYou have Lost, sucks to be you :( \nBank amount is {}.".format(bank_amount))
        elif dice_sum == dice_sum:
            break

        if new_dice_sum == dice_sum:
            bank_amount = bank_amount + bet
            print("You win Here's your bank amount: {}.".format(bank_amount))
    
craps()