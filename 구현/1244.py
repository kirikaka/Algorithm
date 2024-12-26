import sys

n=int(sys.stdin.readline()) #스위치 개수
switch=list(map(int,sys.stdin.readline().split())) #스위치 상태


def change(state):
  res=0
  if state==1:
    res= 0
  elif state==0:
    res= 1
  return res

def boy(num):
  global switch
  for i in range(n):
    if (i+1)%num==0:
      switch[i]=change(switch[i])
  
def girl(num):
  global switch

  switch[num-1]=change(switch[num-1])
  for i in range(0,n//2):
    if (num-i-1)<0 or (num-1+i)>=n:
      continue
    if (switch[num-1-i] == switch[num-1+i]):
      switch[num-1-i]=change(switch[num-1-i])
      switch[num-1+i]=change(switch[num-1+i])
    else:
      break
    
  

ns=int(sys.stdin.readline()) #학생 수
for _ in range(ns):
  sex,num=map(int,sys.stdin.readline().split())
  if sex==1:
    boy(num)
  elif sex==2:
    girl(num)
  
    
for i in range(n):
  print(switch[i],end=' ')
  if (i+1)%20==0:
    print()
