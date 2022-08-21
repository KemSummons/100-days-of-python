row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position_int_1 = int(position[0])
position_int_2 = int(position[1])
# # we can do it more simply like a:
# selected_row = map[position_int_2 - 1]
# selected_row[position_int_1 - 1] = 'X'
if position_int_1 == 1 and position_int_2 == 1:
    map[0][0] = 'X'
elif position_int_1 == 1 and position_int_2 == 2:
    map[1][0] = 'X'
elif position_int_1 == 1 and position_int_2 == 3:
    map[2][0] = 'X'
elif position_int_1 == 2 and position_int_2 == 1:
    map[0][1] = 'X'
elif position_int_1 == 2 and position_int_2 == 2:
    map[1][1] = 'X'
elif position_int_1 == 2 and position_int_2 == 3:
    map[2][1] = 'X'
elif position_int_1 == 3 and position_int_2 == 1:
    map[0][2] = 'X'
elif position_int_1 == 3 and position_int_2 == 2:
    map[1][2] = 'X'
elif position_int_1 == 3 and position_int_2 == 3:
    map[2][2] = 'X'

print(f"{row1}\n{row2}\n{row3}")