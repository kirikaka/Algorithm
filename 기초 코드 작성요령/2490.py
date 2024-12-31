import sys
input=sys.stdin.readline

def yoot(draw):
  su=sum(draw)
  if su==0:
    print('D')
  elif su==1:
    print('C')
  elif su==2:
    print('B')
  elif su==3:
    print('A')
  elif su==4:
    print('E')



for _ in range(3):
  draw=list(map(int,input().split()))
  yoot(draw)
