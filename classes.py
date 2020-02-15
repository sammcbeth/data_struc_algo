class Student:
    def __init__(self, firstName, lstName, year):
        self.firstName = firstName
        self.lstName = lstName
        self.year = year

    def __repr__(self):
        return f'Hi my name is {self.firstName} {self.lstName} and i graduated in {self.year}.'


sam = Student('Sam', 'Mcbeth', 2018)
print(sam)