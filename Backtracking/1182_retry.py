import sys
input=sys.stdin.readline

n,s=map(int,input().split())

nums=list(map(int,input().split()))

count=0
def back(i,sum):
  if i>=n:
    return 
  
"""
 한 분기를 더 들어갈지말지
 다음 원소를 더할지 말지 고민하는 과정이 필요하다. 
"""