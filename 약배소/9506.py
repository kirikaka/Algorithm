while True:
  n=int(input())
  if n==-1:
    break
  
  s=[]
  for i in range(1,n):
    if n%i==0:
      s.append(i)
      
  if sum(s)==n:
    print(n,"= ",end="")
    for k in range(len(s)-1):
      print(s[k],"+ ",end="")
    print(s[-1])
  else:
    print(n,"is NOT perfect.")