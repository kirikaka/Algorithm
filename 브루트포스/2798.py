n,m=map(int,input().split())
cards=list(map(int,input().split()))

lens=len(cards)
result=0
for i in range(lens):
  for j in range(i+1,lens):
    for k in range(j+1,lens):
      if cards[i]+cards[j]+cards[k]>m:
        continue
      else:
        result=max(result,cards[i]+cards[j]+cards[k])
    
print(result)