import sys,copy
from collections import deque
input=sys.stdin.readline

N=int(input())
rgb=[list(input().strip()) for _ in range(N)]

visit=[[False]*N for _ in range(N) ]
visit_abnormal=[[False]*N for _ in range(N) ]

"""
일반인은 RGB의 구역을 구분할 수 있다.
색약인은 RG와 B만 구분할 수 있따.
일반 그림은 RGB로 해놓고 색약인은 RG를 합쳐놓자 해놓으면 되려나?

"""

""" 일반 Copy나 등호는 얕은복사이다. 얕은복사와 깊은 복사 다시 정리해보기. """
rgb_abnormal=copy.deepcopy(rgb) 

#rgb_abnormal 은 색약이 보는 그림.
for i in range(N):        
  for j in range(N):
    if rgb_abnormal[i][j]=='G':
      rgb_abnormal[i][j]='R'


def BFS(visit,x,y,color):
  que=deque()
  que.append([x,y,color])     #세로,가로,색깔
  visit[x][y]=True
  
  
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  
  while que:
    cur=que.popleft()
    cur_color=cur[2]
    
    for i in range(4):
      nx=dx[i]+cur[0]
      ny=dy[i]+cur[1]
      
      if nx<0 or ny<0 or nx>=N or ny>=N:
        continue
      
      if not visit[nx][ny] and rgb[nx][ny]==color:        
        visit[nx][ny]=True
        que.append([nx,ny,cur_color])

def BFS_A(visit,x,y,color):
  que=deque()
  que.append([x,y,color])     #세로,가로,색깔
  visit[x][y]=True
  
  
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  
  while que:
    cur=que.popleft()
    cur_color=cur[2]
    
    for i in range(4):
      nx=dx[i]+cur[0]
      ny=dy[i]+cur[1]
      
      if nx<0 or ny<0 or nx>=N or ny>=N:
        continue
      
      if not visit[nx][ny] and rgb_abnormal[nx][ny]==color:        
        visit[nx][ny]=True
        que.append([nx,ny,cur_color])

count=0
count_abnormal=0  
  
for i in range(N):        
  for j in range(N):
    if not visit[i][j]:
      BFS(visit,i,j,rgb[i][j])
      count+=1
    if not visit_abnormal[i][j]:
      BFS_A(visit_abnormal,i,j,rgb_abnormal[i][j])
      count_abnormal+=1
      
print(count,count_abnormal)