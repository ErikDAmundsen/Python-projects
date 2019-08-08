# for i in range(1,12):
#     print("no {} squared is {} and cubed {:4}".format(i,i**3,i**4))
# # if program flow
# name = input("Please enter your name: ")
# age = int(input ("HOw old are you, {0}".format(name)))
# print(age)
# if age>= 18:
#     print("You are old enough to vote")
# else:
#     print("Please come back in {0}".format(18-age))
print ("please guess a number between 1 and 10:")
guess = int(input())

if guess<5:
    print("guess higher")
    guess = int(input())
    if guess ==5:
        print("Yes")
    else:
        print("No")
elif guess>5:
    print("Guess lower")
    guess=int(input())
    if guess==5:
        print("Well done youve guessed it")
    else:
        print("Sorry, no")
else:
    print("You got it")
# Dont duplicate, bad example