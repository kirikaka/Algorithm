a,b=map(int,input().split())

for i in range(a,b+1):
  for j in range(2,i+1):
    if i%j==0:
      if i==j:
        print(j)
      break
  