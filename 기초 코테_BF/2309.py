import itertools

key=[]
for _ in range(9):
  key.append(int(input()))

key.sort()

for i in itertools.combinations(key,7):
  if sum(i)==100:
    for j in sorted(i):
      print(j)
    break