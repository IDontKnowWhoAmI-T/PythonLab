cities = ["Moscow", "Dubai" "New York", "Los Angeles", "Tokio"]
print("Where do you want to go?")
found = False
cityAdd = input("Tell us the name of this city: ")
for city in cities:
    if cityAdd == city:
        found = True

if found == True:
    print("Found")
else:
    print("Not found")
