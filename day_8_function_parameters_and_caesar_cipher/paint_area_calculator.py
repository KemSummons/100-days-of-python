def paint_calc(height, width, cover):
    result = height * width
    final_result = result // cover
    if result % cover == 0:
        print(f"You'll need {final_result} cans of paint.")
    else:
        final_result += 1
        print(f"You'll need {final_result} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
