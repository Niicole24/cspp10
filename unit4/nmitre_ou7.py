import random
 
# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
   dice1 = random.randint(1,6)    
   dice2 = random.randint(1,6)    
   dice_sum = dice1 + dice2      
   print("Roll 2 dice: {}, {}".format(dice1,dice2))  
   return dice_sum  
   
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank):
   bet = int(input("Enter your bet:"))
while (bet > bank):
        bet = int(input("Enter a valid bet: "))
        return bet
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
    else:
        "equal7"
 
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
   # present user with choices "over7", "under7",
    #   or "equal7"
    print("Choose from the following")
    print("1. over 7 \n2. under 7 \n3. equal to 7")
    # return their choice
    choice = input("Choose from [1|2|3]")
    if choice == 1:
        return "over7"
    elif choice == 2:
        return "under7"
    else:
        return "equal7"
        
def overunder7 ():
    bank = 100 
    while bank > 0:
        bet = get_bet(bank)
        uer_range = choose_range()
        dice = roll2dice()
        round_range = get_range(dice)
        if user_range == round_range:
            print("you win")
            if user_range == "equal7": 
                bank = bank + 4 * bet
        else:
            bank = bank + bet
            
    else: 
        print("You lost")
        bank = bank + bet 
            
        print("your balance is ${}".format(bank))
        
        new_round = input("Do you want to continue?").lower()
        if new_round != "y":
            break
        
        print("Game over, you have ${} in your bank.".format(bank))
        
overunder7()