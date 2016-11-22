import random

#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    N = input("1 = Rock\n2 = Paper\n3 = Scissors\n Enter a Number from 1-3: ")
    if N == "1":
        return 'r'
    elif N == "2":
        return 'p'
    elif N == "3":
        return 's'

#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    comp_move = random.randint(1,3)
    if comp_move == 1:
        return 'r'
    elif comp_move == 2:
        return 'p'
    elif comp_move == 3:
        return 's'

#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    number_of_rounds = input("How many rounds would you like to play? ")
    return int(number_of_rounds)
#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner(p1smove,cmove):
    if p1smove == 'r' and cmove == 's':
        return "Player"
    elif p1smove == 's' and cmove == 'p':
        return "Player"
    elif p1smove == 'p' and cmove == 'r':
        return "Player"
    elif p1smove == 'p' and cmove == "s":
        return "Computer"
    elif p1smove == 's' and cmove == "r":
        return "Computer"
    elif p1smove == 'r' and cmove == 'p':
        return "Computer"
    elif p1smove == "r" and cmove == "r":
        return "Tie"
    elif p1smove == 'p' and cmove == 'p':
        return "Tie"
    elif p1smove == 's' and cmove == 's':
        return "Tie"
        
        
        
        
#function name: get_full_move
#   arguments: a single letter move 'r','p', or 's'
#   purpose: returns the "full" word of a given move
#   returns: returns a string based on the following:
#               "Rock" if given "r"
#               "Paper" if given "p"
#               "Scissors" if given "s"
def get_full_move(short_move):
    if short_move == 'r':
        return "Rock"
    elif short_move == 's':
        return "Scissors"
    elif short_move == 'p':
        return "Paper"

#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(player_score, comp_score, tie):
    print ("You have {} points \nThe computer has {} points\nYou guys tied {} times.".format(player_score,comp_score, tie))
    player_score = int(player_score)
    comp_score = int(comp_score)
    tie = int(tie)
    if player_score > comp_score:
        print ("You win with {} poins".format(player_score))
    elif comp_score > player_score:
        print ("You lost by " + (comp_score - player_score) + " point!!")
    elif comp_score == player_score:
        print ("You tied with the computer")

# function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
# #   returns: none
#def score():
#   player_score = 0
#   comp_score = 0
#   if get_round_winner() == "player":
#        player_score = player_score + 1
#   elif get_round_winner() return "comp":
#        comp_score = comp_score + 1
#   else:
#        return "tie"

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
        while player_score < rounds / 2 and comp_score < rounds / 2:
            if winner == "Player":
                player_score = player_score + 1
            elif winner == "Comp":
                comp_score = comp_score + 1
            elif winner == "Tie":
                ties = ties + 1
        
    print_score(player_score, comp_score, ties)
rps()