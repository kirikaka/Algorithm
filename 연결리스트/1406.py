import sys
input=sys.stdin.readline
"""
L : 커서 왼쪽옮김
D : 커서 오른쪽 옮김
B : 커서 왼쪽 문자 삭제
P $ : $라는 문자를 커서 왼쪽에 추가.

"""

#시간 초과 풀이

# str_l=list(input().strip())
# m=int(input())
# n=len(str_l)
# cursor=n
# for i in range(m):
#   command=input().split()

#   if command[0]=='L' and cursor>0:
#     cursor-=1
#   elif command[0]=='D' and cursor<n:
#     cursor+=1
#   elif command[0]=='B' and cursor>0:
#     str_l.pop(cursor-1)
#     cursor=cursor-1
#   elif command[0]=='P':
#     str_l.insert(cursor,command[1])
#     cursor+=1
    
    
# print("".join(str_l))


# 스택을 이용한 풀이
# 커서가 이동하면 오른쪽 스택에 쌓아둔다


left = list(input().strip())
right = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right[::-1]
print(''.join(answer))