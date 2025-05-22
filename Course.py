class Course:
    def __init__(self):
        self.course = ""
        self.point = 0
        self.student_doing_this_course = []
        self.grade =0


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


    def __eq__(self, other):
        if not isinstance(other, Course):
            return False
        return self.course == other.course and self.point == other.point and self.student_doing_this_course == other.student_doing_this_course

