class Node:
  def __init__(self, data):
    self.data = data  #data는 값을 가리키는 변수(속성, attribute)
    self.next = None  #next는 다음 노드를 가리키는 변수
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length
      
    def __str__(self):
      
      if self.head is None:
        return "Empty LinkedList"        
      print("List Print")
      node=self.head
      res="Head"
      while node:
        res+="-> "+str(node.data)
        node=node.next           
      return res

      
    def appendleft(self,data):
      if self.head is None:
        self.head = Node(data)
      else:
        node=Node(data)
        node.next=self.head
        self.head=node
      self.length+=1
  
    def append(self,data):
      if self.head is None:
        self.head=Node(data)
      else:
        node=self.head #첫번째 노드를 불러오기
        while node.next:
          node=node.next
        node.next=Node(data)
      self.length+=1
      
    def __contains__(self,target):
      if self.head is None:
        return False
      node=self.head
      while node:
        if node.data==target:
          return True
        node=node.next
      return False
          

      
    def remove(self,target):
      node=self.head
      while node is not None and node.data != target:
        prev=node
        node=node.next
      if node is None:
        return False
      if node==self.head:
        self.head=self.head.next
      else:
        prev.next=node.next
      self.length-=1
      return True

      
    def insert(self,i,data):
      if i<0:
        self.appendleft(data)
      elif i>self.length:
        self.append(data)
      else:
        node=self.head
        for _ in range(i-1):
          node=node.next
        temp=Node(data)
        temp.next=node.next
        node.next=temp
        self.length+=1

      
      

if __name__ == "__main__":
    import random
    my_list = LinkedList()
    for i in range(5):
        my_list.append(i)
    print(f"연결 리스트의 상태\n연결 리스트의 길이 = {len(my_list)},  {my_list}")
    print()
    for _ in range(5):
        i = random.randrange(10)
        data = random.randint(10, 20)
        my_list.insert(i, data)
        print(f"{data}를(을) 연결 리스트의 {i}인덱스에 삽입했습니다.")
        print(f"연결 리스트의 길이 = {len(my_list)},  {my_list}\n")