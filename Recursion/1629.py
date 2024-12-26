import sys

a,b,c=map(int,sys.stdin.readline().split())

def recur(a,b):
  
  if b==1:
    return a%c
  else:
    tmp=recur(a,b//2)
    if b%2==0:
      return (tmp * tmp )%c 
    else:
      return (tmp * tmp*a)%c

print(recur(a,b))  