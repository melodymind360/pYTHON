
import random

number = random.randint(0, 100)

print("Guess the magic number between 0 and 100")
#Since the guess minuus 1 is outside the loop it doesnt effect the number. You also want to start
#wuth a value that is not equal to the number so the loop can start.
guess = -1  
#the while is where the loop begins, and it means as long as the guess doesnt equal the wanted
#number it will keep the loop going.

while guess != number:
    guess = int(input("\nEnter your guess: "))

    if guess == number:
        print(f"Yes, the number is {number}")
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

