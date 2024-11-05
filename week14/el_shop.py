import datetime

from sqlalchemy import Column, Date, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///employees.db")
Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    surname = Column("surname", String)
    birthdate = Column("birthdate", Date)
    position = Column("position", String)
    salary = Column("salary", Float)
    start_date = Column("start_date", Date, default=datetime.date.today)

    def __repr__(self):
        return (
            f"ID: {self.id}, Vardas: {self.name} {self.surname}, Gimimo data: "
            f"{self.birthdate}, Pareigos: {self.position}, Atlyginimas: $"
            f"{self.salary:.2f}, Įsidarbinimo data: {self.start_date}"
        )


def create_employee(name, surname, birthdate, position, salary, start_date=None):
    birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()

    if start_date:
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    else:
        start_date = datetime.date.today()

    new_employee = Employee(
        name=name,
        surname=surname,
        birthdate=birthdate,
        position=position,
        salary=salary,
        start_date=start_date,
    )
    session.add(new_employee)
    session.commit()
    print(f"Darbuotojas {name} {surname} sėkmingai pridėtas su įsidarbinimo data " f"{start_date}.")


def read_all_employees():
    employees = session.query(Employee).all()
    if employees:
        for emp in employees:
            print(emp)
    else:
        print("Darbuotojų nerasta.")


def update_employee(emp_id, **kwargs):
    employee = session.query(Employee).filter(Employee.id == emp_id).first()
    if employee:
        for key, value in kwargs.items():
            if hasattr(employee, key):
                setattr(employee, key, value)
        session.commit()
        print(f"Darbuotojas ID {emp_id} sėkmingai atnaujintas.")
    else:
        print(f"Darbuotojo ID {emp_id} nerasta.")


def delete_employee(emp_id):
    employee = session.query(Employee).filter(Employee.id == emp_id).first()
    if employee:
        session.delete(employee)
        session.commit()
        print(f"Darbuotojas ID {emp_id} sėkmingai ištrintas.")
    else:
        print(f"Darbuotojo ID {emp_id} nerasta.")


def main():
    while True:
        print(
            "\n"
            "Parinktys:\n"
            "1. Pridėti darbuotoją\n"
            "2. Peržiūrėti visus darbuotojus\n"
            "3. Atnaujinti darbuotoją\n"
            "4. Ištrinti darbuotoją\n"
            "5. Išeiti"
        )

        choice = int(input("Įveskite savo pasirinkimą: "))

        match choice:
            case 1:
                name = input("Įveskite darbuotojo vardą: ")
                surname = input("Įveskite darbuotojo pavardę: ")
                birthdate = input("Įveskite darbuotojo gimimo datą (YYYY-MM-DD): ")
                position = input("Įveskite darbuotojo pareigas: ")
                salary = float(input("Įveskite darbuotojo atlyginimą: "))
                start_date = input(
                    "Įveskite darbuotojo įsidarbinimo datą (YYYY-MM-DD) arba "
                    "paspauskite ENTER, kad naudotumėte šiandienos datą: "
                )

                if start_date == "":
                    start_date = None

                create_employee(name, surname, birthdate, position, salary, start_date)
            case 2:
                read_all_employees()
            case 3:
                emp_id = int(input("Įveskite darbuotojo ID, kurį norite atnaujinti: "))
                updates = {}
                name = input("Įveskite naują vardą (arba ENTER, kad praleisti): ")
                surname = input("Įveskite naują pavardę (arba ENTER, kad praleisti): ")
                position = input("Įveskite naujas pareigas (arba ENTER, kad praleisti): ")
                salary = input("Įveskite naują atlyginimą (arba ENTER, kad praleisti): ")
                if name:
                    updates["name"] = name
                if surname:
                    updates["surname"] = surname
                if position:
                    updates["position"] = position
                if salary:
                    updates["salary"] = float(salary)
                update_employee(emp_id, **updates)
            case 4:
                emp_id = int(input("Įveskite darbuotojo ID, kurį norite ištrinti: "))
                delete_employee(emp_id)
            case 5:
                print("Viso gero!")
                break
            case _:
                print("Neteisinga parinktis. Bandykite dar kartą.")


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    main()

    session.close()
