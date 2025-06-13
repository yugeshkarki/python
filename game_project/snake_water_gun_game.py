import random
#snake water and gun Game
#   -1 for water ,1 for snake, 0 for gun
# import random
computer=random.choice([-1,1,0])
userStr=input("enter the choice :")
youDict={"s":1,"w":-1,"g":0}
ReverseDict={1:"snake",-1:"water",0:"gun"}

you = youDict[userStr]

print(f"you choose {ReverseDict[you]}\n computer choose ~{ReverseDict[computer]}")

if(computer==you):
    print("It is draw")
 
else:
    if(computer==-1 and you==1):
        print("you Win !")
    elif(computer==-1 and you==0):
        print("you Lose!")

    elif(computer==1 and you==-1):
        print("you Lose!")
    
    elif(computer==1 and you==0):
        print("you Win!")

    elif(computer==0 and you==-1):
        print("you Win !")

    elif(computer==0 and you==1):
        print("you Lose!")

    else:
        print("something went wrong") 