
from collections import deque
import sys

input=sys.stdin.readline

t=int(input())
for _ in range(t):
  m,n,k=map(int,input().split()) #가로길이 m 세로 n 배추 위치의 개수 k
  lettuce=[[0]*m for _ in range(n)] #배추밭
  
  for _ in range(k):          
    x,y=map(int,input().split())    #배추밭의 배추 위치
    lettuce[y][x]=1                 # y가 가로줄이므로 x가 세로줄
  
  visit=[[False]*m for _ in range(n)]


  COUNT=0
  
  
  def BFS(y,x,visit):
    visit[y][x]=True
    que=deque()
    que.append([y,x])
    
      
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]       #  상하좌우
    
    while que:
      cur=que.popleft()
      for i in range(4):
        nx=cur[0]+dx[i]
        ny=cur[1]+dy[i]
        
        if nx<0 or ny<0 or nx>=n or ny>=m:
          continue
        
        if lettuce[nx][ny]==0:
          continue
        
        if visit[nx][ny]==False:    
          #print('현재 위치 : ',  ny,nx)
          visit[nx][ny]=True
          que.append([nx,ny])
          
      
      
      
    
    
    
  
  
  for x in range(n):
    for y in range(m):
      if lettuce[x][y]==1 and visit[x][y] ==False:
        #print('현재 양배추 탐색 위치 : ',  y,x)
        BFS(x,y,visit)
        COUNT+=1
  
  print(COUNT)




  
"""
그림찾기와 마찬가지로 하면된다.


"""




