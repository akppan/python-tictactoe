p1='X'
p2='0'
s=''
li=[]
for i in range(9):
    li.append(s)

print(li)
c=1
while(c):
    sign=input("Choose sign ")
    f=int(input("Choose any number in 1 to 9 "))
    if(li[f-1]==''):
        li[f-1]=sign
    else:
        print("PLACE NOT EMPTY CHOOSE ANOTHER POSITION")
        f=int(input("Choose any number in 1 to 9 "))
    print(li)
    c=int(input("c is "))
