# Banker Roulette

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

num_itam = len(names)

random_choice = random.randint(0 , num_itam - 1)

bill = names[random_choice]

print(bill  + " is going to buy the meal today!$")