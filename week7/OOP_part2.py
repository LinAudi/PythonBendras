class CoffeShop:
    def __init__(self,name,menu):
        self.name = name
        self.menu = menu
        self.orders = []

    def add_order(self, item_name):
        for item in self.menu:
            if item["item_name"] == item_name:
                self.orders.append(item_name)
                return f"The {item_name} is added to the order."
        return f"{item_name} item is not available at this moment."


    def fulfill_order(self,item_name):
        if item_name in self.orders:
            return f"The {item_name} is ready!"
        return "All orders have been fulfilled!"


    def list_orders(self):
        return self.orders

    def due_amount(self):
        price=0
        for item in self.orders:
            price += int(item["item_price"])
        return price

    def drinks_only(self):
        self.menu
        drinks = [item["item_name"]for item in self.menu if item["item_type"] =="Gėrimas"]
        return drinks



menu = [
            {"item_name":"Kava","item_type":"Gėrimas","item_price":2},
            {"item_name":"Sultys","item_type":"Gėrimas","item_price":1.5},
            {"item_name":"Bandelė","item_type":"Užkandis","item_price":0.8},
            {"item_name":"Sumuštinis","item_type":"Užkandis","item_price":2}
        ]
kavine = CoffeShop("Kavine", menu)

print(kavine.add_order("Kava"))
print(kavine.add_order("Iced tea"))
print(kavine.add_order("Bandelė"))
print(kavine.add_order("Sumuštinis"))

print(kavine.list_orders())
print(kavine.due_amount())

print(kavine.fulfill_order("Kava"))
print(kavine.fulfill_order("Bandelė"))
print(kavine.fulfill_order("Sumuštinis"))
print(kavine.fulfill_order("Iced tea"))

print(kavine.list_orders())
print(kavine.due_amount())
print(kavine.drinks_only())