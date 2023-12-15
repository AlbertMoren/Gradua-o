'''Make a program that fills an array with the names of seven students and loads another array with their final grades. Calculate and show:
 ■ the name of the student with the highest average (disregard ties);
 ■ for each student who didn't pass, that is, with an average lower than 7, show how much they need to score on the final exam to pass. Consider that the passing grade for the exam is 5.
'''
# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

students = []
grades = [0] * 7
highest = [0] * 2

for i in range(len(grades)):
    student_name = input("Student's Name: ")

    if student_name in students:
        flag = 1
        while flag == 1:
            student_name = input("Incorrect value. Name already exists in our database. Please enter another: ")
            if student_name not in students:
                flag = 0
    students.append(student_name)
    grades[i] = float(input("Enter this student's grade: "))  # Section responsible for getting the highest grade

    if grades[i] > highest[0]:
        highest[0] = grades[i]
        highest[1] = i

print(f"The student {students[highest[1]]} achieved the highest average, {highest[0]:.2f}\n")
for i in range(len(grades)):
    if grades[i] < 7 and grades[i] >= 4:
        print(f"The student {students[i]} needs to score {10 - grades[i]:.2f} to pass")
