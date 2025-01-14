import sys

input=sys.stdin.readline

n=int(input())

"""
ABAB 순으로 나오면 안되고 ABBA 식으로는 나와야 한다.
그냥 A들어올때 stack[-1]에 A 가 있으면 pop(B도 마찬가지)
stack에 아무것도 안남아잇으면 cnt+=1
"""

cnt=0
for _ in range(n):
  word=input().strip()
  stack=[]
  answer=True
  A_count=1
  B_count=1
  for i in word:

    if stack and stack[-1]=='A' and i=='A':
      stack.pop()
      continue
    if stack and stack[-1]=='B' and i=='B':
      stack.pop()
      continue
    
    
    
    stack.append(i)
    

  
  if len(stack)==0:
    cnt+=1

print(cnt)