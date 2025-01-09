import sys
input=sys.stdin.readline

"""
이중 반복문 쓰면 시간 초과날텐데
스택으로 어떻게 할수 있는 방법이 없을까?
일단 입력받은거에서 하나 pop(=cur)
안에 있는 원소 수만큼 pop한뒤 razer에 추가
razer에최근에 들어온 원소(= 마지막 [-1])과 cur 비교해서 cur보다 크면 res에 넣기
모든 원소 pop후 razer을 뒤집어서 다시 tower 함수 호출
같은 방식은 메모리 초과
"""
n=int(input())
tower=list(map(int,input().split()))


# def towers(tower):
#   global ans
#   if not tower:
#     return
#   razer=[]
#   res=[]
#   cur=tower.pop()
#   for _ in range(len(tower)):
#     razer.append(tower.pop())
#     if razer[-1]>cur:
#       res.append(len(tower)+1)

#   if not res:
#     ans.append(0)
#   else:  
#     ans.append(res[0])
#   need=razer[::-1]

#   towers(need)
  
# towers(tower)

"""
모노토닉 스택?\
특정 수보다 가장 가까이 크거나 작은 수를 알 수 있는 모노 토닉 스택.
`지금 넣으려는 탑보다 낮은 탑은 영원히 필요없으므로 제거한다`가 힌트



"""
mono=[]
arr_index=[0]*n

for i in range(n):
  while mono: #모노토닉 스택에 아무것도 없을때 까지
    if mono[-1][1]>tower[i]: #스택 가장 위와 타워와 비교 스택 top이 더크면
      arr_index[i]=mono[-1][0]+1 #스택 top의 index를 정답에[ 넣기]
      break
    else:
      mono.pop() #모노 스택이 더 클때까지 원소 pop해버리기
  mono.append([i,tower[i]])      #모노가 더 작으면 원소 추가.
  
print(' '.join(map(str, arr_index)))