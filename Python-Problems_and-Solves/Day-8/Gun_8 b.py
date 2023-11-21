def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Please enter valid values for weight and height.")
    else:
        bmi = calculate_bmi(weight, height)
        category = determine_bmi_category(bmi)
        print(f"Your BMI is {bmi:.2f}, which falls into the category: {category}")

except ValueError:
    print("Please enter valid numeric values for weight and height.")
