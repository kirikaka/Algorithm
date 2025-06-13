import sys
input=sys.stdin.readline

n=int(input())

def strfry(a,b):
  res=True

  a=sorted(a)
  b=sorted(b)
  if len(a)!=len(b):
    return False
  
  for i in range(len(a)):
    if not a[i]==b[i]:
      res=False

  
  return res

for _ in range(n):
  a,b=input().split()
  res=strfry(a,b)
  if res:
    print('Possible')
  else:
    print('Impossible')
