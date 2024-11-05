from sqlalchemy.orm import sessionmaker

from models import engine, Person, Bank, Account

Session = sessionmaker(bind=engine)
session = Session()

while True:
    print(
        "\nMeniu:\n1. Prideti vartotoja\n2. Prideti banka\n3. Prideti saskaita\n4. Prideti pajamas / islaidas\n5. Perziureti vartotojus\n6. Perziureti bankus\n7. Perziureti saskaitas\n8. Gauti vartotojo saskaitas\n9. Iseiti"
    )
    choice = int(input("Iveskite savo pasirinkima: "))
    if choice == 1:
        name = input("Iveskite varda: ")
        surname = input("Iveskite pavarde: ")
        social_no = input("Iveskite soc. draudimo numeri: ")
        phone_no = input("Iveskite telefono numeri: ")
        person = Person(name=name, surname=surname, social_security_no=social_no, phone_no=phone_no)
        session.add(person)
        session.commit()
        print("Vartotojas sukurtas!")
    elif choice == 2:
        name = input("Iveskite pavadinima: ")
        address = input("Iveskite adresa: ")
        swift_code = input("Iveskite swift koda: ")
        bank = Bank(name=name, address=address, swift_code=swift_code)
        session.add(bank)
        session.commit()
        print("Bankas sukurtas!")
    elif choice == 3:
        iban_no = input("Iveskite saskaitos numeri: ")
        balance = 0

        banks = session.query(Bank).all()
        for bank in banks:
            print(f"ID: {bank.id} | Name: {bank.name} | Address: {bank.address}")
        bank_id = int(input("Iveskite banko id: "))

        people = session.query(Person).all()
        for person in people:
            print(f"ID: {person.id} | Name: {person.name} | Surname: {person.surname}")
        person_id = int(input("Iveskite zmogaus id: "))
        account = Account(iban_no=iban_no, balance=balance, bank_id=bank_id, person_id=person_id)
        session.add(account)
        session.commit()
        print("Saskaita sukurta!")
    elif choice == 4:
        accounts = session.query(Account).all()
        for account in accounts:
            print(
                f"ID: {account.id} | IBAN: {account.iban_no} | Balance: {account.balance} | Bank name: {account.bank.name}"
            )
        account_id = int(input("Pasirinkite saskaitos ID: "))
        amount = float(input("Iveskite islaidas/pajamas: "))

        selected_account = session.get(Account, account_id)
        selected_account.balance += amount
        session.commit()
        print("Balansas atnaujintas!")
    elif choice == 5:
        people = session.query(Person).all()
        for person in people:
            print(f"ID: {person.id} | Name: {person.name} | Surname: {person.surname}")
    elif choice == 6:
        banks = session.query(Bank).all()
        for bank in banks:
            print(f"ID: {bank.id} | Name: {bank.name} | Address: {bank.address}")
    elif choice == 7:
        accounts = session.query(Account).all()
        for account in accounts:
            print(
                f"ID: {account.id} | IBAN: {account.iban_no} | Balance: {account.balance} | Bank name: {account.bank.name}"
            )
    elif choice == 8:
        people = session.query(Person).all()
        for person in people:
            print(f"ID: {person.id} | Name: {person.name} | Surname: {person.surname}")
        person_id = int(input("Pasirinkite vartotojo ID: "))
        accounts = session.query(Account).filter_by(person_id=person_id).first()
        for account in accounts:
            print(
                f"ID: {account.id} | IBAN: {account.iban_no} | Balance: {account.balance} | Bank name: {account.bank.name}"
            )
    elif choice == 9:
        break
    else:
        print("Nera tokio pasirinkimo!")
