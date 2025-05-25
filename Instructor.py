from Course import Course
class Instructor:
    def __init__(self, email, password, school):
        self.email = email
        self.password = password
        self.school = school
        self.instructors_course = []
        self.name= ""


    def set_name(self, name):
        self.name = name

    def check_password(self, password):
        return password == self.password


    def create_course(self, name, point):
        course = Course()
        course.setCourse(name)
        course.setPoint(point)

        for acourse in self.school.get_courses():
            if acourse == course:
                raise ValueError("Course already exists")

        self.instructors_course.append(course)
        self.school.add_course(course)
        return f"{name} course created successfully"


    def get_student_doing_course(self, name, point):
        the_students = []
        course = Course()
        course.setCourse(name)
        course.setPoint(point)
        if self.__check_student_doing_course(name, point):
            for student in self.school.get_students():
                for acourse in student.get_courses_enrolled():
                    if acourse == course:
                        the_students.append(student)
            return the_students
        else:
            raise ValueError("Can't access course or doesn't exist")


    def __check_student_doing_course(self,name, point):
        course = Course()
        course.setCourse(name)
        course.setPoint(point)
        for acourse in self.instructors_course:
            if acourse == course:
                return True
        return False

    def score_student_in_course(self,course_name, point, name_of_student, grade):
        for student in self.get_student_doing_course(course_name,point):
            if student.name == name_of_student:
                for course in student.get_courses_enrolled():
                    if course.getCourse() == course_name:
                        course.set_grade(grade)



    def to_dict(self):
        return {
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "instructors_course": [course.to_dict() for course in self.instructors_course]
        }

    @classmethod
    def from_dict(cls, data, school):
        instructor = cls(data["email"], data["password"], school)
        instructor.set_name(data["name"])
        instructor.instructors_course = [Course.from_dict(c) for c in data["instructors_course"]]
        return instructor