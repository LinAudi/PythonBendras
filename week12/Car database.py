# Either use the car database you created in the previous
# exercise or download the database:
#
# .
#
# Write a Python program that allows the user via the console to:
#
#     Enter a new car record.
#
#     Search for records based on all columns in the database.
#
# The user can choose which columns to skip in the search.
# For year and price, the user should specify a range (from ... to ...).

import sqlite3

# Connect to the SQLite database (create the DB if it doesn't exist)
conn = sqlite3.connect("cars.sqlite")
cursor = conn.cursor()


# Function to insert a new car into the database
def insert_car(make, model, color, year, price):
    cursor.execute("INSERT INTO cars (make, model, color, year, price) VALUES (?, ?, ?, ?, ?)",
                   (make, model, color, year, price))
    conn.commit()
    print("Car added successfully!")


# Function to search cars in the database
def search_cars(make=None, model=None, color=None, year_range=None, price_range=None):
    query = "SELECT * FROM cars WHERE 1=1"
    params = []

    # Add filtering based on user input
    if make:
        query += " AND make = ?"
        params.append(make)
    if model:
        query += " AND model = ?"
        params.append(model)
    if color:
        query += " AND color = ?"
        params.append(color)
    if year_range:
        query += " AND year BETWEEN ? AND ?"
        params.extend(year_range)
    if price_range:
        query += " AND price BETWEEN ? AND ?"
        params.extend(price_range)

    cursor.execute(query, params)
    results = cursor.fetchall()

    # Display the search results
    if results:
        for row in results:
            print(f"Make: {row[0]}, Model: {row[1]}, Color: {row[2]}, Year: {row[3]}, Price: {row[4]}")
    else:
        print("No matching cars found.")


# Function to take user input for a new car
def add_new_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    color = input("Enter car color: ")
    year = int(input("Enter car year: "))
    price = int(input("Enter car price: "))
    insert_car(make, model, color, year, price)


# Function to handle search filters
def search_for_car():
    print("Enter search criteria. Press Enter to skip a parameter.")

    make = input("Enter car make (or leave blank): ")
    model = input("Enter car model (or leave blank): ")
    color = input("Enter car color (or leave blank): ")

    # Year range input
    year_from = input("Enter start year (or leave blank): ")
    year_to = input("Enter end year (or leave blank): ")
    year_range = None
    if year_from and year_to:
        year_range = (int(year_from), int(year_to))

    # Price range input
    price_from = input("Enter minimum price (or leave blank): ")
    price_to = input("Enter maximum price (or leave blank): ")
    price_range = None
    if price_from and price_to:
        price_range = (int(price_from), int(price_to))

    # Call the search function with the filters
    search_cars(make=make if make else None,
                model=model if model else None,
                color=color if color else None,
                year_range=year_range,
                price_range=price_range)


# Main function to run the program
def main():
    while True:
        print("\n--- Car Database ---")
        print("1. Add new car")
        print("2. Search cars")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_new_car()
        elif choice == "2":
            search_for_car()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")


# Run the main program
if __name__ == "__main__":
    main()

# Close the database connection when the program ends
conn.close()