import sys
from collections import deque
input=sys.stdin.readline


"""
deque로 작성할 수도 있고
리스트 인덱스로도 할 수 있다.
"""

n,k=map(int,input().split())

def josephus(n,k):
  jose=deque()
  res=[]
  for i in range(1,n+1):
    jose.append(i)
  while len(jose)>1:
    for _ in range(k-1):
      jose.append(jose.popleft())
    res.append(jose.popleft())
  res.append(jose.popleft())
  return res

res=josephus(n,k)
print("<", end="")
for i in range(len(res)-1):
  print(res[i], end=", ")
print(str(res[len(res)-1])+">")