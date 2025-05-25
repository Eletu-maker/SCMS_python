class Course:
    def __init__(self):
        self.course = ""
        self.point = None
        self.student_doing_this_course = []
        self.grade = None


    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def getCourse(self):
        return self.course

    def setCourse(self,course):
        self.course = course

    def getPoint(self):
        return self.point

    def setPoint(self,point):
        self.point = point

    def get_student_doing_this_course(self):
        return self.student_doing_this_course


    def set_student_doing_this_course(self,student_doing_this_course):
        self.student_doing_this_course = student_doing_this_course


    def __eq__(self, other):
        if not isinstance(other, Course):
            return False
        return self.course == other.course and self.point == other.point


    def to_dict(self):
        return {
            "course": self.course,
            "point": self.point,
            "grade": self.grade,
            "student_doing_this_course": self.student_doing_this_course
        }

    @classmethod
    def from_dict(cls, data):
        course = cls()
        course.setCourse(data["course"])
        course.setPoint(data["point"])
        course.set_grade(data.get("grade", None))
        course.set_student_doing_this_course(data.get("student_doing_this_course"))
        return course
