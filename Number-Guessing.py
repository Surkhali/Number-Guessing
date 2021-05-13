print()
print("---- Welcome to the Number Guessing Game ----")
print("---- By Sujan Surkhali ----")
print()

import random

while True:
    condition = True
    while condition:
        print("\n------------------------------------")
        num = input("\tGive the number where to end: ")
        print("------------------------------------")
        print()

        if num.isdigit():
            print("\n------------------------------------")
            print("\tLet's begin the challenge!!!")
            print("------------------------------------")
            print()
            num = int(num)
            condition = False
        else:
            print("Alert!!!")
            print("Wrong value input!!!")

    secret = random.randint(1,num)

    guess = None
    count = 1

    while guess != secret:
        guess = input("Give the number between 1 to " + str(num) + ": ")
        if guess.isdigit():
            guess = int(guess)
        if guess == secret:
            print("You win the challenge!!!")
        else:
            print("You have to try again!!!")
            print()
            count +=1
    print("\n------------------------------------")
    print("************** LOL XD **************")
    print("------------------------------------")
    print(" |'It took you",{count},"time to guess.'|")
    print("------------------------------------")

