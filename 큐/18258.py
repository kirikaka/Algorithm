import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
que=deque()
for _ in range(n):
  command=input().split()
  if command[0]=='push':
    que.append(int(command[1]))
  elif command[0]=='front':
    if que:
      print(que[0])
    else:
      print(-1)
  elif command[0]=='back':
    if que:
      print(que[-1])
    else:
      print(-1)
  elif command[0]=='size':
    print(len(que))
  elif command[0] =='empty':
    if len(que)==0:
      print(1)
    else:
      print(0)
  elif command[0]=='pop':
    if que:
      print(que.popleft())
    else:
      print(-1)