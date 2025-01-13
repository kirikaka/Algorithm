import sys,math
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())
need=list(map(int,input().split()))
nums=deque(range(1,n+1))


  
"""
- 첫번째 연산 : popleft 후 n을 줄이기.
- 두번째 연산 : popleft 후 append
- 세번째 연산 : pop 후 appendleft
nums 리스트의 첫 원소가 need의 첫 원소가 아니면 
second나 third 연산중 하나를 한다. 
[1] n-nums[0] + need[0] 과 [2] nums[0]-need[0] 중에 
1이 더 작으면 second연산, 2가 더작으면 third 연산
"""


count=0
for i in need:  # 뽑아내려는 수의 위치 하나씩 반복문 돌리기
    while True:     # 뽑을 때까지 계속 돌리기
        if nums[0] == i:  # dq의 첫인덱스가 뽑아내려는 수의 위치와 같다면 1번 수행
            nums.popleft()
            break
        else:
            if nums.index(i) < len(nums)/2:  # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 작을때는 왼쪽으로 움직여야 최소
                while nums[0] != i:   # dq의 첫번째 인덱스가 i와 같아질때까지 반복
                    nums.append(nums.popleft())  
                    count += 1
            else:   # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 클때는 오른쪽으로 움직여야 최소
                while nums[0] != i:
                    nums.appendleft(nums.pop())  
                    count += 1

print(count)