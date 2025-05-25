import json
from Students import Students
from Instructors import Instructors
from Student import Student
from Course import Course
from Instructor import Instructor
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

    def save_to_file(self, filename="school_data.json"):
        try:
            data = {
                "students": [s.to_dict() for s in self.get_students()],
                "instructors": [i.to_dict() for i in self.get_instructors()],
                "courses": [c.to_dict() for c in self.get_courses()]
            }
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"File write error: {e}")
        except TypeError as e:
            print(f"Serialization error: {e}")

    @classmethod
    def load_from_file(cls, filename="school_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                school = cls()
                school.courses = [Course.from_dict(c) for c in data["courses"]]
                school._students_list = [Student.from_dict(s, school) for s in data["students"]]
                school._instructor_list = [Instructor.from_dict(i, school) for i in data["instructors"]]
                return school
        except FileNotFoundError:
            print("The file was not found.")
        except json.JSONDecodeError:
            print("The file contains invalid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
