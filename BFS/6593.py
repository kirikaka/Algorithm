from collections import deque
import sys
input=sys.stdin.readline

""" 각 칸에서 인접한 6개의 칸(동,서,남,북,상,하)으로 1분의 시간을 들여 이동 """

while(True):
  L,R,C=map(int,input().split()) #층,행(Y),열(X)
  if L==0 and R==0 and C==0:
    break
    
  
  building=[]
  for _ in range(L):
    floor=[input().strip() for _ in range(R)]
    building.append(floor)
    ceiling=input()
  
  visit=[[[False]*C for _ in range(R)] for _ in range(L)]
  
  def BFS(z,y,x,time):
    
    que=deque()
    que.append([z,y,x,time])
    visit[z][y][x]=True
    
    
    
    dz=[0,0,1,-1,0,0]
    dy=[-1,1,0,0,0,0]
    dx=[0,0,0,0,1,-1]
    
    while que:
      cur=que.popleft()
      
      if building[cur[0]][cur[1]][cur[2]]=='E':
          return cur[3]
      
      for i in range(6):
        nz=cur[0]+dz[i]
        ny=cur[1]+dy[i]
        nx=cur[2]+dx[i]
        
        if nz<0 or ny<0 or nx<0 or nz>=L or ny>=R or nx>=C:
          continue
        if building[nz][ny][nx]=='#':
          continue
        if visit[nz][ny][nx]:
          continue
        
        que.append([nz,ny,nx,cur[3]+1])
        visit[nz][ny][nx]=True
        
      
      
    
    
    
  for z in range(L):
    for y in range(R):
      for x in range(C):
        if building[z][y][x]=='S':
          ans=BFS(z,y,x,0)
  
  if ans is None:
    print("Trapped!")
  else:
    print(f"Escaped in {ans} minute(s).")
  
  









