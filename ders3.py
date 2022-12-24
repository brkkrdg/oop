# calculator project
class calculator(object):
    # init method
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b

    def add(self):
        # "addition a+b= result -> return result"
        return self.value1 + self.value2

    def multiply(self):
        # "multiplication a*b =result -> return result"
        return self.value1 * self.value2

    def division(self):
        return self.value1 / self.value2


selection = int(input("select 1 or 2 or 3: "))

v1 = int(input("first value:"))
v2 = int(input("second value:"))

c1 = calculator(v1, v2)
if selection == 1:
    multiply_result = c1.multiply()
    print("Multiply result:", multiply_result)
elif selection == 2:
    division_result = c1.division()
    print("Division result:", division_result)
elif selection == 3:
    add_result = c1.add()
    print("Add result:", add_result)
else:
    print("Error there is no proper selection")
