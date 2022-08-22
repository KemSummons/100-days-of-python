student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# we cant use sum() or len()
# it will be like a:
# print(round(sum(student_heights) / len(student_heights)))

# this is == sum()
all_height = 0
for height in student_heights:
    all_height += height

# this is == len()
all_students = 0
for student in student_heights:
    all_students += 1

print(round(all_height / all_students))
