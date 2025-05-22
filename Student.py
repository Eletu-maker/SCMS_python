from Course import Course
class Student:
    def __init__(self, email, password, school):
        self.email = email
        self.password = password
        self.school = school
        self.courses_enrolled = []
        self.name = ""

    def set_name(self, name):
        self.name = name



    def check_password(self, password):
        return password == self.password

    def get_courses_enrolled(self):
        return self.courses_enrolled


    def enroll_course(self, name, point):
        course = Course()
        course.setCourse(name)
        course.setPoint(point)
        for acourse in self.school.get_courses():
            if acourse == course:
                if course in self.courses_enrolled:
                    raise ValueError("Already enrolled")
                return self.courses_enrolled.append(course)

        raise ValueError("Course not found")

    def view_courses(self):
        return self.courses_enrolled