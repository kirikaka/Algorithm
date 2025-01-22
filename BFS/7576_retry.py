from collections import deque
import sys

input=sys.stdin.readline


""" m은 가로 n은 세로"""
m,n=map(int,input().split())

tomato=[list(map(int,input().split())) for _ in range(n)]

"""
시작점이 여러개인 BFS를 돌 수 있어야 한다.
모든 시작점(익은 토마토)를 큐에 넣고 똑같이 BFS를 돈다.

"""
day=[[0]*m for _ in range(n)]


que=deque()
for i in range(n):
  for j in range(m):
    if tomato[i][j]==1:
      que.append([i,j])
      day[i][j]=0
    elif tomato[i][j]==0:
      day[i][j]=-1

# que=deque()
# for i in range(n):
#   for j in range(m):
#     if tomato[i][j]==0:
#       day[i][j]=-1
#     elif tomato[i][j]==1:
#       que.append([i,j])

dx=[-1,1,0,0]
dy=[0,0,1,-1]
while que:
  cur=que.popleft()
  cur_day=day[cur[0]][cur[1]]



  for i in range(4):
    
    nx=cur[1]+dx[i]
    ny=cur[0]+dy[i]
    
    if ny<0 or nx<0 or ny>=n or nx>=m:
      continue
    
    if tomato[ny][nx]==-1:
      continue
    
    if tomato[ny][nx]==1:
      continue
    
    if day[ny][nx]==-1:
      day[ny][nx]=cur_day+1
      que.append([ny,nx])
      

  
  
need=0

def neeed(need):
  for i in range(n):
    for j in range(m):
      if day[i][j]==-1:
        return -1
        
      elif need<day[i][j]:
        need=day[i][j]
  return need

res=neeed(need)
print(res)


      