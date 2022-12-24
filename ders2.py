class Emp(object):
    age = 25
    salary = 1000  # $

    def ageSalaryRatio(self):
        print("ratio: ", int(self.salary / self.age))


e1 = Emp()
e1.ageSalaryRatio()


# %% initializer or contractor

class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def getName(self):
        print(self.name)


a1 = Animal("cat", 2)
a1.getName()

