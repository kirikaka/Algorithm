from sys import stdin, stdout

def solution(arr):
  arr.sort()
  print(arr)
  
input = stdin.readline 
arr=list(map(int,input().split()))
solution(arr)