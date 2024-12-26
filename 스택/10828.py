import sys

stack=[]

def top(stack):
  if len(stack) == 0:
    return print(-1)
  else:
    return print(stack[-1]) 


def empty(stack):
  if len(stack)==0:
    return print(1)
  else:
    return print(0)

def push(stack,item):
  stack.append(item)

def size(stack):
  return print(len(stack))

def pop(stack):
  if len(stack) == 0:
    return print(-1)
  else:
    return print(stack.pop())

N=int(sys.stdin.readline())
for _  in range(N):
    a=sys.stdin.readline().split()
    if a[0]=='push':
      push(stack,a[1])
    elif a[0]=='pop':
      pop(stack)
    elif a[0]=='size':
      size(stack)
    elif a[0]=='empty':
      empty(stack)
    elif a[0]=='top':
      top(stack)