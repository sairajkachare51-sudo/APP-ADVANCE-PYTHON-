
Marks = int(input("Enter marks of student: "))
Total_Marks = int(input("Enter total marks: "))

Percentage = (Marks / Total_Marks) * 100

print("Percentage =", Percentage)

if Percentage >= 90:
    print("Student has O grade")
elif Percentage >= 80:
    print("Student has A+ grade")
elif Percentage >= 70:
    print("Student has B+ grade")
elif Percentage >= 50:
    print("Student is PASS only")
else:
    print("Student is FAILED")