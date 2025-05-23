from collections import deque

n,k=map(int,input().split())
que=deque()
visit=[False]*100001

que.append([n,0])

while True:
    num,cnt=que.popleft()
    if num==k:
        break
    if num>=0 and num<100001:
        if not visit[num]:
            que.append([num-1,cnt+1])
            que.append([num+1,cnt+1])
            que.append([num*2,cnt+1])
            visit[num]=True

print(cnt)