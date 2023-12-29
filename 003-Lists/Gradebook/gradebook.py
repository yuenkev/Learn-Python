last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

#2D List
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

#Add to the list 
gradebook.append(["computer science", 100])
print(gradebook)

gradebook.append(["visual arts", 93])
print(gradebook)

#modifying visual arts class to be 5 points higher
gradebook[-1][-1] = 98
print(gradebook)

#switch poetry class to pass/fail option
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)

#Combin 2 lists to have a complete book
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
