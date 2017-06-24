class Employer:
    def __init__(self, name, age,position):
        self.name = name
        self.age = age
        self.position = position

    def double_age(self):
        return self.age * 2

emp1=Employer("Somchai",35,"Manager")
emp2=Employer("Boonchoo",25,"Programer")
print(emp1.name)
print(emp1.age)
print(emp1.double_age())
print(emp2.position)
