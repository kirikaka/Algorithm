from collections import deque
import sys
input=sys.stdin.readline


N=int(input())
for _ in range(N):
  L=int(input())
  start_x,start_y=map(int,input().split())
  end_x,end_y=map(int,input().split())
  
  chess=[[False]*L for _ in range(L)]
  time=[[-1]*L for _ in range(L)]
  
  chess[end_x][end_y]=True #시작 위치와 종료 위치 표시
  time[start_x][start_y]=0
  
  que=deque()
  que.append([start_x,start_y])
  
  while que:
    cur=que.popleft()
    cur_time=time[cur[0]][cur[1]]
    
    if chess[cur[0]][cur[1]]:
      break
    
    
    
    dx=[1,2,2,1,-1,-2,-2,-1]
    dy=[-2,-1,1,2,2,1,-1,-2]
    
    for i in range(8):
      nx=cur[0]+dx[i]
      ny=cur[1]+dy[i]
      
      if nx<0 or ny<0 or nx>=L or ny>=L:
        continue
      if time[nx][ny]!=-1:
        continue
      
      que.append([nx,ny])
      time[nx][ny]=cur_time+1
          
  
  
  print(cur_time)
  