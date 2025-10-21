import random
die1=2
die2=5
diettl=die1+die2


if diettl==7 or diettl==11:
    print(f"you rolled a {diettl}, you win!!!")
elif die1 == die2:
    if die1==6 and die2==6:
        print(f"jackpot, you win!!")
    else:
        print(f"you rolled a double!You win!!!")
else: 
    print(f"you rolled a {diettl}, you lose!!! please try again.")
 