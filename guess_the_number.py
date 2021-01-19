#Guess the number
import random

num = random.randint(1,100)

count = 0
game = True
while game:
    guess = int(input("Guess the number : "))

    if guess == num:
        print("Congrats, You guessed the number")
        game = False
    elif guess > num:
        print("You guessed a larger number")
    elif guess < num:
        print("You guessed a smaller number")
    count += 1

    if count == 5:
        print("You lose, Number was",num)
        game = False
