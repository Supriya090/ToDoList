class Persons:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(self.first_name)

class Student(Persons):
    def __init__(self, first, last, standard):
        super().__init__(first, last)
        self.standard = standard
    def print_name_with_std(self):
        print(self.first_name, self.last_name, " studies in ", self.standard )

class Teacher(Persons):
    def __init__(self, f_name, l_name, experience):
        super().__init__(f_name, l_name)
        self.experience = experience
    def teacher_id(self):
        print(self.first_name, self.last_name," has ",self.experience, " years of experience")

class Both(Student, Teacher):
    def __init__(self, fname, lname, stndrd, exp):
        super().__init__(first_name = fname, last_name = lname, standard = stndrd,experience = exp)
    def both_id(self):
        print(self.first_name, self.last_name, self.experience, self.standard)
p1 = Both("Supriya","Khadka",50,20)
#p1.print_name_with_std()
#p1.print_name()
p1.both_id()
