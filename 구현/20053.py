import sys

t=int(sys.stdin.readline())
for i in range(t):
  n=int(sys.stdin.readline())
  nums=list(map(int,sys.stdin.readline().split()))
  print(min(nums), max(nums))