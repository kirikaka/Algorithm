n=int(input())


nums=[]
while True:
  
  
  if(n//10==0):
    cha=n%10
    nums.append(cha)
    break
  
  cha=n%10
  nums.append(cha)
  n=(n-cha)//10
  
    
nums.sort(reverse=True)  
for i in nums:
  print(i,end="")