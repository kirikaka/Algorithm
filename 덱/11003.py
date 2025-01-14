import sys,math
from collections import deque

"""
nums에 크기가 l인 window로 뭐가 더 큰지 확인
최솟값을 확인하는 과정에서 시간복잡도를 O(n)으로 낮춰보자
새로 추가하는 원소가 window에 있는것보다 작으면 작거나 같은게 나올때 까지 pop한다. 
-> 틀리게나오므로 수정필요

"""

input=sys.stdin.readline
n,l=map(int,input().split())


queue=list(map(int,input().split()))
window=deque()

for i in range(n):
   #window의 가장 마지막에 넣을 것보다 크면 어차피 빼야함
  while window and window[-1][1]>queue[i]:
    window.pop()
  window.append([i,queue[i]])
  if window[0][0]<=i-l: #window head의 index에 따라 길이 판별.
    window.popleft()
  print(window[0][1],end=' ')

