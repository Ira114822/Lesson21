from student import Student


class Leader(Student):
    def __init__(self, name, age, sex, mark, alive, phone, email):
        self.name = name
        self.age = age
        self.sex = sex
        self.mark = mark
        self.alive = alive
        self.phone = phone
        self.email = email

    def responsibility(self):
        pass

    def __str__(self):
        return f"{self.name}: age = {self.age};" \
               f" sex = {self.sex};" \
               f" mark = {self.mark};" \
               f" alive = {self.alive};" \
               f" phone = {self.phone};" \
               f" email = {self.email}"