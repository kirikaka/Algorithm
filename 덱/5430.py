import sys,math
from collections import deque

input=sys.stdin.readline

t=int(input())

"""
시간 초과 hint : R 들어올때마다 control 변수에 -1 곱해서
양수면 P 일때 popleft 음수면 pop하기 
"""

for _ in range(t):
  p=input()
  n=int(input())
  nums=deque(input().rstrip()[1:-1].split(','))
  wrong=0
  if n==0:
    nums=[]
  control=1
  for i in p:
    if i =='R':
      control*=(-1)
    elif i=='D':
      if len(nums)==0:
        wrong=1
        continue
      else:
        if control>0:
          nums.popleft()
        else:
          nums.pop()
  if control<0:
    nums=list(reversed(nums))
  
  if wrong==0:
    print("[" + ",".join(nums) + "]")
  else:
    print('error')  
  
  
