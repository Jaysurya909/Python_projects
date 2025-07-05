def box():
    zero='X' if xstate[0]==1 else 'O' if ostate[0]==1 else 0
    one='X' if xstate[1]==1 else 'O' if ostate[1]==1 else 1
    two='X' if xstate[2]==1 else 'O' if ostate[2]==1 else 2
    three='X' if xstate[3]==1 else 'O' if ostate[3]==1 else 3
    four='X' if xstate[4]==1 else 'O' if ostate[4]==1 else 4
    five='X' if xstate[5]==1 else 'O' if ostate[5]==1 else 5
    six='X' if xstate[6]==1 else 'O' if ostate[6]==1 else 6
    seven='X' if xstate[7]==1 else 'O' if ostate[7]==1 else 7
    eight='X' if xstate[8]==1 else 'O' if ostate[8]==1 else 8
    
    
    print(f" {zero} | {one} | {two}")
    print("-----------")
    print(f" {three} | {four} | {five}")
    print("-----------")
    print(f" {six} | {seven} | {eight}")


xstate=[0,0,0,0,0,0,0,0,0]
ostate=[0,0,0,0,0,0,0,0,0]
index_check=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
#win patterns are:- [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
print("The game has begun")
win1=None
win2=None
game=0
while(True):
   
    value=int(input("X's Turn:-"))
    xstate[value]=1
    box()
    for pattern in index_check:
        result=all(xstate[i]==1 for i in pattern)
        if(result==True):
            win1=result
            break
    if(win1==True):
        print("X is The Winner!!\n")
        break
    if(game==4):
        print("The game is draw!!")
        break
    value2=int(input("O's Turn:-"))
    ostate[value2]=1
    box()
    for pattern in index_check:
        result=all(ostate[i]==1 for i in pattern)
        if(result==True):
            win2=result
            break
    if(win2==True):
        print("O is The Winner!!\n")
        break
    game=game+1
    

    
   
