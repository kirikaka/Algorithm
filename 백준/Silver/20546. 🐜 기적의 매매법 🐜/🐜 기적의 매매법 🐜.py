import sys

def bnp(money,price):
  stock=0
  money=money
  price=price
  for i in range(14):
    if money>=price[i]:
      stock+=money//price[i]
      money=money%price[i]
  
  result=money+stock*price[13]
  return result
  
def timing(money,price):
  stock=0
  money=money
  price=price
  up=0
  down=0
  for i in range(1,14):
    if price[i]<price[i-1]:
      up=0
      down+=1
    elif price[i]>price[i-1]:
      up+=1
      down=0
      
    if down>=3:
      stock+=money//price[i]
      money=money%price[i]
    
    elif up>=3:
      money+=price[i]*stock
      stock=0
    
  result=money+stock*price[13]
  return result

money=int(sys.stdin.readline())
price=list(map(int,sys.stdin.readline().split()))
bnp=bnp(money,price)
timing=timing(money,price)

if bnp<timing:
  print('TIMING')
elif bnp>timing:
  print('BNP')
else:
  print('SAMESAME')