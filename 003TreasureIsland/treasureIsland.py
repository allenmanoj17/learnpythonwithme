# # Roller Coaster 
# print("Welcome to the Rollercoaster ride.")
# # Get the height
# height = int(input("Enter your height in cm: "))
# # Check the condition
# if height >= 120:
#     print("Proceed")
# else:
#     print("Please grow taller and then you can ride.")



# # Odd or Even 
# number = int(input("Enter the number you want to check: "))
# if (number % 2) == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# # Nested if & elif and multiple if
# #################################################
# # Roller Coaster 2.0
# print("Welcome to the Rollercoaster ride.")
# bill = 0
# # Get the height
# height = int(input("Enter your height in cm: "))
# # Check the condition
# if height >= 120:
#     print("Proceed")
#     age = int(input("Enter your age: "))
#     if age < 12:
#         bill = 5
#         print("Child ticket - $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets - $7.")
#     else:
#         bill = 12
#         print("Adult tickets - $12.")
#     photo = input("Do you want photos? (1/0) ")
#     if photo == 1:
#         bill += 3
#     print(bill)
# else:
#     print("Please grow taller and then you can ride.")



# # BMI Calculator 2.0 
# # It should tell them the interpretation of their BMI based on the BMI value.
# # Under 18.5 they are underweight
# # Over 18.5 but below 25 they have a normal weight
# # Over 25 but below 30 they are slightly overweight
# # Over 30 but below 35 they are obese
# # Above 35 they are clinically obese.


# weight = float(input("Enter your weight in Kg: "))
# height = float(input("Enter your height in m: "))
# bmi = round(weight / (height ** 2))
# print("Your BMI is: " + str(bmi)) 

# if bmi < 18.5:
#     print("You're Underweight")
# elif bmi < 25:
#     print("You've a normal weight")
# elif bmi < 30:
#     print("You've slightly overweight")
# elif bmi < 35:
#     print("You're obese")
# else:
#     print("clinically obese")
# print("Thank you for using BMI 2.0")


# # Leap Year
# # This is how you work out whether if a particular year is a leap year.
# # on every year that is evenly divisible by 4 
# # except every year that is evenly divisible by 100 
# # unless the year is also evenly divisible by 400
# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not a leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not a leap year.")


# Pizza Order
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill =+ 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")