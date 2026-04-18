# BMI Calculator with Interpretations

# Get user input for weight and height

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
# Calculate BMI
bmi = weight / (height ** 2)
# Interpret BMI
if bmi < 18.5:
    interpretation = "Underweight"
elif 18.5 <= bmi < 25:
    interpretation = "Normal weight"
elif 25 <= bmi < 30:
    interpretation = "Overweight"
else:
    interpretation = "Obese"

# Print the result
print(f"Your BMI is: {bmi:.2f}. You are classified as: {interpretation}.")

