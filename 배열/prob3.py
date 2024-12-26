from sys import stdin, stdout

def solution(arr):
  ans=[]
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      ans.append(arr[i]+arr[j])
      
  ans=sorted(list(set(ans)))
  print(ans)
  
input = stdin.readline 
arr=list(map(int,input().split()))
solution(arr)