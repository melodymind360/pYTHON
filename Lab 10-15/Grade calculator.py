grade = float(input("Enter your grade: "))

if grade >= 90:
   letter_grade = "A"
elif grade >= 80:
   letter_grade = "B"
elif grade >= 70:
   letter_grade = "C"
elif grade >= 60:
   letter_grade = "D"
else:
   letter_grade = "F"

print(f"Your letter grade is: {letter_grade}")
#this program tells you what grade you get based on the number you put in using above or equal 
#questions with if, elif, and else statements.