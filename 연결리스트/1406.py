import sys

str_l=list(sys.stdin.readline().strip())
n=int(sys.stdin.readline())

for i in range(n):
  command=sys.stdin.readline().split()
  if command[0]=='L' 