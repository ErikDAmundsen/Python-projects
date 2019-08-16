# ipAddress = input("please enter an ip address:")
# print(ipAddress.count("."))

parrotList = ["not pinin", "no more","a stiff", "bereft of life"]
parrotList.append("A norwegian blue parrot")
for state in parrotList:
    print("this parrot is "+ state)

even=[2,4,6,8]
odd=[1,3,5,7]

numbers = even +odd
numbers.sort()
print(numbers)
# print(sorted(numbers))

list1= []
list2=list()

if list1 ==list2:
    print("the lists are equal")
print(list("THe lists are equal"))

anotherEven = list(even)
anotherEven.sort(reverse=True)
print(even)

number=[even,odd]
print(number)