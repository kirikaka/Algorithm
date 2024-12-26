import sys


n,m=map(int,sys.stdin.readline().split())
light=list(map(int,sys.stdin.readline().split()))

for _ in range(m):
  a,b,c=map(int,sys.stdin.readline().split())
  if a==1:
      light[b-1]=c
  elif a==2:
    for i in range(b-1,c):
      if(light[i]==0):
        light[i]=1
      else:
        light[i]=0
  elif a==3:
    for i in range(b-1,c):
      light[i]=0
  elif a==4:
    for i in range(b-1,c):
      light[i]=1
  
for i in range(n):
  print(light[i],end=" ")
