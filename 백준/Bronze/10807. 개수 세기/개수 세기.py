num=int(input())
b=input().split()
a=[int(x) for x in b]
need=int(input())

count=0
for i in a:
  if i == need:
    count+=1
print(count)