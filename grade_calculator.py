Students_name = input("Enter the student's name: ")
Marks_Bangla = float(input("Enter the marks obtained in Bangla: "))
Marks_English = float(input("Enter the marks obtained in English: "))
Marks_Math = float(input("Enter the marks obtained in Math: "))

if (Marks_Bangla < 0 or Marks_Bangla > 100 or
        Marks_English < 0 or Marks_English > 100 or
        Marks_Math < 0 or Marks_Math > 100):
    print("Invalid marks! Each subject mark must be between 0 and 100.")
else:
    average_marks = (Marks_Bangla + Marks_English + Marks_Math) / 3

    if average_marks >= 80 and average_marks <= 100:
        grade = "A+"
    elif average_marks >= 70 and average_marks < 79:
        grade = "A"
    elif average_marks >= 60 and average_marks < 69:
        grade = "A-"
    elif average_marks >= 50 and average_marks < 59:
        grade = "B"
    elif average_marks >= 40 and average_marks < 49:
        grade = "C"
    else:
        grade = "F"

    print("Student's name:", Students_name)
    print("Average marks:", round(average_marks, 2))
    print("Final grade:", grade)