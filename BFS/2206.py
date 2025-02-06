from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000000)


N,M=map(int,input().split())

move=[list(map(int,input().strip())) for _ in range(N)]
visit=[[-1]*M for _ in range(N)]


"""
- 이동하며 최단경로를 계산하면서 움직인다..?
0이나 1이나 구분하지않고 경로를 계산한다.
1을 카운트한다. que에 넣을때 1을 지낫는지의 여부에 대해 확인한다
ex) que.append([y,x,최단 경로,1을 몇번 지낫는지])
만약 1을 지낫는데 또 1을 지나야하면 가지않고 continue
"""
que=deque()
que.append([0,0,0,False])
visit[0][0]=0

cnt=0

while que:
  cur=que.popleft()
  
  if cur[0]==N-1 and cur[1]==M-1:
    cnt=cur[3]
  
  dx=[-1,1,0,0]
  dy=[0,0,1,-1]
  
  for i in range(4):
    ny=cur[0]+dy[i]
    nx=cur[1]+dx[i]
    
    
    if nx<0 or ny<0 or nx>=M or ny>=N:
      continue
    if visit[ny][nx]!=-1:
      continue
    if move[ny][nx]==1 and cur[3]==1:
      continue
    if move[ny][nx]==1 and cur[3]==0:
      new_cur=True
    que.append([ny,nx,cur[2]+1,new_cur])
    visit[ny][nx]=cur[2]+1
    
    
if visit[N-1][M-1]==-1:
  print(-1)
elif cnt==0:
  print(visit[N-1][M-1])
else:
  print(visit[N-1][M-1]+1)


