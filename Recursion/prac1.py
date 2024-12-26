import sys


def print_recur(n):
  if n<0:
    return
  print(n)
  n-=1
  print_recur(n)
  
def summ(n):
  
  if n<0:
    return 0
  else:
    return n+summ(n-1)
    
    
n=int(sys.stdin.readline())
print_recur(n)
sres=summ(n)

print(sres)