import sys
num=int(sys.stdin.readline())

all=[]
for i in range(num):
  all.append(sys.stdin.readline().rstrip())
all=list(set(all))
all.sort()
res=sorted(all,key=len)

for i in res:
  print(i)