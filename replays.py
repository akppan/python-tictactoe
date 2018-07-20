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


def full_board_check():
    while(replay()):
        global li
        li=[]
        s=""
        for i in range(9):
            li.append(s)
        player_input()


firsttime()
full_board_check()
