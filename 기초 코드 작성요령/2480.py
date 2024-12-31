import sys
input=sys.stdin.readline

nums=list(map(int,input().split()))

cnt=1
ans=[]
need=0
for i in nums:
  if i in ans:
    cnt+=1
    need=i
    continue
  else:
    ans.append(i)

ans.sort()
if cnt==3:
  print(need*1000+10000)
elif cnt==2:
  print(need*100+1000)
elif cnt==1:
  print(ans[-1]*100) 