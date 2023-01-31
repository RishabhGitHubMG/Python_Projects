#  Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_sum = name1 + name2

name_sum = name_sum.lower()
name_sum = name_sum.lower()

t = name_sum.count("t")
r = name_sum.count("r")
u = name_sum.count("u")
e = name_sum.count("e")
true = t + r + u + e
l = name_sum.count("l")
o = name_sum.count("o")
v = name_sum.count("v")
e = name_sum.count("e")
love = l + o + v + e

love_sum = str(true) + str(love)

love_sum1 = int(love_sum)

if (love_sum1 < 10) or (love_sum1 > 90):
    print(f"Your score is {love_sum}, you go together like coke and mentos.")

elif (love_sum1 >= 40) and (love_sum1 <= 50) :
    print(f"Your score is {love_sum}, you are alright together.")

else :
    print(f"Your score is {love_sum}.")
    