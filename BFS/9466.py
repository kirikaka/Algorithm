from collections import deque
import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
  n=int(input())
  # student=[x for x in range(1,n+1)]
  togo=list(map(int,input().split()))

  visit=[False for _ in range(n)]
  
   
  """
  Cyclic ������ ���� ���� �̷� �� �ִ�. 
  �� ���̶�� ���� �����ؾ� Cyclic �̹Ƿ� ���� �����ؾ� ���̶�� ����. 
  ������ �����ϸ� �ϳ��� ���� �� �� �ִ�.
  
  ��� ������ ������ �ʴ� �л��� ���� ����ض�?
  
  togo�� ��ȸ�ϸ� �л��� ȣ���� ������ deque�� �����Ѵ�. deque�� �ִ� ���� [ȣ����,������]
  �ش� �л��� ���ϴ� �л����� ȣ���ϰ� ȣ����� �л��� �� �ٸ� �л��� ȣ���Ѵ�.
  ȣ���ؼ� deque�� �ְ� Cyclic���� �Ǵܾ�����?
  
  deque�� ù ������ [0]�� ������ ������ [1]�� ������ ��?
  
  �ٸ��� �� ���� count + 1
  
  
  - ��ȸ�� �������� ���� visit True?
  - �湮������ visit�� True�� ����.
  - Cycle�� ���� ��� �ٷ� break�ϰ�
  - 
  - �̹� �湮�� ���Ҹ� continue
  
  """
  count=0
  
  for i in range(n):
    if i+1==togo[i]:  #������ ������ �Ǿ���� ���
      count+=1
      continue
    
    out=deque()
    go=deque()
    
    """
    
    """
    
    if not visit[i]:
      visit[i]=True
      
      
    
    
    

  print("������: ",count)
  
  