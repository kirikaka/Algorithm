n=int(input())
card1=set(list(map(int,input().split())))

m=int(input())
card2=list(map(int,input().split()))


res=[]
for i in card2:
  if i in card1:
    res.append(1)
  else:
    res.append(0) 

for i in res:
  print(i,end=" ")