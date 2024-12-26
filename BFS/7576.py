from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())

tomato=[]
for _ in range(m):
  row=list(map(int,sys.stdin.readline().split()))
  tomato.append(row)


day=[[0]*n for _ in range(m)]

que=deque()
for i in range(m):
  for j in range(n):
    if tomato[i][j]==0:
      day[i][j]=-1
    elif tomato[i][j]==1:
      que.append([i,j])
      
while que:
  dx=[-1,0,0,1]
  dy=[0,1,-1,0]
  value=que.popleft()
  for i in range(4):
    ny=value[0]+dy[i]
    nx=value[1]+dx[i]
    if nx<0 or ny<0 or ny>=m or nx>=n:
      continue
    if day[ny][nx]>=0:
      continue
    day[ny][nx]=day[value[0]][value[1]]+1
    que.append([ny,nx])
    
ans=0      
for i in range(m):
  for j in range(n):
    ans=max(ans,day[i][j])

for i in range(m):
  for j in range(n):
    if day[i][j]== -1:  
      ans=-1
          

print(ans)
    
    
