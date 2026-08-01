student_name = input("Enter the student's name :")
student_marks = {'alice':98,'john':90,'sai':100,'peter':99}

if student_name in student_marks :
    print(f"{student_name}: {student_marks[student_name]}")
else : 
    print("Student not found.")


