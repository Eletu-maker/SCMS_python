from Course import Course
class Instructor:
    def __init__(self, email, password, school):
        self.email = email
        self.password = password
        self.school = school

    def check_password(self, password):
        return password == self.password


    def create_course(self, name, point):
        course = Course()
        course.setCourse(name)
        course.setPoint(point)

        if course in self.school.get_courses():
            raise ValueError("Course already exists")

        self.school.add_course(course)
