age = 24
print("my age is " + str(age))
#replacement fields
print ("my age is {0} years".format(age))
print("i have {0} brothers and {1} sister and {1} dogs".format(2,4) )
# old method
for i in range(1,12):
    print("no. %2d squared is %4d and cubed is %4d" %(i, i **2,i**3))
for i in range(1,12):
    print("no. {0:2} squared is {0:<4} and cubed is {2:<4}".format (i, i **2,i**3))