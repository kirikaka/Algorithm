import sys

def recur(n,r,c):
  if n==0:
    return 0
  half=2**(n-1)
  if r<half and c<half: # 1사분면
    return recur(n-1,r,c)
  if r<half and c>=half:
    return (half*half)+recur(n-1,r,c-half)
  if r>=half and c<half:
    return (2*half*half)+recur(n-1,r-half,c)
  else:
    return (3*half*half)+recur(n-1,r-half,c-half)

  


n,r,c=map(int,sys.stdin.readline().split())

print(recur(n,r,c))
