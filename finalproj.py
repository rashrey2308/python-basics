#A Voting System

dict1={"A":1,"B":2,"C":3,"D":4}
dict2={1:True,2:False,3:True,4:False}
party=[0,42,22,43,12]
party2={1:'BJP', 2:'ABC', 3:'TMC', 4:'DEF'}
password='pass1'
while(True):
    print("Choices: \n1. Login to cast his/her vote \n2. See the result based on the votes \n3. Exit")
    print("Enter Choice")
    n=int(input())
    if(n==3):
        exit()
    if (n==1):
        print("Enter name:")
        name=input()
        print("Enter voter ID:")
        id=int(input())
        if(dict1[name]==id):
            if(dict2[id]==True):
                print(dict2[id])
                print("Already voted")
            else:
                print ("List of parties:")
                print ("1:BJP, 2:ABC, 3:TMC, 4:DEF")
                print ("Enter the choice of party number")
                pn=int(input())
                party[pn]+=1
                print("Your vote has been registered. Thank you for voting")
                continue
        else:
            print("Invalid credentials")
            continue
    elif(n==2):
        print("Enter password")
        p=input()
        if(p!=password):
            print("Wrong Password")
            continue
        else:
            print ("BJP: ",party[1]," ABC: ",party[2]," TMC: ",party[3]," DEF: ",party[4])
            m=party[1]
            pos=1
            for i in range(len(party)):
                if m<party[i]:
                    m=party[i]
                    pos=i
            print (party2[pos]," won!!")
    else:
        print ("Wrong Choice")
