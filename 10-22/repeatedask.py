X=0
NO="n"
YES="y"
answer=""
while (answer!=NO):
    answer=input(f"do you want to continue? 1.{YES} 2.{NO} ")
    if answer==YES:X += 1 
    print(f"you have repeated {X} times")
    
    

else:    
    print("you have exited the program")
