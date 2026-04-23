# Life in weeks

def calculate_life_in_weeks(age):
    weeks_left = (90 - age) * 52
    print(f"You have {weeks_left} weeks left until you turn 90.")

current_age = int(input("What is your current age? "))

calculate_life_in_weeks(current_age)