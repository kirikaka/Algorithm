import sys
from collections import deque

input=sys.stdin.readline

#세로(y), 가로(x), 높이(Z)
M,N,H = map(int,input().split()) 

tomato=[]
for _ in range(H):
    tomato.append([list(map(int,input().split())) for _ in range(N)])

day=[[[0]*M for _ in range(N) ] for _ in range(H)]

""" 토마토가 2층으로 쌓아져있다. """

dx=[-1,1,0,0,0,0] #
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]


que=deque()
for i in range(H):
  for j in range(N):
    for k in range(M):
      if tomato[i][j][k]==1:
        que.append([i,j,k])
        day[i][j][k]==0
      elif tomato[i][j][k]==0:
          day[i][j][k]=-1


while que:
  cur=que.popleft()
  cur_day=day[cur[0]][cur[1]][cur[2]]

  for i in range(6):
    nz=cur[0]+dz[i]
    ny=cur[1]+dy[i]
    nx=cur[2]+dx[i]

    if nz<0 or nx<0 or ny<0 or nz>=H or ny>=N or nx>=M:
      continue
    if tomato[nz][ny][nx]==1:
      continue
    if tomato[nz][ny][nx]==-1:
      continue
    if day[nz][ny][nx]==-1:
      day[nz][ny][nx]=cur_day+1
      que.append([nz,ny,nx])

need=0

def neeed(need):
  for i in range(H):
    for j in range(N):
      for k in range(M):
        if day[i][j][k]==-1:
          return -1
        elif need<day[i][j][k]:
          need=day[i][j][k]
  return need


res=neeed(need)
print(res)