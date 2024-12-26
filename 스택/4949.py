import sys


while True:
  answer=True
  stack=[]
  sent=sys.stdin.readline().rstrip()
  if sent=='.':
    break
  for i in sent:
    if i=='(' or i=='[':
      stack.append(i)
      
    elif i==']':
      if len(stack) ==0:
        answer=False
        break
      else:
        gual=stack[-1]
      if len(stack) ==0 or gual != '[':
        answer=False
        break
      stack.pop()
      
      
    elif i==')':
      if len(stack) ==0:
        answer=False
        break
      else:
        gual=stack[-1]
      if len(stack) ==0 or gual != '(':
        answer=False
        break
      stack.pop()
  
  if len(stack) == 0  and answer:
    print('yes')
  else:
    print('no')
    
    
