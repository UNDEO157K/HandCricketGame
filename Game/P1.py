import random

a = input("choose odd or even : ")
b = int(input("enter your number : "))
c = random.randrange(1,11)
print("computer chooses :", c)
print("sum of chooses :", (b+c))
    
# Taking toss decision

if((a=="odd" and (b+c)%2==1) or (a=="even" and (b+c)%2==0) ):
    print("you won the toss")
    k = input("choose batting or balling : ")
    if(k=="batting"):
        l = "balling"
        print("computer chooses", l)
    else:
        l = "batting"
        print("computer chooses", l) 
else:
    print("you lost the toss")
    options = ["batting","balling"]
    l = random.choice(options)
    print(f"computer chooses {l}")
    if(l=="batting"):
        k = "balling"
        print("you choose", k)
    else:
        k = "batting"
        print("you choose", k)

    
# starting game 

if(k =="batting"):
    score = 0
    while True:
        you = int(input("enter your number : "))
        computer = random.randrange(1,11)
        print("you choose ", you)
        print("computer choose ", computer)
        score = score + you
        if(you==computer):
            print("1st Innings are over")
            print("Target is " , score + 1)
            break
    k = "balling"
    l = "batting"
    print("2nd Innings begins")
    print(f"now you choose {k} and computer chooses {l}" )
    sor = 0
    while True:
        you = int(input("enter your number : "))
        computer = random.randrange(1,11)
        print("you choose ", you)
        print("computer choose ", computer)
        sor = sor + computer
        if(you==computer):
            print("You WON !!. Computer loses ")
            break
        if(sor>=(score + 1)):
            print(f"computer scores a total of {sor}")
            print("You lost and Computer wins")




if(k =="balling"):
    sor = 0
    while True:
        you = int(input("enter your number : "))
        computer = random.randrange(1,11)
        print("you choose ", you)
        print("computer choose ", computer)
        sor = sor + computer
        if(you==computer):
            print("1st Innings are over")
            print("Target is " , sor + 1)
            break
    k = "batting"
    l = "balling"
    print("2nd Innings begins")
    print(f"now you choose {k} and computer chooses {l}" )
    score = 0
    while True:
        you = int(input("enter your number : "))
        computer = random.randrange(1,11)
        print("you choose ", you)
        print("computer choose ", computer)
        score = score + you
        if(you==computer):
            print(f"you scored a total of {score}")
            print("You lost and Computer wins")
            break
        if(score>=(sor + 1)):
           print(f"you scored a total of {score}")
           print("You WON !!. Computer loses ")




        
