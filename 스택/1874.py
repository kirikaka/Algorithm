import sys
input=sys.stdin.readline

n=int(input())
ans=[]


"""
숫자 하나 입력받고 그전 숫자까지 stack에 넣는다. 넣을 때마다 + 넣기
stack 마지막 거와 num이 같으면 pop하고 - 넣기
아니면 NO 출력

"""
now=1
condition=True
stack=[]
res=[]
for _ in range(n):
  num=int(input())
  for i in range(now,num+1):  
    stack.append(now)
    res.append('+')
    now+=1
  if stack[-1]==num:
    stack.pop()
    res.append('-')
  else:
    condition=False
    
if condition:
  for i in res:
    print(i)
else:
  print('NO')
