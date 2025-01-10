import sys
input=sys.stdin.readline

n,m,k=map(int,input().split()) #노트북 세로,가로,스티커 개수


sticker=[]

for i in range(k):
  R,C=map(int,input().split()) #스티커가 붙은 모눈종이 크기
  tmp=[]
  for _ in range(R):
    tmp.append(list(map(int,input().split())))
  sticker.append(tmp)
  
dx=[-1,0,1,0]
dy=[0,1,0,-1]


