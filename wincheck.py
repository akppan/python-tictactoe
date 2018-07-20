def win_check():
    if(li[0]==li[1]==li[2] and li[0]!=''):
        return True
    if(li[3]==li[4]==li[5] and li[3]!=''):
        return True
    if(li[6]==li[7]==li[8] and li[6]!=''):
        return True
    if(li[0]==li[3]==li[6] and li[0]!=''):
        return True
    if(li[1]==li[4]==li[7] and li[1]!=''):
        return True
    if(li[2]==li[5]==li[8] and li[2]!=''):
        return True
    if(li[0]==li[4]==li[8] and li[0]!=''):
        return True
    if(li[2]==li[4]==li[6] and li[2]!=''):
        return True
