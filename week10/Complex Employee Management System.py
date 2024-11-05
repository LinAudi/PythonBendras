class Employee:

    raise_amt = 1.05
    def __init__(self,name: str, id: int, salary: float):
        self.name = name
        self.id = id
        self._salary = salary

    # def give_raise(self):
    #     self._salary = self._salary * self.give_raise_amt
    #
    # @classmethod
    # def set_raise_amt(cls, amount):
    #     cls.raise_amt = amount

class Manager(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id, salary)
        self.subordinates = []

    def add_subordinate(self, emp):
        self.subordinates.append(emp)

    def remove_subordinate(self,emp_id):

        self.subordinates = [emp for emp in self.subordinates if emp.id != emp_id]



employee1 = Employee("Alice", 101, 50000)
employee2 = Employee("Bob", 102, 55000)
employee3 = Employee("Mick", 108, 50000)
employee4 = Employee("John", 152, 55000)

mgr = Manager("Charlie", 201, 80000)

mgr.add_subordinate(employee1)
mgr.add_subordinate(employee2)
mgr.add_subordinate(employee3)
mgr.add_subordinate(employee4)

print([emp.name for emp in mgr.subordinates])

mgr.remove_subordinate(101)
mgr.remove_subordinate(152)


print([emp.name for emp in mgr.subordinates])