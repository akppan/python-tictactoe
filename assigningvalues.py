def func()
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
