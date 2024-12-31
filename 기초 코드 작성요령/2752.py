import sys
input=sys.stdin.readline

nums=list(map(int,input().split()))
nums.sort()

for i in nums:
  print(i,end=' ')