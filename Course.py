class Course:
    def __init__(self):
        self.course = ""
        self.point = 0
        self.student_doing_this_course = []

    def getCourse(self):
        return self.course

    def setCourse(self,course):
        self.course = course

    def getPoint(self):
        return self.point

    def setPoint(self,point):
        self.point = point
