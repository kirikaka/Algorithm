import sys
input=sys.stdin.readline

n=int(input())
oasis=[]
for _ in range(n):
  oasis.append(int(input()))

"""
첫째 줄에 줄에서 기다리고 있는 사람의 수 N이 주어진다. (1 ≤ N ≤ 500,000)
O(nlogn)가 최대

현재 사람보다 큰 사람만 stack에 보관하면 풀 수 있었다.
0. 스택에 키와 몇번째 사람인지를 같이 저장한다. 
1. stack[-1]이 현재 사람보다 작으면 팝
2. 스택이 비어잇으면 그냥 추가
3. 

"""
stack=[]
count=0

height,cnt=0,1
for i in oasis:
  while stack and stack[-1]<i:
    stack.pop()
    
    count+=1
  if stack and stack[-1]==i:
    count+=1
    
