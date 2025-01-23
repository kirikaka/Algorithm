
      


from collections import deque
import sys

input=sys.stdin.readline

n,k=map(int,input().split())

"""
걸으면 x-1 or x+1
순간이동하면 그 위치에서 x*2
힌트
수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.
왜 BFS 일까?  큐에 뭘 넣는거야?
방문 리스트를 만들어놓고? 걸린 시간을 쓰기.

1. 시작 위치를 큐에 넣기
1-1. 시간을 방문 리스트에 기록
2. 큐에서 popleft
3. 팝한것에서 +,-1한 것과 두배 한것 모두 큐에 넣기.
4. 방문안했으면 방문 시간과 que에 넣기



"""
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
  
      






