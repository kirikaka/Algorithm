n=int(input())

nums=list(map(int,input().split()))

nums_set=list(set(nums))
nums_set.sort()

dictList = dict(zip(nums_set,list(range(len(nums_set)))))

for i in nums:
  print(dictList[i],end=" ")
      
