import sys
from itertools import permutations, product,combinations
from itertools import combinations 

input=sys.stdin.readline
n,m=map(int,input().split())


ans=[]
def back():
  if len(ans)==m:
    return
  for i in range(1,n+1):
    
  
