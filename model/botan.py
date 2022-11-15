from student import Student


class Botan(Student):
    def __init__(self, name, age, sex, mark, alive, power):
        self.name = name
        self.age = age
        self.sex = sex
        self.mark = mark
        self.alive = alive
        self.power = power

    def learn_hard(self):
        pass

    def __str__(self):
        return f"{self.name}: age = {self.age};" \
               f" sex = {self.sex};" \
               f" mark = {self.mark};" \
               f" alive = {self.alive};" \
               f" power = {self.power}"