class Human:
    def __init__(self, name, age, sex, alive):
        self.name = name
        self.age = age
        self.sex = sex
        self.alive = alive

    def walk(self):
        pass
    def eat(self):
        pass
    def sleep(self):
        pass

    def __str__(self):
        return f"{self.name}: age = {self.age};" \
               f" sex = {self.sex};" \
               f" alive = {self.alive}"