for i in range(22):
    print(" ",end="")
print("PLAYER {}'s TURN".format(1))

li=[]
s=""
for i in range(9):
    li.append(s)

pos=1
li[pos]='X'

def display_board(pos):
    for j in range(3):
        for i in range(20):
            print(" ",end="")
        for i in range(9):
            print("--",end="")
            i+=1
        print("")
        for i in range(20):
            print(" ",end="")
        for k in range(19):
            if(k%6==0):
                print("|",end="")
            else:
                print(" ",end="")
        print("")
        for i in range(20):
            print(" ",end="")
        for k in range(19):
            if(k%6==0):
                print("|",end="")
            elif(k%3==0 and k%6!=0 and li[pos]!='' and pos==(3*j)+((k+3)/6.0)):
                print("{}".format(li[pos]),end="")
            else:
                print(" ",end="")
        print("")
        for i in range(20):
            print(" ",end="")
        for k in range(19):
            if(k%6==0):
                print("|",end="")
            else:
                print(" ",end="")
        print("")

    for i in range(20):
        print(" ",end="")
    for i in range(9):
        print("--",end="")
        i+=1
    print("")


display_board(pos)
        
