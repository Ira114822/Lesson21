class MarkNote:
    def __init__(self):
        self._marks = []


    def __add__(self, mark):
        self._marks.append(mark)

    def get(self, index):
        return self._marks[index]

    def size(self):
        return  len(self._marks)

marknote = MarkNote()

marknote.add(5)
marknote.add(8)
marknote.add(9)
marknote.add(10)
marknote.add(5)

for index in