import sys
input=sys.stdin.readline

gual=list(input().strip())
stack=[]

"""
()인 괄호열의 값은 2이다.
[] 인 괄호열의 값은 3이다.
(X) 의 괄호값은 2*값(X) 으로 계산된다.
[X] 의 괄호값은 3*값(X) 으로 계산된다.
올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.

(()[[]]) ([]) = 2*(2 + 3*3) + 2*3

step1. 열때 tmp에 2or3을 곱하기. 
step2. 닫을 때 mid에 다 옮기기? 그러면 가장 큰 괄호는 어케하냐고
step3. 
   


"""
tmp=1
res=0
mid=0
for i in range(len(gual)):
  
  if stack and gual[i]==')' and stack[-1]=='(':
    stack.pop()
    if stack:
      tmp*=2
      print('A')
    else:
      mid*=2
  elif stack and gual[i]==']' and stack[-1]=='[':
    stack.pop()
    if stack:
      tmp*=3
      print('B')
    else:
      mid*=3
      
  elif stack and gual[i]=='(' and stack[-1]=='(':
    stack.append(gual[i])
    print('C')
    
  elif stack and gual[i]=='[' and stack[-1]=='[':
    stack.append(gual[i])
    print('D')
    
  elif stack and gual[i]=='[':
    stack.append(gual[i])
    mid+=tmp
    tmp=1
    print('E')
  elif stack and gual[i]=='(':
    stack.append(gual[i])
    mid+=tmp
    tmp=1
    print('F')
  
    
  elif gual[i]==')' and stack[-1]=='(':
    stack.pop()
    if not stack:
      mid*=2
      print('F')
  elif gual[i]==']' and stack[-1]=='[':
    stack.pop()
    if not stack:
      mid*=3
      print('G')
    
  else:
    stack.append(gual[i])
    print('H')
  
     
  if len(stack)==0:
    res+=mid
    
  print(i+1,'번째 순서')
  print(stack)
  print('현재 계산 값 : ',tmp)
  print('현재 중간 값 : ',mid)
  print()

  
print(stack)
if len(stack)>0:
  print(0)
else:
  print(res)