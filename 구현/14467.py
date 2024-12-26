import sys

n=int(sys.stdin.readline())

count={}
cnt=0
for _ in range(n):
  cow,cross=sys.stdin.readline().split()
  if cow not in count.keys():
    count[cow]=cross
    continue
  if count[cow]!=cross:
    count[cow]=cross
    cnt+=1
    
print(cnt)
  