# shoppinglist = ["milk","pasta","eggs", "spam", "bread", "rice"]
# for item in shoppinglist:
#     if item == 'spam':
#         continue
#
#     print("Buy "+ item)
#
meal = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
nastyfood = 'spam'
for item in meal:


    if item == nastyfood:
     print("no spam")
     break
    else:
        print("Yes please")
for i in range(0, 100, 7):
    print(i)
    if i>0 and i%11==0:
        break
for i in range(0,20):
    if i%3==0 or i%5==0:
        continue
    print(i)
number = "9,372,223,036,854,775,807"
cleanedNumber = ''

for i in range(0,len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]
newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))

x= 23
x -= 4
print(x)

x/=4
print(x)

greeting = "good "
greeting+= "morning"

print(greeting)
number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for i in range(0,8):
    answer+=5

print(answer)