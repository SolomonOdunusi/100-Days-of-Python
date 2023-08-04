#Calculate for the percentage tip of bills

greet = "We appreciate your tip!!!"
print(greet)

bill = input("What is your total bill: ")
tip = input("What percentage will you be tipping? 10%, 12% or 15%: ")
num_people = input("Among how many people will the bill be split: ")

tip_percent = float(tip) / 100
main_tip = tip_percent * float(bill)
total_bill = main_tip + float(bill)
split_bill = total_bill / float(num_people)
final = round(split_bill, 4)


result = f"Each person will pay: ${final}"
print(result)

# Output
# We appreciate your tip!!!
# What is your total bill: 5354
# What percentage will you be tipping? 10%, 12% or 15%: 15
# Among how many people will the bill be split: 11
# Each person will pay: $559.73