import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
RGB=[list(input().strip()) for _ in range(N)]

visit=[[False]*N for _ in range(N) ]

"""
일반인은 RGB의 구역을 구분할 수 있다.
색약인은 RG와 B만 구분할 수 있따.
R,G,B를 따로 돌린다음에 색약인사람은 


"""


def BFS_R(visit):
  que=deque()
  que.append([0,0])     #세로,가로,색깔
  visit[0][0]=True
  


  
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  
  while que:
    cur=que.popleft()
    
    for i in range(4):
      nx=dx[i]+cur[0]
      ny=dy[i]+cur[1]
      
      if nx<0 or ny<0 or nx>=N or ny>=N:
        continue
      
      if not visit[nx][ny] and RGB[nx][ny]=='R':        
        visit[nx][ny]=True
        que.append([nx,ny])


def BFS_G(visit):
  que=deque()
  que.append([0,0])     #세로,가로,색깔
  visit[0][0]=True
  


  
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  
  while que:
    cur=que.popleft()
    
    for i in range(4):
      nx=dx[i]+cur[0]
      ny=dy[i]+cur[1]
      
      if nx<0 or ny<0 or nx>=N or ny>=N:
        continue
      
      if not visit[nx][ny] and RGB[nx][ny]=='G':        
        visit[nx][ny]=True
        que.append([nx,ny])
          
        
def BFS_B(visit):
  que=deque()
  que.append([0,0])     #세로,가로,색깔
  visit[0][0]=True
  


  
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  
  while que:
    cur=que.popleft()
    
    for i in range(4):
      nx=dx[i]+cur[0]
      ny=dy[i]+cur[1]
      
      if nx<0 or ny<0 or nx>=N or ny>=N:
        continue
      
      if not visit[nx][ny] and RGB[nx][ny]=='B':        
        visit[nx][ny]=True
        que.append([nx,ny])
          
        
      

      
  
  
