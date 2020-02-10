NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
a = NAT.replace('Fast', 'Gigabit')
print(NAT)
print(a)

print("Мы поменяли Fast на Gigabit")
print("Кол-во символов в начале: ", len(NAT))
print("Кол-во символов в онце: ", len(a))
