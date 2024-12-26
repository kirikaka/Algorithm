from sys import stdin, stdout

def solution(arr):
  arr=list(set(arr))
  arr.sort(reverse=True)
  print(arr)
  
input = stdin.readline 
arr=list(map(int,input().split()))
solution(arr)