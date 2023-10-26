class Student:
    def __init__(self, name=None, age=None, grades=None, schoolClass=None):
        self.schoolClass = schoolClass
        self.name = name
        self.age = age
        self.grades = grades or []

    def set_class(self, schoolClass):
        self.schoolClass = schoolClass

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        else:
            return sum(self.grades) / len(self.grades)
    
KadenFrisk = Student("KadenFrisk", 15, [100,90,89,100,99], "Math")
print(str(KadenFrisk.get_average_grade()))