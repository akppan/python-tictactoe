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
