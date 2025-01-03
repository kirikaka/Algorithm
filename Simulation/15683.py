import sys
input=sys.stdin.readline

n,m=map(int,input().split())

cam=[]
for _ in range(n):
  cam.append(list(map(int,input().split())))


def left(cam,row,col):
  check=cam[row]
  loc=0
  for i in range(col):
    if check[i]==6:
      loc=i+1
      
      
  cam[row][loc:col] = ["#"] * (col-(loc))
  

def right(cam,row,col):
  check=cam[row]
  loc=0
  for i in range(m):
    if check[i]==6:
      loc=i
      
  cam[row][col+1:loc] = ["#"] * (loc - col)
  

def up(cam,row,col):
  check=[i[col] for i in cam][:row] #세로 열 추출 
  loc=0
  for i in range(m):
    if check[i]==6:
      loc=i
      
  wall=check[col:loc]
  zeros=wall.count(0)
  return zeros

def down(cam,row,col):
  check=[i[col] for i in cam][row+1:] #세로 열 추출
  loc=0
  for i in range(m):
    if check[i]==6:
      loc=i
      
  wall=check[col:loc]
  zeros=wall.count(0)
  return zeros


left(cam,2,2)
print(cam)

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

"""