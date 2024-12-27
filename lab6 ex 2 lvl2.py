students = []
for _ in range(5):
    surname = input("Enter student's surname: ")
    math_grade = float(input("Enter math's mark: "))
    physics_grade = float(input("Enter physics' mark: "))
    russian_grade = float(input("Enter russian's mark: "))
    if math_grade == 2 or physics_grade == 2 or russian_grade == 2:
        print(f"{surname} expelled.")
        continue
    average_grade = (math_grade + physics_grade + russian_grade) / 3
    students.append({
        'surname': surname,
        'average_grade': average_grade
    })
students.sort(key=lambda x: x['average_grade'], reverse=True)
print("\nList of students who successfully passed the exams:")
print(f"{'Surname':<20} {'Average score':<15}")
for student in students:
    print(f"{student['surname']:<20} {student['average_grade']:<15.2f}")