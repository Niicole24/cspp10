import random
number = input("Enter a number to end with: ")
print ("The number is between 1 and {}.".format(number))
answer = random.randint(1, int(number))
guessing_number = 0
guess = -1
while guess != answer:
    guessing_number = guessing_number + 1
    guess = int(input("Guess what the number is: "))
    if guess > answer:
        print ("To high, Try again. ")
    elif guess < answer:
        print ("To low, Try again. ")
print ("You are correct! It took you these many guesses {}.".format(guessing_number))