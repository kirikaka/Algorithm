a=[]
for _ in range(9):
  a.append(list(map(int,input().split())))

max_num=0
x,y=0,0
for i in range(9):
  for j in range(9):
    if a[i][j]>=max_num:
      max_num=a[i][j]
      x,y=i+1,j+1

print(max_num)
print(x,y)