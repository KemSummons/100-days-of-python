# Use a Debugger
def mutate(a_list):
    b_list = []
# we have for-loop, which multiply elements in a_list and adding they in b_list
    for item in a_list:
        new_item = item * 2
# in next string we have problem - adding elements in b_list use only last multiply (13 * 2)
# because 'b_list.append(new_item)' don't enter in for-loop construction
# for debugging problem we must adding one indent (tab or 4 spaces)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
