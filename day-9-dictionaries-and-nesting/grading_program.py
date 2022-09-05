student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_scores[key] = "Outstanding"
        student_grades[key] = student_scores[key]
    elif student_scores[key] > 80:
        student_scores[key] = "Exceeds Expectations"
        student_grades[key] = student_scores[key]
    elif student_scores[key] > 70:
        student_scores[key] = "Acceptable"
        student_grades[key] = student_scores[key]
    else:
        student_scores[key] = "Fail"
        student_grades[key] = student_scores[key]

print(student_grades)
