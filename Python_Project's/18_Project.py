# Treasure Map

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

Horizontal = int(position[0])
Vertical   = int(position[1])

Selacted_row = map[Vertical - 1]
Selacted_row[Horizontal - 1] = " X"

print(f"{row1}\n{row2}\n{row3}")