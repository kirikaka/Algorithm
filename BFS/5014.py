from collections import deque
import sys

input=sys.stdin.readline

F,S,G,U,D=map(int,input().split())

visit=[False]*(F)

"""
건물 높이 F
강호가 있는 S층
가는 층 G
누르면 위로 U칸
누르면 아래로 D칸 
"""



que=deque()
que.append([S-1,0])
visit[S-1]=True


def BFS():
  
  while que:
    
    cur=que.popleft()
    cur_time=cur[1]
    d=[-D,U]
    
    
    if cur[0]==G-1:
      return cur_time
    
    for i in range(2):
      dy=cur[0]+d[i]
      
      
      if dy<0 or dy>=F:
        continue
      if visit[dy]:
        continue
      
      
      que.append([dy,cur_time+1])
      visit[dy]=True

ans=BFS()

if ans is None:
  print("use the stairs")
else:
  print(ans)  
