import random 

my_busket = {}

ware_1 = input("name of produkt: ")
my_busket[ware_1] = random.randint(1,10)

print(" ")

ware21 = input("name of produkt: ")
my_busket[ware21] = random.randint(10,100)

print(" ")

ware31 = input("name of produkt: ")
my_busket[ware31] = random.randint(10,1000)

print(" ")

ware41 = input("name of produkt: ")
my_busket[ware41] = random.randint(1,100)

print(" ")

ware51 = input("name of produkt: ")
my_busket[ware51] = random.randint(10,20)

print(" ")

print(my_busket)