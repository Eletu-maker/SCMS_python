import unittest

from School import *


class MyTestCase(unittest.TestCase):
    def test_that_student_can_be_register(self):
        school = School()
        stud = school.students

        stud.register_student("ydfuv@gmail.com","6356")


        self.assertEqual(1,len(school.get_students()))


    def test_that_student_can_be_register_twice_with_the_same_email(self):
        school = School()
        stud = school.students
        stud.register_student("ydfuv@gmail.com","6356")
        with self.assertRaises(ValueError) as context:
            stud.register_student("ydfuv@gmail.com","6356")

        self.assertEqual("Student already registered", str(context.exception))
        self.assertEqual(1, len(school.get_students()))

    def test_that_student_can_login(self):
        school = School()
        stud = school.students
        stud.register_student("ydfuv@gmail.com","6356")
        stud.register_student("magic@gmail.com","6356")
        lis=school.get_students()
        self.assertEqual(lis[1],stud.login("magic@gmail.com","6356"))

    def test_Wrong_password(self):
        school = School()
        stud = school.students
        stud.register_student("ydfuv@gmail.com", "6356")
        stud.register_student("magic@gmail.com", "6356")

        with self.assertRaises(ValueError) as context:
            stud.login("magic@gmail.com","6376")

        self.assertEqual("Wrong password", str(context.exception))

    def test_acc_do_not_exist(self):
        school = School()
        stud = school.students
        stud.register_student("ydfuv@gmail.com", "6356")
        stud.register_student("magic@gmail.com", "6356")
        lis = school.get_students()
        with self.assertRaises(ValueError) as context:
            stud.login("wryu@gmail.com", "6376")


        self.assertEqual("Student does not exist", str(context.exception))

    def test_that_instructor_can_be_register(self):
        school = School()
        stud = school.instructors

        stud.register_instructor("ydfuv@gmail.com", "6356")

        self.assertEqual(1, len(school.get_instructors()))  # add assertion here

    def test_that_instructor_can_be_register_twice_with_the_same_email(self):
        school = School()
        stud = school.instructors
        stud.register_instructor("ydfuv@gmail.com", "6356")
        with self.assertRaises(ValueError) as context:
            stud.register_instructor("ydfuv@gmail.com", "6356")

        self.assertEqual("Instructor already registered", str(context.exception))
        self.assertEqual(1,len(school.get_instructors()))

    def test_that_instructor_can_login(self):
        school = School()
        stud = school.instructors
        stud.register_instructor("ydfuv@gmail.com", "6356")
        stud.register_instructor("magic@gmail.com", "6356")
        lis = school.get_instructors()
        self.assertEqual(lis[1], stud.login("magic@gmail.com", "6356"))

    def test_Wrong_password_for_instructor(self):
        school = School()
        stud = school.instructors
        stud.register_instructor("ydfuv@gmail.com", "6356")
        stud.register_instructor("magic@gmail.com", "6356")
        with self.assertRaises(ValueError) as context:
            stud.login("magic@gmail.com", "6376")

        self.assertEqual("wrong password", str(context.exception))

    def test_acc_do_not_existfor_instructor(self):
        school = School()
        stud = school.instructors
        stud.register_instructor("ydfuv@gmail.com", "6356")
        stud.register_instructor("magic@gmail.com", "6356")
        with self.assertRaises(ValueError) as context:
            stud.login("wryu@gmail.com", "6376")

        self.assertEqual("Instructor do not exist", str(context.exception))



    def test_that_instructor_can_create_course(self):
        school = School()
        stud = school.instructors
        stud.register_instructor("magic@gmail.com", "6356")
        inst = stud.login("magic@gmail.com", "6356")
        inst.create_course("python",4)
        self.assertEqual(1,len(school.get_courses()))



    def test_that_instructor_can_create_more_course(self):
        school = School()
        stud = school.instructors
        stud.register_instructor("magic@gmail.com", "6356")
        inst = stud.login("magic@gmail.com", "6356")
        inst.create_course("python",4)
        inst.create_course("java", 4)
        self.assertEqual(2,len(school.get_courses()))


    def test_that_student_can_enroll_course(self):
        school = School()
        instructor = school.instructors
        instructor.register_instructor("magic@gmail.com", "6356")
        inst = instructor.login("magic@gmail.com", "6356")
        inst.create_course("python", 4)
        student = school.students
        student.register_student("ydfuv@gmail.com", "6356")
        stud = student.login("ydfuv@gmail.com", "6356")
        stud.enroll_course("python",4)

        self.assertEqual(1,len(stud.get_courses_enrolled()))

    def test_that_student_can_enroll_more_course(self):
        school = School()
        instructor = school.instructors
        instructor.register_instructor("magic@gmail.com", "6356")
        inst = instructor.login("magic@gmail.com", "6356")
        inst.create_course("python", 4)
        inst.create_course("java", 4)
        student = school.students
        student.register_student("ydfuv@gmail.com", "6356")
        stud = student.login("ydfuv@gmail.com", "6356")
        stud.enroll_course("python", 4)
        stud.enroll_course("java", 4)

        self.assertEqual(2, len(stud.get_courses_enrolled()))


if __name__ == '__main__':
    unittest.main()
