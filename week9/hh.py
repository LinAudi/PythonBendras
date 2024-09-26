class TableManagement:
    def __init__(self):
        # Simulates table availability; None means unreserved
        self.tables = {i: None for i in range(1, 11)}  # 10 tables in the restaurant

    def check_reservation(self, name):
        for table, reserved_name in self.tables.items():
            if reserved_name == name:
                return table
        return None

    def reserve_table(self, name):
        for table_number, reserved in self.tables.items():
            if not reserved:
                self.tables[table_number] = name
                print(f"Table {table_number} reserved for {name}.")
                return table_number
        print("Sorry, no tables available.")
        return None

    def show_tables(self):
        print("\nTable Status:")
        for table, reserved in self.tables.items():
            status = f"reserved by {reserved}" if reserved else "available"
            print(f"Table {table}: {status}")


class Menu:
    def __init__(self):
        self.items = {
            "Breakfast": {"Pancakes": {"weight": 200, "time": 10, "calories": 450, "price": 5}},
            "Lunch": {"Vegan Salad": {"weight": 150, "time": 5, "calories": 300, "price": 7}},
            "Dinner": {"Steak": {"weight": 350, "time": 15, "calories": 800, "price": 20}},
            "Drinks": {"Coke": {"weight": 200, "time": 0, "calories": 180, "price": 2}},
        }

    def display_menu(self):
        for meal, dishes in self.items.items():
            print(f"\n---{meal.upper()}---")
            for dish, details in dishes.items():
                print(
                    f"{dish}: Weight: {details['weight']}g, Time: {details['time']}min, Calories: {details['calories']}cal, Price: ${details['price']}"
                )


class Order:
    def __init__(self):
        self.cart = []

    def add_to_order(self, item_name, menu):
        for meal, dishes in menu.items.items():
            if item_name in dishes:
                self.cart.append({item_name: dishes[item_name]})
                print(f"Added {item_name} to your order.")
                return
        print(f"{item_name} is not on the menu.")

    def remove_from_order(self, item_name):
        for item in self.cart:
            if item_name in item:
                self.cart.remove(item)
                print(f"Removed {item_name} from your order.")
                return
        print(f"{item_name} is not in your order.")

    def view_order(self):
        print("\nYour current order:")
        for item in self.cart:
            for name, details in item.items():
                print(f"{name}: ${details['price']}")

    def finalize_order(self):
        total_cost = sum(item[list(item.keys())[0]]["price"] for item in self.cart)
        print(f"\nTotal payable: ${total_cost:.2f}")
        return total_cost

    def add_tip(self, total_cost, percentage):
        tip = total_cost * percentage / 100
        total_with_tip = total_cost + tip
        print(f"Including tip, your total is: ${total_with_tip:.2f}")
        return total_with_tip


def main():
    print("Welcome to the Restaurant Management System")
    table_manager = TableManagement()
    menu = Menu()
    order = Order()

    # Handle table reservation
    name = input("Please enter your name for reservation check: ")
    reserved_table = table_manager.check_reservation(name)
    if not reserved_table:
        reserved_table = table_manager.reserve_table(name)
    if reserved_table:
        table_manager.show_tables()
        menu.display_menu()

        # Handle ordering
        while True:
            choice = input(
                "\nWould you like to add, remove, view, or finalize your order? (add/remove/view/finalize): "
            ).lower()
            if choice == "add":
                item = input("Enter an item to add to your order: ")
                order.add_to_order(item, menu)
            elif choice == "remove":
                item = input("Enter an item to remove from your order: ")
                order.remove_from_order(item)
            elif choice == "view":
                order.view_order()
            elif choice == "finalize":
                total = order.finalize_order()
                tip_percent = float(input("Enter tip percentage (0 for no tip): "))
                total_with_tip = order.add_tip(total, tip_percent)
                break


if __name__ == "__main__":
    main()
