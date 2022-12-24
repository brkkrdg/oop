employee1_name = "messi"
employee1_age = 33
employee1_address = "badasses"


class Employee(object):
    # attribute = age, address, name
    # behaviour = pass
    pass


employee1 = Employee()


# %% attribute

class Football:
    football_club = "Barcelona"
    age = 30


f1 = Football()
f1.football_club = "Real Madrid"
print(f1.football_club)


# %% methods

class Square(object):
    edge = 5  # meter
    area = 0

    def Area(self):
        self.area = self.edge * self.edge
        print("area: ", self.area)


s1 = Square()
s1.edge = 7
s1.Area()

