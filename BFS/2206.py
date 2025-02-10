from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)


N,M=map(int,input().split())

move=[list(map(int,input().strip())) for _ in range(N)]
visit=[[-1]*M for _ in range(N)]
visit_crash=[[-1]*M for _ in range(N)]

"""
- 이동하며 최단경로를 계산하면서 움직인다..?
0이나 1이나 구분하지않고 경로를 계산한다.
1을 카운트한다. que에 넣을때 1을 지낫는지의 여부에 대해 확인한다
ex) que.append([y,x,최단 경로,1을 몇번 지낫는지])
만약 1을 지낫는데 또 1을 지나야하면 가지않고 continue

부시고 방문한 것과 부시지 않고 방문한 것을 다르게 해야한다
HOW?
visit와 visit_crash를 모두 만들어서\
"""


que=deque()
que.append([0,0,0,False])
visit[0][0]=0
visit_crash[0][0]=0



cnt=True

while que:
  cur=que.popleft()
  # print(cur)
  if cur[0]==N-1 and cur[1]==M-1:
    cnt=cur[3]
  
  dx=[-1,1,0,0]
  dy=[0,0,1,-1]
  
  for i in range(4):
    new_cur=cur[3]
    nx=cur[1]+dx[i]
    ny=cur[0]+dy[i]
    
    if nx<0 or ny<0 or nx>=M or ny>=N:
      continue
    if cur[3] is False and visit[ny][nx]!=-1:
      continue
    if cur[3] is True and visit_crash[ny][nx]!= -1:
      continue
    if move[ny][nx]==1 and cur[3]==True:
      continue
    if move[ny][nx]==1 and cur[3]==False:
      new_cur=True
    que.append([ny,nx,cur[2]+1,new_cur])
    
    if new_cur:
      visit_crash[ny][nx]=cur[2]+1
    else:
      visit[ny][nx]=cur[2]+1

# print(visit)
# print(visit_crash)




# if visit[N-1][M-1]==-1 and visit_crash[N-1][M-1]==-1:
#   print(-1)
# elif cnt is False:
#   print(visit[N-1][M-1]+1)
# else:
#   print(visit_crash[N-1][M-1]+1)
  
if visit[N-1][M-1]==-1 and visit_crash[N-1][M-1]==-1:
  print(-1)
else:
  crash=visit_crash[N-1][M-1]
  non_crash=visit[N-1][M-1]
  res=0
  if crash !=-1 and non_crash !=-1:
    res=min(crash,non_crash)
  elif crash==-1:
    res=non_crash
  else:
    res=crash

  print(res+1)
  

# 반례  
# 10 2
# 01
# 00
# 10
# 00
# 01
# 00
# 10
# 00
# 01
# 00

# ans:13