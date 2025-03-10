import sys
input=sys.stdin.readline

n,m=map(int,input().split())

cctv=[]
office=[]

mode=[
  [],
  [[0],[1],[2],[3]],
  [[0,2],[1,3]],
  [[0,1],[1,2],[2,3],[0,3]],
  [[0,1,2],[1,2,3],[0,2,3],[0,1,3]],
  [[0,1,2,]],
]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
  tmp=list(map(int,input().split()))
  office.append()
  for j in range(m):
    if office[j] in [1,2,3,4,5]:
      cctv.append([tmp[j],i,j])

"""
사각 지대의 최소 크기. 카메라가 가능한 한 많은 곳을 비춰야한다. 
카메라가 항상 0이 많은 쪽을 비춰야할까? 
이중 리스트를 순회하며 1~5까지의 카메라를 찾을때마다 
해당 카메라가 만들 수 있는 최소 사각지대를 찾는다.
1일 때 : 상하좌우 모두 확인하기
2일 때 : 상하 or 좌우 확인하기
3일 때 : 상우 or 상좌 or 우하 or 좌하 확인하기
4일 때 : 상좌우 or 상하좌 or 상하우 or 하좌우 확인
5일 때 : 상하좌우 모두 더하기.

CCTV가 겹치면 어떡하지?
사각지대를 찾지말고 0을 #으로 만들까
그 다음에 0의 개수를 찾으면되려나 


CCTV종류와 x,y좌표를 가지는 리스트
백트래킹으로 회전가능한 모든 경우의 수를 구해야 한다.


"""