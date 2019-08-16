import random
highest = 10
answer = random.randint(1,highest)

print("Please guess a number btw 1 and {} ".format(highest))
guess=0
while guess != answer:
    guess = int(input())
    if guess<answer:
        print("guess higher")
    elif guess >answer:
        print("guess lower")
    else:
     print("you got it!")
