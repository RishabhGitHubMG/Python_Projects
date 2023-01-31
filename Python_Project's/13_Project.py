# Pizza Order Practice
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
    bill += 25
sum1 = size
if add_pepperoni == "Y":
    if add_pepperoni == "S":
        bill += 2
    elif add_pepperoni == "M":
        bill += 3
    else: 
        bill += 3
sum2 = add_pepperoni
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")