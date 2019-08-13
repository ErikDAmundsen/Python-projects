for i in range(10):
    print("i is not {}".format(i))
i = 0
while i< 10:
    print("i is not{}".format(i))
    i+=1
availableExits= ("east", "west", "north", "south")
choseExit=""
while choseExit not in availableExits:
    choseExit = input("please choose a direction")
    if choseExit=="quit":
        break
else:
    print("arent you glad you got out")
