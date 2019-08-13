for i in (range (1,20)):
    print("i is now {}".format(i))
    number = "9,223,372"
    for i in range(0, len(number)):
        print (number[i])

print("i is now {}".format(i))
number = "9,223,372,036,854,775"
CleanedNumber = ' '
for i in range(0, len(number)):
        if number[i] in'1234567890':
            CleanedNumber += number[i]
newNumber = int(CleanedNumber)
print("The nuberis {}".format(newNumber))

number = "9,223,372,036,854,775"
CleanedNumber = ' '

for char in number:
    if char in '0123456789':
        CleanedNumber += char
newNumber = int(CleanedNumber)
print (newNumber)

for state in ["illinois","alabam","Washington"]:
    print("Driving through {}".format(state))


for i in range(0,100,5):
    print("i is {}".format(i))


for i in range(1,13):
    for j in range(1,13):
        print ("{0} time {1} equals {2}".format(i,j,i*j))

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
for char in quote:
    if char in"ABCDEFGHIJKLMONOPQRSTUVWXYZ":
        print (char)