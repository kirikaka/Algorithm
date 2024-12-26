from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
mat = [
  [0, 1, 1, 1, 1, 1],
  [0, 1, 0, 0, 0, 1],
  [0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 0],
  [0, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 0]
  ]
# for _ in range(N):
#     row = list(map(int, input().split()))
#     mat.append(row)
print(mat)

def bfs(y,x): # 좌표의 행과 열을 x,y를 반대로 넣어야한다. 
  visited=[[False]*M for _ in range(N)]
  dx=[-1,0,0,1] #열
  dy=[0,1,-1,0] #행
  
  visited[y][x]=True
  queue=deque()
  queue.append([y,x])
  while queue:
    loc=queue.popleft()
    print(loc[0],loc[1])
    for i in range(4):
      ny=loc[0]+dy[i]  #행 좌표 계산
      nx=loc[1]+dx[i]  #열 좌표 계산
      if (ny <0) or (ny>=N) or (nx<0) or( nx>=M):
        continue
      if mat[ny][nx]==1:
        continue
      if not visited[ny][nx]:
        visited[ny][nx]=True
        queue.append([ny,nx])
        
bfs(0,0)