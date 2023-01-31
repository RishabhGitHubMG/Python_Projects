# Project: Tip Calculator
print("Welcome to the tip Calculator")
bill= float(input("What was the total bill?\n"))
tip = int(input("What pearscantage tip would you like to give? 10, 12 or 15\n"))
people = int(input("How many peopls to split the bill\n"))
# b = float(bill)
# t = int(tip)
# p = int(people)
# if 10:
#     sum = bill * 1.10
# elif 12:
#     sum = bill * 1.12
# elif 15 :
#     sum = bill * 1.15

tip_as_persantage = tip / 100
total_tip_amount = bill * tip_as_persantage
total_bill = bill + total_tip_amount

sum_1 = total_bill / people

ANS = round(sum_1, 2)

print(f"Each pearchen should pay {ANS}")
