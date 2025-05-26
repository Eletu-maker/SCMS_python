from School import School



def main():
    school =  School.load_from_file() or School()
    stud = school.students
    inst = school.instructors
    while True:
        try:
            print(""""
                Which role are you:
               1. Student
               2. Instructor
               3. Exit
                   """)

            role = input("Enter your choice: ")
            if role == '1':
                print(""" Student
                            1. Register
                            2. login
                                """)
                student_choice = input("Enter your choice: ")
                if student_choice == "1":
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    print(stud.register_student(email, password))

                if student_choice == "2":
                    try:
                        email = input("Enter your email: ")
                        password = input("Enter your password: ")
                        student_logedin= stud.login(email, password)
                        print("You are logged in")
                        while True:
                            print("""
                            What do you want to do?
                            1. Enroll for a course
                            2. view all courses enrolled in
                            3. Score student doing a course
                            4. log out
                            """)
                            student_activity = input("Enter your choice: ")
                            if student_activity == "1":
                                student_course_name = input("Enter your course name: ")
                                student_course_point = input("Enter your course point: ")
                                print( student_logedin.enroll_course(student_course_name, student_course_point))

                            if student_activity == "2":
                                for course in student_logedin.courses:
                                    print(course.to_dict())

                            if student_activity == "4":
                                break



                    except ValueError as e:
                        print(e)
                        break





            if role == '2':
                print(""" Instructor
                                1. Register
                                2. login
                                    """)
                instructor_choice = input("Enter your choice: ")
                if instructor_choice == "1":
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    print(inst.register_instructor(email, password))

                if instructor_choice == "2":
                    try:
                        email = input("Enter your email: ")
                        password = input("Enter your password: ")
                        instructor_logedin = inst.login(email, password)
                        print("You are logged in")

                        while True:
                            print("""
                            What do you want to do?
                            1. Create a course
                            2. Get Student doing a course
                            3. Score student doing a course
                            4. log out
                            """)
                            instructor_activity = input("Enter your choice: ")
                            if instructor_activity == "1":
                                course_name = input("Enter your course name: ")
                                course_point = input("Enter your course point: ")
                                print( instructor_logedin.create_course(course_name, course_point))

                            if instructor_activity == "4":
                                break





                    except ValueError as e:
                        print(e)






            if role == '3':
                print("bye")
                break

            if role not in ["1", "2", "3"]:
                print("Invalid choice")

        except ValueError as e:
            print(e)
        school.save_to_file()






if __name__ == "__main__":
    main()