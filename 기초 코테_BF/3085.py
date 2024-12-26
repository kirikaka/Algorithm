n=int(input())
candy=[]
for _ in range(n):
  candy.append(list(input()))

def count_candy():
  max_count=0
  for x in range(n):
    for y in range(n-1):
      max_count+=1
      
      

for x in range(n):
  for y in range(n):
    if y+1<n:
      candy[x][y]