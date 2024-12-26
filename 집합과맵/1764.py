n,m=map(int,input().split())

n_name=set()
for i in range(n):
  n_name.add(input())

m_name=set()
for j in range(m):
  m_name.add(input())
  
li=list(n_name&m_name)
li.sort()

print(len(li))
for i in li:
  print(i)