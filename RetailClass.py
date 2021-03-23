# Retail Class
# Due 03/23/2021

class Account:

    def __init__(self, name, accNum):
        self.account = {}
        self.account.update({name: accNum})
        self.shopList = {}

    def printShopList(self):
        print("Item", "      ", "Price")
        for x, y in self.shopList.items():
            print(x, '       ', "$", y)

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
        self.storeItems = {"Hat": 1111, "Shoes": 1111, "Pants": 1111, "Shirt": 1111, "Belt": 1111}

    def printStore(self):
        print("#", "Item", "      ", "Price")
        count = int(1)
        for x, y in self.storeItems.items():
            print(count, x, '       ', "$", y)
            count += 1


def buy(acc, num):
    if num == 1:
        acc.addItem("Hat", 1111)
    elif num == 2:
        acc.addItem("Shoes", 1111)
    elif num == 3:
        acc.addItem("Pants", 1111)
    elif num == 4:
        acc.addItem("Shirt", 1111)
    elif num == 5:
        acc.addItem("Belt", 1111)


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