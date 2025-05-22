from Student import Student

class Students:
    def __init__(self, school):
        self.school = school

    def register_student(self, email, password):
        if self.__check_student(email):
            raise ValueError("User already registered")
        stud = Student(email, password, self.school)
        self.school.add_student(stud)

    def __check_student(self, email):
        check = False
        for s in self.school.get_students():
            if s.email == email:
                check = True
        for instructor in self.school.get_instructors():
            if instructor.email == email:
                check = True
        return check

    def login(self, email, password):
        if self.__check_student(email):
            for s in self.school.get_students():
                if s.email == email and s.check_password(password):
                    return s
            raise ValueError("Wrong password")
        else:
            raise ValueError("Student does not exist")
