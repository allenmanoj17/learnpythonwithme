# print(len("hello"))
# print("hello"[4])

# my_name = "Allen Manoj"
# print(my_name[4] + my_name[7])

# num = len(input("Name?"))
# print(type(num))
# Output -> <class 'int'>

# print(str(len((input("Name?")))))

# num = len(input("Name?"))
# newnum = str(num)
# print("Your name has " + newnum + " charaters.")

# a = 123
# print(type(a))
# a = str(123)
# print(type(a))
# a = float(123)
# print(type(a))

# print(100 + float(120.3))
# Output 220.3

#print(str('33') + str('56'))
# Output 3356

# Input must be any two digit integer and the task is to find the sum of both the digit
# input = 23
# Output = 5
# ----- Solution ------
# value = input("Type a two digit number: ")
# firstDigit = value[0]
# secondDigit = value[1]
# sum = int(firstDigit) + int(secondDigit)
# print(sum)

# print(3 + 3)  Addition
# print(3 - 2)  Subtraction
# print(3 * 3)  Multiplication
# print(9 / 3)  Division
# print(3 ** 2) Exponential

# Order of priority - PEMDAS - calculation occurs from left to right
# print(3 + 4 / 2 - 1 + 5)
# Output - 9.0 --- The reason of floating value is because of the division

# BMI Calculator
# BMI = Weight/(Height)^2
# -----Solution-----
# weight = input("Enter your weight in Kg: ")
# height = input("Enter your height in m: ")
# bmi = float(weight) / float(height)**2
# print(int(bmi)) #Prints as whole number


# # Usage of f-String
# score = 0
# height = 1.8
# isWinning = True
# # Usual Method
# # print("Your score is " + str(score) + ", your height is " + str(height) + ", you are winning is " + str(isWinning))
# # f-String
# print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# Life in Weeks
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# ---- Solution -----
# currentAge = input("What is your age? ")
# intAge = int(currentAge)
# ageLeft = 90 - int(intAge)
# days =  ageLeft * 365
# weeks = ageLeft * 52
# months = ageLeft * 12
# print(f"You have {days} days, {weeks} weeks, {months} months, and {ageLeft} years left.")

# -- Tip Calculator --
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")

totalBill = float(input("What was the total bill? $"))
tipPercentage = int(input("What percentage tip would you like to give? "))
totalPeople = int(input("How many people to split the bill? "))

totalAmount = float((totalBill/totalPeople) * ((tipPercentage/100 )+ 1))
roundAmount = "{:.2f}".format(round(totalAmount,2))

print(f"Each person should pay ${roundAmount}")
