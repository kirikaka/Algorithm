import sys

answer={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30}

student=[]
for i in range(28):
  n=int(sys.stdin.readline())
  student.append(n)

student=set(student)
for i in answer:
  if i not in student:
    print(i)