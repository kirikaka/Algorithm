import sys
input=sys.stdin.readline
n=int(input())
sys.setrecursionlimit(10 ** 4)

"""
queen은 상하좌우대각선 모두 공격가능
같은 열 불가, 같은 행 불가
대각선 불가
[행 index+1,열 index+1],[행 index-1,열 index-1] 불가
[행 index-1,열 index+1],[행 index+1,열 index-1] 불가
현재 행이 보드판 사이즈(n)보다 크면 가능한 방법 한 가지 찾았다 생각해 1을 리턴.
현재 칸의 열, 대각선, reverse대각선(오른쪽 위로)에 퀸이 놓아져 있으면 다음 열로 넘어간다.
현재 칸에 퀸을 놓을 수 있으면 row,col을 계산해서 열,대각선,reverse대각선에 넣는다


"""
cnt=0

def chess(row,cross,cross_reverse,cols):
  global n
  if row==n:
    
    return 1
  
  sol = 0
  for col in range(n):
    curr_cross= row-col #현재 기준 Right to left 아래 대각선은 행-열
    curr_cross_reverse=row+col #현재 기준  Left to right 대각선은 열과 행 더하기
    
    
    if (col in cols or curr_cross in cross or curr_cross_reverse in cross_reverse):
      continue
    
    cols.add(col)
    cross.add(curr_cross)
    cross_reverse.add(curr_cross_reverse)
    sol+=chess(row+1,cross,cross_reverse,cols)
    
    #만약에 return이 나오면 되돌아가면서 set에서 추가했던 요소를 삭제한다..
    cols.remove(col)
    cross.remove(curr_cross)
    cross_reverse.remove(curr_cross_reverse)
  
  return sol

print(chess(0,set(),set(),set()))