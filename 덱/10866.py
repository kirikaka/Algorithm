from collections import deque
import sys


def push_front(d,item):
  d.appendleft(item)
    
def push_back(d,item):
  d.append(item)
    
def pop_front(d):
  if len(d) !=0:
    temp=d.popleft()
    print(temp)
  else:
    print(-1)
  
def pop_back(d):
  if len(d) !=0:
    temp=d.pop()
    print(temp)
  else:
    print(-1)

def back(d):
  if len(d) !=0:
    temp=d[-1]
    print(temp)
  else:
    print(-1)

def size(d):
  print(len(d))
    
def front(d):
  if len(d) !=0:
    temp=d[0]
    print(temp)
  else:
    print(-1)

def empty(d):
  if len(d) !=0:
    print(0)
  else:
    print(1)


d=deque()
N=int(sys.stdin.readline())

for _ in range(N):
  a=sys.stdin.readline().split()
  if a[0]=='push_front':
    push_front(d,int(a[1]))
  elif a[0]=='push_back':
    push_back(d,int(a[1]))
  elif a[0]=='pop_front':
    pop_front(d)
  elif a[0]=='pop_back':
    pop_back(d)
  elif a[0]=='back':
    back(d)
  elif a[0]=='size':
    size(d)
  elif a[0]=='empty':
    empty(d)
  elif a[0]=='front':
    front(d)