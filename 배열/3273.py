import sys
from itertools import permutations,combinations

input=sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))
x=int(input())

nums.sort()
if len(nums)%2==1:
  l=len(nums)+1
  
  