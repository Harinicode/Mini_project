import random
def play():
    cguess=random.choice(['r','p','s'])                 #computer
    pguess=input("Enter r-rock,p-paper & s-scissor: ")  #player guessa
    if(pguess=='r' and cguess=='p')or(pguess=='p' and cguess=='s')or(pguess=='s' and cguess=='r'):
        return False
    else:
        return True
    if cguess==pguess:
        return 'd'
   
n=int(input('Enter the no. of chances: '))
n1=n
pwin=0
cwin=0
for i in range(3):
    print("YOU HAVE {} CHANCES: ".format(n))
    val=play()
    if val=='d':
        print("Draw\n")
        continue
    if val:
        print("You Won\n")
        pwin+=1                                         #player win count
    else:
        print("Computer Won\n")
        cwin+=1                                         #computer win count
    n-=1

print("\nYou won {} times\nComputer won {} times\nDraw {} times".format(pwin,cwin,n1-(pwin+cwin)))
