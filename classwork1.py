import random
x = 0
players = []

quests = ["Соверши пранк над игроком находящимя справа от тебя", "Съешь тапок", "Принеси дорогую для тебя вещь в жертву демонам",
         "Иди вон!", "Спрячься"]

o = input("Введите количество игроков: ")
o = int(o)
print("Введите имена игроков: ")
while x < o:
    name = input("Имя: ")
    players.append(name)
    x = x + 1
print(players)
while True:
    player = random.randint(0, o-1)
    quest = random.randint(0, len(quests) - 1)
    print(players[player], quests[quest])
    input()
  
