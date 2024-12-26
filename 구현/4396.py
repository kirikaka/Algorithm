import sys

n=int(sys.stdin.readline())

dx=[-1,0,1,-1,1,-1,0,1]
dy=[-1,-1,-1,0,0,1,1,1]

answer=[]
for _ in range(n):
  answer.append(list(sys.stdin.readline().strip()))
  
now=[]
for _ in range(n):
  now.append(list(sys.stdin.readline().strip()))


def check_bomb(i,j):
  count=0
  for d in range(8):
    nx=i+dx[d]
    ny=j+dy[d]
    if nx<0 or ny<0 or nx>=n or ny>=n:
      continue
    if answer[nx][ny]=='*':
      count+=1
  return count



for i in range(n):
  for j in range(n):
    if answer[i][j]=='.':
      answer[i][j]=check_bomb(i,j)


result=[]
for i in range(n):
  temp=[]
  for j in range(n):
    if now[i][j]=='x':
      temp.append(answer[i][j])
    else:
      temp.append(now[i][j])
  result.append(temp)

for i in range(n):
  for j in range(n):
    if result[i][j]=='*':
      for x in range(n):
        for y in range(n):
          if answer[x][y]=='*':
            result[x][y]='*'
            

for i in range(n):
    for j in range(n):
        print(result[i][j], end='')
    print()
        
  
      
