# This program asks for your name and calculates your average and highest test scores
# It contains several errors (syntax, runtime, and logic) for you to find and fix

print("Welcome to the Debugging Lab!")
#Make sure to have end parenthasis for statments
name = input("Enter your name: ")
#make sure to have qoutes around strings and what you want to print.
print("Hello " + name + "!" + " Let's calculate your test scores.")

scores = [85, 90, 78, 88, 92]
#make sure to have an indentation before loop thingy
total = 0
for score in scores:
    total = total + score
#lens gives you amount of set  number in a list
average = total / len(scores)
print("Your average score is: ", average)
#highest is a variable that is contantly checked to see if there is a new high score
highest = 0
for s in scores:
    if s > highest:
        highest = s

print("Your highest score was:" + str(highest))