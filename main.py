import math

def convPoundToKilo(weight):
    return weight * 9 / 20

def convInchToMeter(height):
    return height / 40

def calculateBMI(weight, height):
    return round(convPoundToKilo(weight) / (convInchToMeter(height) ** 2), 1)

def categorizeBMI(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal weight"
    elif bmi >= 25 and bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def calcSavingsPerYear(salary, percentSaved):
    return salary * percentSaved * 1.35

def calcYearsToGoalMet(savedPerYear, goal):
    return math.ceil(goal / savedPerYear)

def isGoalMet(age, yearsToFinish):
    if (age + yearsToFinish) < 100:
        return True
    else:
        return False

# This code was found on github, it is used for getting correct input from the user.
def get_int_above_zero(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter an integer.")
            continue

        if value <= 0:
            print("Sorry, your response must be above zero.")
            continue
        else:
            break
    return value

def get_int_nonnegative(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter an integer.")
            continue

        if value < 0:
            print("Sorry, your response must be above zero.")
            continue
        else:
            break
    return value

def get_float_between_zero_and_one(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a float.")
            continue

        if value <= 0 or value >= 1:
            print("Sorry, your response must be above zero and below one.")
            continue
        else:
            break
    return value

def FinalCalculatorBMI():
    weight = get_int_above_zero("Enter the weight in pounds: ")
    feet = get_int_above_zero("Enter the number of feet in height: ")
    inches = get_int_nonnegative("Enter the number of inches in height: ")
    height = feet * 12 + inches
    bmi = calculateBMI(weight, height)
    category = categorizeBMI(bmi)
    print()
    print("Based on your inputs of " + str(weight) + " pounds and " + str(height) +
          " inches, the calculated BMI is " + str(bmi) + " which is categorized as "
          + str(category) + ".")

def FinalCalculatorRetirement():
    salary = get_int_above_zero("Enter your salary: ")
    percentSaved = get_float_between_zero_and_one("Enter the percent saved in decimal format: ")
    goal = get_int_above_zero("Enter your overall savings goal: ")
    age = get_int_above_zero("Enter your current age: ")
    savingsPerYear = calcSavingsPerYear(salary, percentSaved)
    years = calcYearsToGoalMet(savingsPerYear, goal)
    goalAchieved = isGoalMet(age, years)
    if goalAchieved:
        print()
        print("You will achieve your savings goal at the age of " + str((age + years)) + ".")
    else:
        print()
        print("You will not achieve your savings goal before the age of 100.")  

def chooseFunc():
    while True:
        try:
            choice = int(input("1. BMI Calculator\n2. Retirement Calculator\n3. End Application\nSelect a number to run the given app: "))
        except ValueError:
            print("Please choose an integer from the selection of [1, 2, 3]")
            continue
        if choice == 1:
            FinalCalculatorBMI()
            print()
            chooseFunc()
            break
        elif choice == 2:
            FinalCalculatorRetirement()
            print()
            chooseFunc()
            break
        elif choice == 3:
            break
        else:
            print("Please choose a valid option.\n")

def main():
    chooseFunc()

if __name__ == "__main__":
    main()
            
    
