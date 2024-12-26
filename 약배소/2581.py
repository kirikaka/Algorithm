m=int(input())
n=int(input())

s=[]
last=0
for i in range(m,n+1):
  count=0
  for j in range(2,i+1):
    if i%j==0:
      count+=1    
  if count==1:
    s.append(i)


if len(s)>0:
  print(sum(s))
  print(s[0])
else:
  print(-1)
