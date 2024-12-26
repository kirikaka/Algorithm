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


visited=[[False]*M for _ in range(N)]

def DFS(visited,y,x):
  dx=[-1,0,0,1]
  dy=[0,1,-1,0]
  visited[y][x]=True
  stack=[]
  stack.append([y,x])
    
  
  while stack:
    value=stack.pop()
    for i in range(4):
      nx=value[1]+dx[i]
      ny=value[0]+dy[i]
      if (ny<0 or nx<0  or ny>=M or nx>=N):
        continue
      if mat[ny][nx]==1:
        continue
      if not visited[ny][nx]:
        stack.append([ny,nx])
        visited[ny][nx]=True
      
DFS(visited,0,0)
for i in range(N):
  for j in range(M):
    print(visited[i][j],end=' ')
  print()