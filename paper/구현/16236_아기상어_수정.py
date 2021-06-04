import queue
inf=1000000

n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]

#이동을 위한 값, 상좌우하 순
dx=[0,-1,1,0]
dy=[-1,0,0,1]


#bfs(n,board,x,y,size) : queue활용하여 먹을 수 있는 물고기 중 가장 가까운 물고기의 좌표 반환
#comp(a,b,time) : 먹을 수 있는 물고기의 두 좌표를 비교 -> 걸린 시간/y/x 순으로 비교
#sol 메인 솔루션 함수 

#size[0] : 아기상어 크기
#size[1] : 먹은 물고기 수 (size[0]==size[1]일 때마다 초기화)
#board[][] : 상어와 물고기가 사는 바닷 속
#time[][] : 아기상어가 해당 좌표까지 가는데 걸리는 시간을 담은 리스트


def sol(n,board):
    
    time=0 #최종 시간
    x,y,t=-1,-1,0

    for i in range(n):#아기상어의 초기위치 찾기
        for j in range(n):
            if board[i][j]==9:
                x,y=j,i
                board[y][x]=0
                break
    
    size=[2,0] #아기상어 초기 크기 [크기,먹은물고기수]

    while(t!=inf): #bfs 반환된 t 값이 유효한 값이 아닐 때까지 bfs 반복
        x,y,t=bfs(n,board,x,y,size) 
        if t!=inf:
            time+=t
    return time

def bfs(n,board,x,y,size):
    


    
    time=[[0]*n for _ in range(n)]#아기상어로 부터의 거리 확인 + 각 칸을 방문 했는지 여부 위한 2차원리스트
    rx,ry,rt=n+1,n+1,inf #비교를 위한 값 선언 (유효하지 않은초기 값)
    
    
    #bfs
    q=queue.Queue() #bfs를 위한 큐 선언
    q.put([x,y]) #처음 노드 
    
    

    while(not q.empty()):
        x,y=q.get()
        
        
        if board[y][x]<size[0] and board[y][x]>0: #상어보다 작은 물고기를 찾았을 때
            rx,ry,rt=comp([rx,ry],[x,y],time) #비교 함수를 통해 더 적절한 위치 선택

        elif board[y][x]<=size[0]:#통과 가능한 위치(0 또는 아기상어 크기)
            for i in range(4):#위 왼쪽 오른쪽 아래 순으로 탐색
                nx=x+dx[i]
                ny=y+dy[i]

                if ny>=n or ny<0:continue
                if nx>=n or nx<0:continue #범위 확인

                if time[ny][nx]!=0:continue #방문한 좌표인지 확인

                time[ny][nx]=time[y][x]+1 #거리 추가  
                
    if rt!=inf: #시간 값이 유효하다면=>먹을 수 있는 물고기가 있었다면
        size[1]+=1 #먹은 물고기 수 증가
        if size[1]==size[0]: #벌크업
            size[0]+=1
            size[1]=0
        board[y][x]=0 #죽은물고기 묘지
                        
    return rx,ry,rt

def comp(a,b,time): #비교함수
        nx,ny=a[0],a[1]
        mx,my=b[0],b[1]
        nt,mt=time[nx,ny],time[mx,my]

        if nt<mt: #시간비교
            return nx,ny,nt
        elif mt<nt:
            return mx,my,mt

        if ny<my:#y좌표 비교
            return nx,ny,nt
        elif my<ny:
            return mx,my,mt

        if nx<mx: #x좌표 비교
            return nx,nx,nt
        elif mx<nx:
            return mx,my,mt

        
        
        



print(sol(n,board))