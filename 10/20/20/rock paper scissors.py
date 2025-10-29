import random
#make sure to define all variables and associate 
# them with their assigned numbers for accesibility reasons
rock = "rock"
paper = "paper"
scissors = "scissors"

print ("Welcome to Rock, Paper, Scissors!")
#in order for the person to chose what they want inter user_choice. Than do the input so they can
#chose what they want.
#in order for the computer to chose use computer_choice and then random.choice.
user_choice = input("Enter your choice (rock, paper, scissors): ")
computer_choice = random.choice([rock, paper, scissors])

if user_choice == computer_choice:
    print(f"Both chose {user_choice}. It's a tie!")
elif user_choice == rock and computer_choice == scissors:
        print("Rock beats scissors! You win.")
elif user_choice == paper and computer_choice == rock:
        print("Paper beats rock! You win.")
elif user_choice == scissors and computer_choice == paper:
        print("Scissors beats paper! You win.")
        #use else statement at the end for when user loses
else:
    print(f"Sorry, {computer_choice} beats {user_choice}. You lose.")
   
