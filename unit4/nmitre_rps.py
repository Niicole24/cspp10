import random


def get_p1_move():
    N = input("1 = Rock\n2 = Paper\n3 = Scissors\n Enter number from 1-3: ")
    if N == "1":
        return 'r'
    elif N == "2":
        return 'p'
    elif N == "3":
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
        return "The Player wins!"
    elif p1smove == 's' and cmove == 'p':
        return "The Player wins!"
    elif p1smove == 'p' and cmove == 'r':
        return "The Player wins!"
    elif p1smove == 'p' and cmove == "s":
        return "The Computer Won!"
    elif p1smove == 's' and cmove == "r":
        return "The Computer Won!"
    elif p1smove == 'r' and cmove == 'p':
        return "The Computer Won!"
    elif p1smove == "r" and cmove == "r":
        return "It was a Tie!"
    elif p1smove == 'p' and cmove == 'p':
        return "It was a Tie!"
    elif p1smove == 's' and cmove == 's':
        return "It was a Tie"
        

def get_full_move(short_move):
    if short_move == 'r':
        return "Rock"
    elif short_move == 's':
        return "Scissors"
    elif short_move == 'p':
        return "Paper"


def print_score(player_score, comp_score, tie):
    print ("You have {} points \nThe computer has {} points\nYou guys tied {} times.".format(player_score,comp_score, tie))
    player_score = int(player_score)
    comp_score = int(comp_score)
    tie = int(tie)
    if player_score > comp_score:
        print ("You win with {} points".format(player_score))
    elif comp_score > player_score:
        print ("You lost by " + (comp_score - player_score) + " point!!")
    elif comp_score == player_score:
        print ("You are tied with the computer.")


def rps():
    player_score = 0
    comp_score = 0
    ties = 0
    rounds = get_rounds()
    for x in range(rounds):
        player_1 = get_p1_move()
        computer_1 = get_comp_move()
        winner = get_round_winner(player_1,computer_1)
        print(winner)
        if winner == "Player":
            player_score = player_score + 1
        elif winner == "Computer":
            comp_score = comp_score + 1
        elif winner == "Tie":
            ties = ties + 1
    print_score(player_score, comp_score, ties)
rps()