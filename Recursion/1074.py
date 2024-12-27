import sys

def recur(n,r,c):
  if n==0:
    return 0
  half=2**(n-1)
  if r<half and c<half: # 왼쪽 위
    return recur(n-1,r,c)
  if r<half and c>=half: # 오른쪽 위
    return (half*half)+recur(n-1,r,c-half) 
  if r>=half and c<half: # 왼아래
    return (2*half*half)+recur(n-1,r-half,c)
  else:                  # 오른 아래
    return (3*half*half)+recur(n-1,r-half,c-half)

  


n,r,c=map(int,sys.stdin.readline().split())

print(recur(n,r,c))
