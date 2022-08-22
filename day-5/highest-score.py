student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# we cant use max()
# it will be like a:
# print(max(student_scores))

# this is == max()
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f'The highest score in the class is: {max_score}')
