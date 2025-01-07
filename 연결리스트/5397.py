import sys
input=sys.stdin.readline

"""
- : 백스페이스로 커서 앞의 글자를 지운다
<> : 화살표
앞의 1406과 같은 stack으로 해볼까?
"""
n=int(input())
for _ in range(n):
  kang=input().strip()
  left=[]
  right=[]
  for i in kang:

    if i=='<' and left:
      right.append(left.pop())
    elif i=='>' and right:
      left.append(right.pop())
    elif i=='-' and left:
      left.pop()
    elif not i=='<' and not i=='>' and not i=='-':
      left.append(i)
  res=left+right[::-1]
  print("".join(res))
  
