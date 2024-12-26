import sys

def check_row():
  res=0
  for i in range(5):
    cnt=0
    for j in range(5):
      if bingo[i][j]==1:
        cnt+=1
    if cnt==5:
      res+=1
  return res
      
def check_col():
  res=0
  for i in range(5):
    cnt=0
    for j in range(5):
      if bingo[j][i]==1:
        cnt+=1
    if cnt==5:
      res+=1

  return res

def check_cross():
  res=0
  cnt=0

  for i in range(5):
    if bingo[i][4-i]==1:
      cnt+=1
  if cnt==5:
    res+=1
    
  cnt=0
  for i in range(5):
    if bingo[i][i]==1:
      cnt+=1
  if cnt==5:
    res+=1
  return res
      
    
    
    
mine=[]
for _ in range(5):
  mine.append(list(map(int,sys.stdin.readline().split())))
mc=[]
for _ in range(5):
  mc+=list(map(int,sys.stdin.readline().split()))

bingo=[[0]*5 for _ in range(5)]


for i in range(25):
  for j in range(5):
    for k in range(5):
      if mc[i]==mine[j][k]:
        count=0
        bingo[j][k]=1
        
        count+=check_col()
        count+=check_row()
        count+=check_cross()
        if count>=3:
          print(i+1)
          exit()
        

  