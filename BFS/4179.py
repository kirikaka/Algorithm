from collections import deque
import sys

input=sys.stdin.readline

r,c=map(int,input().split())

visit = [[False] * c for _ in range(r)] # 방문 여부
space=[[list(input().rstrip()) for _ in range(r)]] #입력받은 미로찾기



"""
벽으로 모두 막혀있으면 Impossible 출력

"""
