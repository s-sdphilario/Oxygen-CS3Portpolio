class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def display_info(self):
        print("Product: ", self.name)
        print("Price: ₱", self.price)
        print("Quantity: ", self.quantity)
    def sell(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(quantity, self.name, "sold.")
        else:
            print("Not enough stock.")
    def restock(self, amount):
        if amount<=0:
            print("Amount must be greater than 0.")
        else:
            self.quantity += amount
            print("Restock {amount} item(s).")
            print("New quantity: ", self.quantity)
    def remove(self, amount):
        if amount<=0:
            print("Amount must be greater than 0.")
        elif amount <= self.quantity:
            self.quantity -= amount
            print("Remove {amount} item(s).")
            print("New quantity: ", self.quantity)
        else:
            print("Not enough stock to remove that amount.")
    def     show_all_products(self):
        if not self.products:
            print("No products available.")
            return
        print("\n---PRODUCT LIST---")
        print("{'No. ' :<5}{'Name' :<25}{'Price' :<10}{'Quantity' :<10}")
        print("==" * 50)
        for i, p in enumerate(self.products, 1):
            print("{i:<5}{p.name:<25}{p.price:<10}{p.quantity:<10}")
        
    

        
product1 = Product("Nissin Cup Noodles", 50, 25)
product2 = Product("C2 Lemon Tea", 25, 30)
product3 = Product("C2 Red Tea", 25, 30)
product4 = Product("Pringles Cheese Flavor Large",75, 20)
product5 = Product("Pringles Sour Cream Flavor Large", 75, 20)

product1.display_info()
print("--" * 30)
product2.display_info()
print("--" * 30)
product3.display_info()
print("--" * 30)
product4.display_info()
print("--" * 30)
product5.display_info()

print("--Before Selling--")
product1.display_info()
print("\nSelling 3 items")
product1.sell(3)
print("\n--After Selling--")
product1.display_info()

print("--Before Restocking--")
product2.display_info()
print("\n--Restocking items--")
product2.sell(10)
print("\n--After Restocking--")
product2.display_info()

print("--Before Removing--")
product3.display_info()
print("\n--Removing items--")
product3.remove(50)
print("\n--After Removing--")
product3.display_info()