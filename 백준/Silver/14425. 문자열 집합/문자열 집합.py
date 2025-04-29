n,m=map(int,input().split())

n_string=set()
for i in range(n):
  n_string.add(input().rstrip())

cnt=0
for i in range(m):
  tmp=input().rstrip()
  if tmp in n_string:
    cnt+=1
    
print(cnt)
  
  
