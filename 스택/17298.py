import sys
from collections import deque

input=sys.stdin.readline
n=int(input())

"""
수열 A의 크기 N (1 ≤ N ≤ 1,000,000) 이므로 
최대 시간복잡도는 O(nlogn)

- 틀린 풀이 1
리스트를 순회하며 element 하나당
다른 원소랑 비교해서 더 큰수 나올떄 까지 pop 시키기

- 풀이 2
그냥 pop해서 원소를 순회하고
pop한 원소(cur)와 stack의 top을 비교
cur이 더 작으면 stack의 top을 result에 넣고
cur이 더 크면 stack을 모두 순회하며 큰거 나올때 까지 찾는다. 

"""

stack=[]
res=[]
nge=list(map(int,input().split()))

while nge:
  tmp=nge.pop()
  if len(stack) == 0:
    stack.append(tmp)
    res.append(-1)  
  else:
    if stack[-1]<=tmp: 
      while stack:
        if stack[-1]>tmp:
          res.append(stack[-1])
          break
        stack.pop()
      if not stack:
        res.append(-1)
    else:
      res.append(stack[-1])
    stack.append(tmp)

print(" ".join(map(str,res[::-1])))
        
      


# #시간초과
# nge=deque(map(int,input().split()))

# for i in range(n):
#   cur=nge.popleft()
#   ohbig=-1
#   temp=deque()
#   while nge:
#     cur_pop=nge.popleft()
#     temp.append(cur_pop)
#     if cur<cur_pop:
#       ohbig=cur_pop
#       break
#   nge=nge+temp
#   answer.append(ohbig)

# print(" ".join(map(str,answer)))

  
  