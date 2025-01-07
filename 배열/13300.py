import sys

input=sys.stdin.readline

n,k=map(int,input().split())
boy=[]
girl=[]
for _ in range(n):
  s,y=map(int,input().split())
  if s==1:
    boy.append(y)
  else:
    girl.append(y)



room=0
for i in range(1,7):
  tmp=boy.count(i)
  if tmp==0:
    continue
  elif tmp==1:
    room+=1
  else:
    room+=tmp//2+tmp%2
for i in range(1,7):
  girls=girl.count(i)
  if girls==0:
    continue
  elif girls==1:
    room+=1
  else:
    room+=girls//2+girls%2

print(room)