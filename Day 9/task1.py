student_scores = {
    "Alice": 85,
    "Ben": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88,
    "Fiona": 76,
    "George": 90,
    "Hannah": 82,
    "Ian": 79,
    "Julia": 94,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]

    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)