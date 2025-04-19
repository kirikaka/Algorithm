from collections import deque
import sys

input=sys.stdin.readline

r,c=map(int,input().split())  #r은 행,Y좌표. C는 열,X좌표

space=[list(input().strip()) for _ in range(r)] #입력받은 미로찾기

visit = [[0] * c for _ in range(r)] # 지훈 방문 여부
fire = [[0] * c for _ in range(r)] # 불 방문 여부

"""
1. 지훈과 불의 위치와 속성을 큐에 넣기.
1-1. 왜 불이 먼저 ??
1-1-a. 지훈이랑 불이랑 동시에 움직인다고 봐야하는데 두개의 que를 동시에 가동하지않는
이상 불가능하다 그러므로 불을 먼저 움직여서 동시성을 만들어 준다. 
2. que의 맨 앞 pop해서 [2]로 지훈인지 불인지 구분하기
3. 지훈인 경우
3-1. r,c나 0보다 작으면 탈출이므로 return
3-2. 만약 불이 있거나 벽이면 continue
3-3. 이미 방문했으면 continue
3-4. 전부 아니면 que에 넣기.
4. 불인 경우
4-1. 경계 넘으면 continue
4-2. 벽이면 continue
4-3. 이미 방문했으면 Continue

"""
que=deque()



for x in range(r):      # x는 행
  for y in range(c):    # y는 열
    if space[x][y]=='J':
      que.append([x,y,'J'])     # que에 [행,열,사람]로 append
      visit[x][y]=1
      
    if space[x][y]=='F':
      que.appendleft([x,y,'F'])      # que에 [행,열,불]로 append
      fire[x][y]=1
      
      

def BFS():
  global que
  
  dx=[-1,1,0,0]   #상하좌우
  dy=[0,0,-1,1]   #상하좌우
  
  while que:
  
    cur=que.popleft()
    x=cur[0]
    y=cur[1]
    
    
    
    if cur[2]=='J':
      for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        
        if nx < 0 or nx>=r or ny<0 or ny>=c:
          return visit[x][y]
        if space[nx][ny]=='#' or fire[nx][ny]!=0:
          continue
        if visit[nx][ny]!=0:
          continue
        que.append([nx,ny,'J'])
        visit[nx][ny]=visit[x][y]+1
        
    else:
      for i in range(4):
        nx=dx[i]+cur[0]
        ny=dy[i]+cur[1]
        
        if nx < 0 or nx>=r or ny<0 or ny>=c:
          continue
        if space[nx][ny]=='#':
          continue
        if fire[nx][ny]!=0:
          continue
        que.append([nx,ny,'F'])
        fire[nx][ny]=fire[x][y]+1
      
ans=BFS()

      
if ans is None:
  print('IMPOSSIBLE')
else:
  print(ans)
  
  
  
  
  