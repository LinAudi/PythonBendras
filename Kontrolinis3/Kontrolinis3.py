import sqlite3

conn = sqlite3.connect("Finances.db")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS finances(
id INTEGER PRIMARY KEY AUTOINCREMENT,
tipas TEXT NOT NULL,
suma FLOAT NOT NULL,
kategorija TEXT NOT NULL)
"""
)
conn.commit()


def continued():
    while True:
        input("Press any key to continue").lower()
        break


def data_input(type, amount, category):
    cursor.execute(
        "INSERT INTO Finances (tipas, suma, kategorija) VALUES (?, ?, ?)",
        (type, amount, category),
    )
    conn.commit()


def add_income():
    type = "Įplaukos"
    amount = input("Įveskite įplaukas: ")
    category = input("Įveskite Kategoriją:").upper()

    data_input(type, amount, category)
    continued()


def add_expenses():
    type = "Išlaidos"
    amount = input("Įveskite išlaidas: ")
    category = input("Įveskite Kategoriją:").upper()

    data_input(type, amount, category)
    continued()


def get_all_income():
    query1 = "SELECT SUM(suma) FROM Finances WHERE tipas ='Įplaukos'"
    cursor.execute(query1)
    income_total = cursor.fetchone()[0]
    return income_total


def get_all_expenses():
    query2 = "SELECT SUM(suma) FROM Finances WHERE tipas ='Išlaidos'"
    cursor.execute(query2)
    expenses_total = cursor.fetchone()[0]
    return expenses_total


def get_balance():
    balance_total = get_all_income() - get_all_expenses()
    print(f"Balansas yra: {balance_total} Eur")
    continued()


def table():
    cursor.execute("SELECT * FROM finances")  # Replace with your table name
    rows = cursor.fetchall()
    print("(id, tipas, suma, kategorija)")
    if rows:
        for row in rows:
            print(row)
        else:
            print("Daugiau įvesčių nėra:")


def delete():
    table()

    delete_row_id = int(input("Įveskite pašalinti norimos eilutės ID."))
    query4 = "DELETE FROM finances WHERE id = ?"
    cursor.execute(query4, (delete_row_id,))
    conn.commit()
    print(f"Eilutė nr. {delete_row_id} buvo pašalinta.")
    continued()


def update():
    table()
    delete_row_id1 = int(input("Įveskite pakeisti norimos eilutės ID."))

    update_type = input("Ką norite pakeisti sumą, ar kategoriją?").lower()
    if update_type == "suma" or update_type == "sumą":
        input1 = input("Įveskite naują sumą:")
        query5 = """UPDATE finances SET suma = ? WHERE id = ?"""
        cursor.execute(
            query5,
            (
                input1,
                delete_row_id1,
            ),
        )
        conn.commit()
        continued()

    elif update_type == "kategorija" or update_type == "kategoriją":
        input2 = input("Įveskite naują kategoriją:").upper()
        query6 = """UPDATE finances SET kategorija = ? WHERE id = ?"""
        cursor.execute(
            query6,
            (
                input2,
                delete_row_id1,
            ),
        )
        conn.commit()
        continued()

    else:
        print("Bloga įvestis:")
        continued()
        update()


def main():
    while True:
        print("\n--- Šeimos finansai ---\n")
        print("0. Bendra išklotinė:\n")
        print("1. Įvesti įplaukas:")
        print("2. Įvesti išlaidas:\n")
        print("3. Gauti balansą:\n")
        print("4. Visos įplaukos:")
        print("5. Visos išlaidos:\n")
        print("6. Ištrinti įplaukas/Išlaidas:")
        print("7. Atnaujinti įplaukas/išlaidas:\n")
        print("8. Išeiti.\n")

        choice = input("Pasirinkite norimą veiksmą(Įveisti skaičių): \n")

        if choice == "0":
            table()
            continued()
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expenses()
        elif choice == "3":
            get_balance()
        elif choice == "4":
            print(f"Bendra įplaukų suma: {get_all_income()} Eu")
            continued()
        elif choice == "5":
            print(f"Bendra išlaidų suma: {get_all_expenses()}Eu")
            continued()
        elif choice == "6":
            delete()
        elif choice == "7":
            update()
        elif choice == "8":
            print("Gražios dienos!")
            break
        else:
            print("Bloga įvestis. Pasirinkite meniu skaičiu.")


if __name__ == "__main__":
    main()
