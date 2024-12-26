n=int(input())

history=set()
for _ in range(n):
  tmp=input().split()
  if tmp[0] in history:
    history.remove(tmp[0])
  else:
    history.add(tmp[0])
  
li=list(history)

li.sort(reverse=True)
for i in li:
  print(i)