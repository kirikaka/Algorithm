import sys

class Node:
  def __init__(self, data):
    self.data = data  #data는 값을 가리키는 변수(속성, attribute)
    self.next = None  #next는 다음 노드를 가리키는 변수
    
    
class LinkedList:  
  def __init__(self):
    self.head = None
    self.length = 0
    self.cursor=0

  def __len__(self):
    return self.length
    
    
  
  def append(self,data):
    if self.head is None:
      self.head=Node(data)
    else:
      node=self.head
      while node.next is not None:
        node=node.next
      node.next=Node(data)
    self.length+=1
    self.cursor+=1
    
        
  def __str__(self):
    if self.head is None:
      return "It is empty"
    res=""
    node=self.head
    while node is not None:
      res+=str(node.data)
      node=node.next
    return res
      
  def L(self): 
    if self.cursor!=0:
      self.cursor-=1
    
  
  def D(self): 
    if self.cursor!=self.length:
      self.cursor+=1
  
#커서 왼 쪽에 있는 원소를 삭제해야한다. 왼쪽 
  def B(self):   
    if self.cursor!=0:
      cursor=self.cursor
      node=self.head
      for _ in range(cursor-1):
        prev=node
        node=node.next
      if node==self.head:
        self.head=self.head.next
      else:
        prev.next=node.next
      self.cursor-=1
      self.length-=1


    
  def P(self,data):
    cursor=self.cursor
    if cursor==0 and self.head is not None:
      temp=Node(data)
      temp.next=self.head
      self.head=temp
      self.cursor+=1
      self.length+=1
      return 
        
    if self.head:
      node=self.head
      for _ in range(cursor-1):
        node=node.next
      temp=Node(data)
      temp.next=node.next
      node.next=temp
      self.cursor+=1
      self.length+=1
      
    else:
      self.head=Node(data)
      self.cursor+=1
      self.length+=1

    

str_ex=sys.stdin.readline().strip()
n=int(sys.stdin.readline())


editor=LinkedList()
for i in range(len(str_ex)):
  editor.append(str_ex[i])


for _ in range(n):
  func=sys.stdin.readline().split()
  if func[0]=='P':
    editor.P(func[1])
  elif func[0]=='L':
    editor.L()
  elif func[0]=='D':
    editor.D()
  elif func[0]=='B':
    editor.B()

print(editor)