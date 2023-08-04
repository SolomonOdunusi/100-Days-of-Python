# Body Mass Index Program

height =  input("Please input your height in metres: ")
weight =  input("Please input your weight in kilogram: ")

height_sqr = float(height) ** 2

bmi = int(weight) / height_sqr

print("Your Body Mass Index is ", int(bmi))

#Equation for BMI
# BMI = weight(kg) / height**2(m)

print("===============================================")
# I am creating a program that calculates the number of days,
# weeks and month left in the of a person 
# who lives up to the age of 90 years

greeting = print("Welcome to my Program")

age = input("What is your age? ")

diff_age = 90 - int(age)

days = diff_age * 365
weeks = diff_age * 52
months = diff_age * 12

print(f"You have {days} days, {weeks} weeks and {months} months left till the age of 90")










