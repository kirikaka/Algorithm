import sys
from itertools import permutations, product,combinations
from itertools import combinations 

input=sys.stdin.readline
n,m=map(int,input().split())
sys.setrecursionlimit(10000)


ans=[]
def back():
  if len(ans)==m:
    print(" ".join(map(str,ans)))
    return
  for i in range(1,n+1):
    if len(ans)==0:     
      ans.append(i)
      back()
      ans.pop()
    elif ans[-1]<=i:
      ans.append(i)
      back()
      ans.pop()
    
back()


"""
  첫번쨰 원소 넣을 떄와 다른 경우의 수를 따로 구성해 둔다. 
"""