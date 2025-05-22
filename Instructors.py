from Instructor import Instructor
class Instructors:
    def __init__(self,school):
        self.school = school

    def register_instructor(self, email, password):
        if self.__check_instructor(email):
            raise ValueError("Instructor already registered")
        stud = Instructor(email, password, self.school)
        self.school.add_instructor(stud)

    def __check_instructor(self, email):
        for instructor in self.school.get_instructors():
            if instructor.email == email:
                return True
        return False



    def login(self, email, password):
        if self.__check_instructor(email):
            for instructor in self.school.get_instructors():
                if instructor.email == email and instructor.check_password(password):
                    return instructor
            raise ValueError("wrong password")
        else:
            raise ValueError("Instructor do not exist")