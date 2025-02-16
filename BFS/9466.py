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
#   Cyclic ������ ���� ���� �̷� �� �ִ�. 
#   �� ���̶�� ���� �����ؾ� Cyclic �̹Ƿ� ���� �����ؾ� ���̶�� ����. 
#   ������ �����ϸ� �ϳ��� ���� �� �� �ִ�.
  
#   ��� ������ ������ �ʴ� �л��� ���� ����ض�?
  
#   togo�� ��ȸ�ϸ� �л��� ȣ���� ������ deque�� �����Ѵ�. deque�� �ִ� ���� [ȣ����,������]
#   �ش� �л��� ���ϴ� �л����� ȣ���ϰ� ȣ����� �л��� �� �ٸ� �л��� ȣ���Ѵ�.
#   ȣ���ؼ� deque�� �ְ� Cyclic���� �Ǵܾ�����?
  
#   deque�� ù ������ [0]�� ������ ������ [1]�� ������ ��?
  
#   �ٸ��� �� ���� count + 1
  
  
#   - ��ȸ�� �������� ���� visit True?
#   - �湮������ visit�� True�� ����.
#   - Cycle�� ���� ��� �ٷ� break�ϰ�
#   - 
#   - �̹� �湮�� ���Ҹ� continue
  
  

#   """
#   count=0
  
#   for i in range(n):
#     if i+1==togo[i]:  #������ ������ �Ǿ���� ���
#       count+=1
#       continue
    
#     out=deque()
#     go=deque()
    
#     """
    
#     """
    
#     if not visit[i]:
#       visit[i]=True
#       out.append()
      
    
    
    

  # print("������: ",count)
  
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

# ���� �ڵ�
T = int(input())  # �׽�Ʈ ���̽� ��
for _ in range(T):
    n = int(input())  # �л� ��
    students = [0] + list(map(int, input().split()))  # �л����� ������ �л� ��ȣ
    print(solve(n, students))