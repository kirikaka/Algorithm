import sys

queue=[]
head=0
rear=0


def push(queue,item):
  global rear
  queue.append(item)
  rear+=1

def pop(queue):
  global head
  if len(queue)==0:
    return print(-1)
  else:
    head+=1
    return print(queue.pop(0))

def size(queue):
  return print(len(queue))

def empty(queue):
  if len(queue)==0:
    return print(1)
  else:
    return print(0)
  
def front(queue):
  if len(queue)==0:
    return print(-1)
  else:
    return print(queue[0])
    

def back(queue):
  if len(queue)==0:
    return print(-1)
  else:
    return print(queue[-1])
    
    
  
N=int(sys.stdin.readline())
for _ in range(N):
  a=sys.stdin.readline().split()
  if a[0]=='push':
    push(queue,int(a[1]))
  elif a[0]=='size':
    size(queue)
  elif a[0]=='empty':
    empty(queue)
  elif a[0]=='front':
    front(queue)
  elif a[0]=='back':
    back(queue)
  elif a[0]=='pop':
    pop(queue)