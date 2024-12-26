"""
  올바른 체스판의 예시를 만들어 두고 하나씩 비교해본다.
  
"""


n,m=map(int,input().split())
chess=[]
for _ in range(n):
  chess.append(list(input()))

white_chess=[
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
]
black_chess=[
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
]
 
min_count=1e9


for i in range(n-7):
  for j in range(m-7):
    temp_chess=[lst[j:j+8] for lst in chess[i:i+8]]
    black=0
    white=0
    
    for x in range(8):
      for y in range(8):
        if temp_chess[x][y]!=black_chess[x][y]:
          black+=1
           
        if temp_chess[x][y]!=white_chess[x][y]:
          white+=1
           
           
    count=min(black,white)
    if count < min_count:
      min_count = count
    
        
        
print(min_count)