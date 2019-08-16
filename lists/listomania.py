menu = []
menu.append(["1egg", "spam", "bacon"])
menu.append(["2 egg", "spam", "bacon"])
menu.append(["3egg", "spam", "bacon"])
menu.append(["4egg", "spam", "bacon"])
menu.append(["5egg", "spam", "bacon"])
menu.append(["6egg", "spam", "bacon"])
# print (menu)

for meal in menu:
    if  "2" in meal:
        print(meal)
        for ingredients in meal:
            print(ingredients)
