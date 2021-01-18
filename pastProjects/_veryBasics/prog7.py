# number guessing game in python

import random

win_number = random.randint(1, 100)
count = 0
cont = True

while cont:
    guess = int(input("Guess a number between 1 and 100: "))
    count += 1
    if guess == win_number:
        cont = False
        print(f"CORRECT! You Won...! in {count} trials.")
    elif guess < win_number:
        print("Think higher...")
    else:
        print("Go a bit low")

print("Game Over")

# //////////////////////////////////////////////////////////////////////////////

# # program to find the sum of digits in a number entered

# num = input("Enter a number: ")
# add = 0

# for i in num:
#     add += int(i)

# print("The sum of the digits in the number = {}".format(add))
