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
                acourse.student_doing_this_course.append(self)
                self.courses_enrolled.append(course)
                return f"Enrolled in {name} successfully"
        raise ValueError("Course not found")

    def view_courses(self):
        return self.courses_enrolled

    def to_dict(self):
        return {
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "courses_enrolled": [course.to_dict() for course in self.courses_enrolled]
        }

    @classmethod
    def from_dict(cls, data, school):
        student = cls(data["email"], data["password"], school)
        student.set_name(data["name"])
        student.courses_enrolled = [Course.from_dict(c) for c in data["courses_enrolled"]]
        return student