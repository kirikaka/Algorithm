from collections import deque
import sys
input=sys.stdin.readline

T=int(input())


for _ in range(T):
  w,h=map(int,input().split()) # w는 x, h는 y
  
  building=[list(input().strip()) for _ in range(h)]  
  visit=[[0]*w for _ in range(h)]
  fire=[[0]*w for _ in range(h)]
  
  que=deque()
  
  
  for y in range(h):
    for x in range(w):
      if building[y][x]=='@':
        visit[y][x]=1
        que.append([y,x,"@"])
      if building[y][x]=='*':
        fire[y][x]=1
        que.appendleft([y,x,'F'])
  
  
  def BFS():
    global que
  
    while que:
      dx=[-1,1,0,0]
      dy=[0,0,1,-1]
      
      cur=que.popleft()
      
      cur_y=cur[0]
      cur_x=cur[1]
            
      if cur[2]=='@':
        
        for i in range(4):
          nx=dx[i]+cur_x
          ny=dy[i]+cur_y
          
          
          if ny<0 or nx<0 or nx>=w or ny>=h:
            return visit[cur_y][cur_x]
          
          if building[ny][nx]=='#':
            continue
          if fire[ny][nx] !=0:
            continue
          if visit[ny][nx]!=0:
            continue
          que.append([ny,nx,'@'])
          visit[ny][nx]=visit[cur_y][cur_x]+1
          
      elif cur[2]=='F':
        for i in range(4):
          nx=dx[i]+cur_x
          ny=dy[i]+cur_y
          
          if nx<0 or ny<0 or nx>=w or ny>=h:
            continue          
          if building[ny][nx]=='#':
            continue
          if fire[ny][nx] !=0:
            continue
                  
          que.append([ny,nx,'F'])
          fire[ny][nx]=fire[cur_y][cur_x]+1
  
  ans=BFS()
    
  if ans is None:
    print('IMPOSSIBLE')
  else:
    print(ans)  
  
