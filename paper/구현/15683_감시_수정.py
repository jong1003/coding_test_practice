import copy
#완전탐색 문제


n,m=map(int,input().split())
init_board=[list(map(int, input().split())) for _ in range(n)]


def sol():
    q=[]
    for i in range(n):
        for j in range(m):
            if init_board[i][j]>0 and init_board[i][j]<6:
                q.append([i,j])

    dfs(q,0,init_board)

    return invisible


def dfs(queue,index,board):
    start_board=copy.deepcopy(board)
    invisible=0
    
    if index==len(queue):
        invisible=min(invisible,count(board))

    else:
        y,x=queue[index]
        cctv_type=board[y][x]
        
        if cctv_type==1:
            for i in range(4):
                make[i](board,y,x)
                dfs(queue,index+1,board)
                board=copy.deepcopy(start_board)
        
        elif cctv_type==2:
            make[0](board,y,x)
            make[1](board,y,x)
            dfs(queue,index+1,board)
            board=copy.deepcopy(start_board)

            make[2](board,y,x)
            make[3](board,y,x)

            dfs(queue,index+1,board)
            board=copy.deepcopy(start_board)

        elif cctv_type==3:
            a=[0,0,1,1]
            b=[2,3,2,3]

            for i in range(4):
                make[a[i]](board,y,x)
                make[b[i]](board,y,x)
                dfs(queue,index+1,board)
                board=copy.deepcopy(start_board)

        elif cctv_type==4:
            for i in range(4):
                for j in range(4):
                    if j!=i:
                        make[j](board,y,x)
                dfs(queue,index+1,board)
                board=copy.deepcopy(start_board)
        else:
            for i in range(4):
                make[i](board,y,x)            
            dfs(queue,index+1,board)
            board=copy.deepcopy(start_board)


def count(board):
    num=0
    for i in board:
        for j in i:
            if j==0:
                num+=1
    return num

def up(board,y,x):
    if y==0:
        return

    for i in range(y-1,-1,-1):
        if board[i][x]==0:
            board[i][x]=7
        elif board[i][x]==6:
            break

def down(board,y,x):
    if y==n-1:
        return

    for i in range(y+1,n):
        if board[i][x]==0:
            board[i][x]=7
        elif board[i][x]==6:
            break

def left(board,y,x):
    if x==0:
        return

    for i in range(x-1,-1,-1):
        if board[y][i]==0:
            board[y][i]=7
        elif board[y][i]==6:
            break

def right(board,y,x):
    if x==m-1:
        return

    for i in range(x+1,m):
        if board[y][i]==0:
            board[y][i]=7
        elif board[y][i]==6:
            break

make={0:left,1:right,2:up,3:down}
print(sol())