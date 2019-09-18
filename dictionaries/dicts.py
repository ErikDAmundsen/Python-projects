fruit = {"orange": "a sweet, orange citrus fruit",
         "apple":"good for making cider",
         "lemon": " a sour, yellow crirus fruit",
         "grape": "a sour, green citrus fruit"

         }
veg={
    "cabbage": "every childs favorite",
    "Sprouts": "mm, lovely",
    "sprinch": "more pleace"

}
# veg.update(fruit)
# print(veg)
# print(fruit.update(veg))
# print(fruit)

niceAndNasty = fruit.copy()
niceAndNasty.update(veg)
print(niceAndNasty)
print(fruit)