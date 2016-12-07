import random


def get_p1_move():
    X = input("1 = Rock\n2 = Paper\n3 = Scissors\n Enter number from 1-3: ")
    if X == "1":
        return 'r'
    elif X == "2":
        return 'p'
    elif X == "3":
        return 's'


def get_comp_move():
    comp_move = random.randint(1,3)
    if comp_move == 1:
        return 'r'
    elif comp_move == 2:
        return 'p'
    elif comp_move == 3:
        return 's'


def get_rounds():
    number_of_rounds = input("How many rounds would you like to play? ")
    return int(number_of_rounds)

def get_round_winner(p1smove,cmove):
    if p1smove == 'r' and cmove == 's':
        print ("\nComputer chose scissors\n")
        return "The player wins!"
    elif p1smove == 's' and cmove == 'p':
        print ("\nComputer chose paper\n")
        return "The player wins!"
    elif p1smove == 'p' and cmove == 'r':
        print ("\nComputer chose rock\n")
        return "The player wins!"
    elif p1smove == 'p' and cmove == "s":
        print ("\nYou chose paper\n")
        return "The Computer Won!"
    elif p1smove == 's' and cmove == "r":
        print ("\nYou chose rock\n")
        return "The Computer Won!"
    elif p1smove == 'r' and cmove == 'p':
        print ("\nYou chose paper\n")
        return "The Computer Won!"
    elif p1smove == "r" and cmove == "r":
        print ("\nYou guys both chose rock\n")
        return "It was a Tie!"
    elif p1smove == 'p' and cmove == 'p':
        print ("\nYou guys both chose paper\n")
        return "It was a Tie!"
    elif p1smove == 's' and cmove == 's':
        print ("\nYou guys both chose scissors\n")
        return "It was a Tie!"
        

def get_full_move(short_move):
    if short_move == 'r':
        return "Rock"
    elif short_move == 's':
        return "Scissors"
    elif short_move == 'p':
        return "Paper"


def print_score(player_score, comp_score, tie):
    print ("You have {} points \n The computer has {} points\n You guys tied {} times.".format(player_score,comp_score, tie))
    player_score = int(player_score)
    comp_score = int(comp_score)
    tie = int(tie)

def rps():
    player_score = 0
    comp_score = 0
    ties = 0
    rounds = get_rounds()
    for x in range(rounds):
        p1smove = get_p1_move()
        cmove = get_comp_move()
        winner = get_round_winner(p1smove,cmove)
        print(winner)
        if winner == "The player wins!":
            player_score = player_score + 1
        elif winner == "The Computer Won!":
            comp_score = comp_score + 1
        elif winner == "It was a Tie!":
            ties = ties + 1
    print_score(player_score, comp_score, ties)
    
rps()