# x = int(5 )
# y= int(7)
#
# if x>y:
#     print("x is greater than y")
# elif x<y:
#     print("x is smaller than y")
# else:
#     print("x equals y")

age = int(input("What is your age"))
name = (input("What is your name"))

if age>18 and age<31:
    print("{} you are elegible for the trip".format(name))
else:
    print("sorry {}you are ineligible for the trip".format(name))