# -*- coding: utf-8 -*-
from collections import deque
import sys
input=sys.stdin.readline

# T=int(input())

# for _ in range(T):
#   n=int(input())
#   # student=[x for x in range(1,n+1)]
#   togo=list(map(int,input().split()))

#   visit=[False for _ in range(n)]
  
   
#   """
#   Cyclic 형태일 때는 팀을 이룰 수 있다. 
#   두 명이라면 서로 선택해야 Cyclic 이므로 서로 선택해야 팀이라고 본다. 
#   스스로 선택하면 하나의 팀이 될 수 있다.
  
#   어느 팀에도 속하지 않는 학생의 수를 계산해라?
  
#   togo를 순회하며 학생을 호출할 때마다 deque을 생성한다. deque에 넣는 것은 [호출자,지명자]
#   해당 학생이 원하는 학생으로 호출하고 호출당한 학생이 또 다른 학생을 호출한다.
#   호출해서 deque에 넣고 Cyclic인지 판단어케함?
  
#   deque의 첫 원소의 [0]과 마지막 원소의 [1]이 같은지 비교?
  
#   다르면 팀 없음 count + 1
  
  
#   - 순회로 접근했을 때만 visit True?
#   - 방문했으면 visit에 True로 변경.
#   - Cycle이 나온 경우 바로 break하고
#   - 
#   - 이미 방문한 원소면 continue
  
  

#   """
#   count=0
  
#   for i in range(n):
#     if i+1==togo[i]:  #스스로 한팀이 되어버린 경우
#       count+=1
#       continue
    
#     out=deque()
#     go=deque()
    
#     """
    
#     """
    
#     if not visit[i]:
#       visit[i]=True
#       out.append()
      
    
    
    

  # print("정답은: ",count)
  
def solve(n, students):
    visited = [False] * (n+1)
    in_cycle = [False] * (n+1)
    distance = [0] * (n+1)
    not_in_team = n

    for start in range(1, n+1):
        if not visited[start]:
            queue = deque([(start, 0)])
            path = []

            while queue:
                current, dist = queue.popleft()
                
                if visited[current]:
                    if not in_cycle[current]:
                        cycle_length = dist - distance[current]
                        for i in range(cycle_length):
                            in_cycle[path[len(path) - 1 - i]] = True
                            not_in_team -= 1
                    break

                visited[current] = True
                distance[current] = dist
                path.append(current)

                next_student = students[current]
                queue.append((next_student, dist + 1))

    return not_in_team

# 메인 코드
T = int(input())  # 테스트 케이스 수
for _ in range(T):
    n = int(input())  # 학생 수
    students = [0] + list(map(int, input().split()))  # 학생들이 선택한 학생 번호
    print(solve(n, students))