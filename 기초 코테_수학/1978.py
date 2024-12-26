n=int(input())

_list=list(map(int,input().split()))
count=0

for i in _list:
  for k in range(2,i+1):
    if i%k==0:
      if i==k:
        count+=1
      break
      
print(count)