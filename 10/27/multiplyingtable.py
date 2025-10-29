
wantednumber= int(input("choose a number to multiply by all whole numbers up to 10: "))
#need to set wanted number variable first, than set the looping range for the multiplying variable (mv)
#
mv=(1,10)
print(f"choose a number to multiply by all whole numbers up to 10{wantednumber}: ")
mv = 0
while mv !=10:
    mv = mv + 1
    total = wantednumber * mv
    print(f"{wantednumber} x {mv} = {total}")
    #the != means not equal to 10, you have to set mv to 0 so it starts at zero and than adds 1 when
    #  the loop starts, so the table stars at 1 as it adds 
    # 1 in the beggining in the loop.
    #you than want to set your total as the wanted number times the changing variable,
    #you than need to put it in a print statment to show it.
    #it will than repeat the process until the mv equals 10.
   
