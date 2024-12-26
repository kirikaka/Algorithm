stack=[]
MAX_SIZE=10
pos=0

def top(stack):
  return stack[pos-1]

def  isFull(stack):
  return len(stack)==MAX_SIZE

def isEmpty(stack):
  return len(stack)==0

def push(stack,item):
  if isFull(stack):
    print("스택이 가득 찼습니다.")
  else:
    stack.append(item)
    print("데이터 추가")

def pop(stack):
  if isEmpty(stack):
    print('스택이 비어있습니다.')
    return None
  else:
    print(f'{top(stack)}이 나가집니다.')
    return stack.pop()
  
  

# 스택에 데이터 추가
stack.append(1)
stack.append(2)
stack.append(3)

# 스택에서 데이터 꺼냄
top_element = stack.pop( ) 
next_element = stack.pop( ) 

# 스택의 크기를 구함
stack_size = len(stack)
print(stack)