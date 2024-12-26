nums=[]

for i in range(5):
  nums.append(int(input()))
  
nums.sort()

res=sum(nums)

print(res//5)
print(nums[2])