from human import Human
from marknote import MarkNote

class Student(Human):
    def __init__(self, name, age, sex, marknote, alive):
        self.name = name
        self.age = age
        self.sex = sex
        if isinstance(marknote, MarkNote):
            self.note = marknote
        else:
            self.note = MarkNote()

        self.note.add(mark)
        self.alive = alive

    def study(self):
        pass

    def add(self, mark):
        self.note.add(mark)

    def __str__(self):
        return f"{self.name}: age = {self.age};" \
               f" sex = {self.sex};" \
               f" mark = {self.mark};" \
               f" alive = {self.alive}"