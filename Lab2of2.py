#1. What is the length of the string variable verse?
#2. What is the index of the first occurrence of the word 'and' in verse?
#3. What is the index of the last occurrence of the word 'you' in verse?
#4. What is the count of occurrences of the word 'you' in the verse?


verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

new_str = verse.split()
print (new_str)
print (len(new_str))

answer1 = (len("verse"))

answer2 = (new_str.index("and"))

#print (new_str.index("you")) #1st you
#print (new_str.index(("you"), 2, 71)) #2nd you
#print (new_str.index(("you"), 10, 71)) #3rd you
answer3 = new_str.index(("you"), 20, 71) #4th you

answer4 = new_str.count("you")

#answers
print ("the length of the string variable verse is {}".format(answer1))
print ("the index of the first occurrence of the word 'and' in verse is {}".format(answer2))
print ("the index of the last occurrence of the word 'you' in verse is {}".format(answer3))
print ("the count of occurrences of the word 'you' in the verse is {}".format(answer4))


