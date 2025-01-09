
import sys

input=sys.stdin.readline
n=int(input())
building=[]

for i in range(n):
  building.append(int(input()))

count=0
stack=[]
for b in building:
  while stack:
    if stack[-1]<=b:
      stack.pop()
    else:
      break
  stack.append(b)
  
  count+=len(stack)-1   #stack에 현재 빌딩보다 더 큰 빌딩만 남아 있으므로 count
  
print(count)