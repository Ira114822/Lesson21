from human import Human


class Worker(Human):
    def __init__(self, name, age, sex, alive, salary):
        self.name = name
        self.age = age
        self.sex = sex
        self.alive = alive
        self.salary = salary

    def work(self):
        pass

    def __str__(self):
        return f"{self.name}: age = {self.age};" \
               f" sex = {self.sex};" \
               f" salary = {self.salary};" \
               f" alive = {self.alive}"