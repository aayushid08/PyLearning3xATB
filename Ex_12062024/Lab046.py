# Grading Scale Program
# Question : Program to implement a grading scale based on the given marks.
#
# """
# This program takes a student's marks as input and assigns a corresponding grade based on the grading scale.
# The grading scale is as follows:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
# """

# Multiple condition - if, elif, else

# step 1 -> logic building
# input from user
# score -> int
# output -> string
# write the rough logic

# Get the student's marks from the user

score = int(input("Enter the student's score: "))

# if score < 100 and score >= 90:
#     print("Grade A")
# elif score < 90 and score >= 80:
#     print("Grade B")
# elif score < 80 and score >= 70:
#     print("Grade C")
# elif score < 70 and score >= 60:
#     print("Grade D")
# else:
#     print("Grade F")

# other logic
if score <= 100 and score >= 90:
    print("Grade A")
elif score <= 89 and score >= 80:
    print("Grade B")
elif score <= 79 and score >= 70:
    print("Grade C")
elif score <= 69 and score >= 60:
    print("Grade D")
elif score <= 60 and score >= 0:
    print("Grade F")
else:
    print("Invalid score")

##################################

