import sys
input=sys.stdin.readline

n=list(map(int,input().strip()))

cnt=0
sets=[0 for _ in range(10)]

for i in range(len(n)):
  if n[i]==9:
    n[i]=6


for i in range(len(n)):
  sets[n[i]]+=1

if sets[6]%2==1:
  sets[6]=sets[6]//2+1
else:
  sets[6]=sets[6]//2


print(max(sets))



