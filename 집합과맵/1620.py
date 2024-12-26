n,m=map(int,input().split())

index=1
poket1={}
poket2={}
for i in range(n):
  txt=input()
  poket1[str(index)]=txt
  poket2[txt]=index
  index+=1
  
pok_list=poket2.keys()  
res=[]

for i in range(m):
  inp=input()
  if inp in pok_list:
    res.append(poket2[inp])
  else:
    res.append(poket1[inp])


for i in res:
  print(i)