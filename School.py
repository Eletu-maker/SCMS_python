from Students import Students
from Instructors import Instructors
class School:
    def __init__(self):

        self._students_list = []
        self.courses = []
        self.students = Students(self)
        self.instructors = Instructors(self)
        self._instructor_list = []

    def get_courses(self):
        return self.courses



    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student):
        if student not in self._students_list:
            self._students_list.append(student)

    def get_students(self):
        return self._students_list


    def add_instructor(self, instructor):
        if instructor not in self._instructor_list:
            self._instructor_list.append(instructor)

    def get_instructors(self):
        return self._instructor_list
