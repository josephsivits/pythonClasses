# Retail Class
# Due 03/23/2021

class Account:

    def __init__(self, name, accNum):
        self.account = {}
        self.account.update({name: accNum})
        self.shopList = {}

    def printShopList(self):
        print("Item\t\t\tPrice")
        for x, y in self.shopList.items():
            print(x,"\t\t\t$", y)

        print()

    def addItem(self, name, price):
        self.shopList.update({name: price})

    def removeItem(self, itemName):
        for x in self.shopList.keys():
            if x == itemName:
                del self.shopList[itemName]
                break

    def purchase(self):
        total = int(0)
        for x in self.shopList.values():
            total += x

        self.printShopList()
        print("Total Price: $", total)


class Store:

    def __init__(self):
        self.storeItems = {"GG Logo Bucket Hat": 530, "GG Baseball Hat": 390, "GG Print Joggers": 1020, "GG Jacquard Joggers": 1380, "Leather Dr. G Belt": 360, "Gucci Logo Shirt":590,"GG Beige Print Polo":1150,"GG Rhyton Sneakers":790,"Ace Supreme Sneaker":590}

    def printStore(self):
        print("#", "Item", "\t\t\t\t\t", "Price")
        count = int(1)
        for x, y in self.storeItems.items():
            print(count, x, '\t\t\t', "$", y)
            count += 1


def buy(acc, num):
    if num == 1:
        acc.addItem("GG Logo Bucket Hat", 530)
    elif num == 2:
        acc.addItem("GG Baseball Hat", 390)
    elif num == 3:
        acc.addItem("GG Print Joggers", 1020)
    elif num == 4:
        acc.addItem("GG Jacquard Joggers", 1380)
    elif num == 5:
        acc.addItem("Leather Dr. G Belt", 590)
    elif num ==6:
        acc.addItem("Gucci Logo Shirt", 360)
    elif num == 7:
        acc.addItem("GG Print Polo", 1150)
    elif num == 8:
        acc.addItem("GG Rhyton Sneakers", 790)
    elif num == 9:
        acc.addItem("Ace Supreme Sneakers", 590)

# This is the main driver

print("Welcome new customer!")
gucci = Store()
user = input("Enter your name to enter the store : ")
account = Account(user, "00001")

intent = int(0)
print("Welcome to the Gucci Store!")

gucci.printStore()
intent = int(input("Enter Item # you want to buy (0 exit): "))
while intent != 0:
    buy(account, intent)
    intent = int(input("Enter Item # you want to buy (0 exit): "))

print("Your Shopping Cart:")
account.printShopList()


intent = int(input("Would You like to remove an item(1 for yes, 0 for no): "))

while intent != 0:
    item = input("Enter Item Name you wish to remove: ")
    account.removeItem(item)
    intent = int(input("Would You like to remove an item(1 for yes, 0 for no): "))

print("Time to complete your purchase.")
account.purchase()