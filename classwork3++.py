more = ["red", "grey", "green", "pink", "grey", "brown", "red", "grey", "blue", "yellow"]
something = 0
x = input("Введите цвет: ")
for i in more:
    if i == x:
        something = something + 1

print(something)


