import heapq

n=int(input())
_list=[]

for _ in range(5):
  nums=map(int,input().split())
  for i in nums:
    if len(_list)<n:
      heapq.heappush(_list,i)
    else:
      if _list[0]<i:
        heapq.heappop(_list)
        heapq.heappush(_list,i)
        
        
print(_list[0])
      