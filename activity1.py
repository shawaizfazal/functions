import random
playing = True
number = str (random.randint(0,9))
print("i will generate a number from 0 to 9 you have to guess it exactly but one didgit at a time ")
print("the game ends when you get 1 hero! ")
while playing:
    guess=input ("give me your best try! /n")
    if number == guess:
        print("you will win the game eventually")
        print("the number was ",number)
        break
    else:
        print("your observation isnt right please try again!/n")