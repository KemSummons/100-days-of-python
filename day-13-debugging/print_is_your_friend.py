# Print is Your Friend
# we have useless variables 'pages' and 'word_per_page' with value '0'
# because in strings № 6 and 7 we have variables 'pages' and 'word_per_page' with input
# so no need declare a variables before input
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# in next string we have two symbols '==', what means strict comparison, not an assignment
# next string must be like a - word_per_page = int(input("Number of words per page: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
