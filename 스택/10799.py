import sys

input=sys.stdin.readline
"""
레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ( ) 으로 표현된다. 
또한, 모든 ( ) 는 반드시 레이저를 표현한다.
쇠막대기의 왼쪽 끝은 여는 괄호 ( 로, 오른쪽 끝은 닫힌 괄호 ) 로 표현된다.

( 하나 들어오면 쇠막대기 하나라고 생각.
()이렇게 들어와야 레이저 이기 때문에.

step1. (가 들어올때 pipe에 그냥 넣는다.
step2. )가 들어올때 pipe의 rear가 (이며 인덱스가 하나차이면 레이저.
step3. pipe의 시작과 끝을 저장해 둔다. 

"""
batch=input().strip()
razer=[]
pipe=[]
res=0
pipes=0
for i in range(len(batch)):
  if batch[i]=='(':
    pipe.append([i,batch[i]])
    pipes+=1

  elif batch[i]==')' and pipe[-1][1]=='(' and pipe[-1][0]+1==i:
    pipe.pop()
    razer.append([i-1,i]) #레이저의 위치
    pipes-=1
    res+=pipes
    
  else:
    pipe.append([i,batch[i]]) #파이프의 끝
    pipes-=1
    res+=1

print(res)




## 시간초과 풀이
# batch=input().strip()
# razer=[]
# pipe=[]

# for i in range(len(batch)):
#   if batch[i]=='(':
#     pipe.append([i,batch[i]])

#   elif batch[i]==')' and pipe[-1][1]=='(' and pipe[-1][0]+1==i:
#     pipe.pop()
#     razer.append([i-1,i]) #레이저의 위치
#   else:
#     pipe.append([i,batch[i]]) #파이프의 끝


# # print(razer)


# pipes=[]
# start=0
# loc=[]
# for i in range(len(pipe)):
#   if pipe[i][1]=='(':
#     pipes.append([pipe[i][0]])
#     loc.append(start)
#     start+=1
#   else:
#     pipes[loc.pop()].append(pipe[i][0])
    
# # print(pipes)    

# res=0
# for i in pipes:
#   part=1
#   for j in razer:
#     if j[0]>i[0] and j[1]<i[1]:
#       part+=1
#   # print(i,"인 쇠파이프의 부러진 갯수",part)
#   res+=part
  

# print(res)