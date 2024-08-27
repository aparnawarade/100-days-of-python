line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input(" Where do you want to put the treasure?"
                 )  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
#print(f"{line1}\n{line2}\n{line3}")
column = position[0]
column_pos = {"A": 0, "B": 1, "C": 2}
column1 = column_pos.get(column)
row = int(position[1]) - 1
list_nested = [line1, line2, line3]
list_nested[row][column1] = 'X'
for i in list_nested:
  print(i)
