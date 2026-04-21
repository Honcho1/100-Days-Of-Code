# Find the highest number in a list of numbers.

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 57, 99, 92, 100, 102, 110, 111, 115, 109, 105, 120, 122, 130, 128, 132, 135, 140, 138, 142, 145, 150]

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
