import heapq as qq

_list=[32,16,54,94,81,31]
print(_list)

qq.heapify(_list)
qq.heappush(_list,7)
print(qq.heappop(_list))  #7

print(qq.heappushpop(_list,100))  #16

print(qq.heapify(_list))
