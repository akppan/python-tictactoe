'''First python project'''

for i in range(22):
    print(" ",end="")
print("WELCOME TO TIC-TAC-TOE\n\n")


dictt={}

li=[]

s=""
for i in range(9):
    li.append(s)


def firsttime():
    for i in range(22):
        print(" ",end="")
    print("RULES OF GAME")
    print("If any player is able to make 3 consecutive signs 'X' or '0' in\na row or column or diagonally wins the game")
    player_input()



def replay():
    print("Do you want to play again? 1 for YES 0 for NO")
    pa=int(input())
    return pa

#============================================================
def player_turn(no):
    for i in range(22):
        print(" ",end="")
    print("PLAYER {}'s TURN".format(no))


#============================================================
def display_board(num):
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
            elif(k%3==0 and k%6!=0 and li[int((3*j)+((k+3)/6.0))-1]!=''):
                print("{}".format(li[int((3*j)+((k+3)/6.0))-1]),end="")
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

#=============================================================        


def player_input():
    global p1
    global p2
    global dictt
    p1=input('Player 1 Choose your variable "X" or "0" ')
    while(p1!='X' and p1!='0'):
        print("PLAYER 1 HAVE CHOOSEN A WRONG VARIABLE\nCHOOSE FROM GIVEN ONES")
        p1=input('Player 1 Choose your variable "X" or "0" ')
        
    if(p1=='X'):
        p2='0'
        print('Player 2 is "0"')
    elif(p1=='0'):
        p2='X'
        print('Player 2 is "X"')


    dictt={'pl1':[p1,1],'pl2':[p2,2]}

    place_marker()

#==============================================================

def place_marker():
    p=1
    turn=0
    global li
    while(not win_check() and turn<9):
        sign=dictt['pl'+str(int(not p)+1)][0]
        player_turn(dictt['pl'+str(int(not p)+1)][1])
        turn+=1
        for i in range(17):
            print(" ",end="")
        pos=int(input("Choose any number in 1 to 9 "))
        while(not space_check(pos)):
            pos=int(input("Choose another number in 1 to 9 "))
            print("POSITION NOT EMPTY, CHOOSE ANOTHER NUMBER")
        li[pos-1]=sign
        display_board(pos+1)
        p=not p
    if(not win_check() and turn>=9):
        print("MATCH DRAW")
    else:
        player_win(dictt['pl'+str(int(p)+1)][1])
    

#==============================================================

def win_check():
    if(li[0]==li[1]==li[2] and li[0]!=''):
        return True
    elif(li[3]==li[4]==li[5] and li[3]!=''):
        return True
    elif(li[6]==li[7]==li[8] and li[6]!=''):
        return True
    elif(li[0]==li[3]==li[6] and li[0]!=''):
        return True
    elif(li[1]==li[4]==li[7] and li[1]!=''):
        return True
    elif(li[2]==li[5]==li[8] and li[2]!=''):
        return True
    elif(li[0]==li[4]==li[8] and li[0]!=''):
        return True
    elif(li[2]==li[4]==li[6] and li[2]!=''):
        return True

#==============================================================


def space_check(pos):
    if(li[pos-1]==''):
        return True
    else:
        return False

#==============================================================

def full_board_check():
    while(replay()):
        global li
        li=[]
        s=""
        for i in range(9):
            li.append(s)
        player_input()

def player_win(pla):
    print("PLAYER {} wins".format(pla))

firsttime()
full_board_check()
