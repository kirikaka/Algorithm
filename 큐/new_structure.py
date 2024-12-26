queue=[]
pos=0
front=0
rear=0


def top(queue):
  return queue[pos-1]

def isEmpty(queue):
  return len(queue)==0

def enqueue(queue,item):
  global rear
  queue.append(item)
  rear+=1
  print("데이터 추가")

def dequeue(queue):
  global front
  if isEmpty(queue):
    print('스택이 비어있습니다.')
    return None
  else:
    print(f'{top(queue)}이 나가집니다.')
    front+=1
    return queue[front-1]
  
for i in range(0,8):
  enqueue(queue,chr(ord("A") + i))
  print(f"Enqueued data : {queue[rear-1]}")
print()

while not front==rear:
  print(f"Dequeue data= { dequeue(queue)}")