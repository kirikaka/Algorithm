n,m=map(int,input().split())

res=[]

def backtrack():
    if len(res)==m:
        print(' '.join(map(str,res)))
        return

    for i in range(1,n+1):
        if i not in res:
            res.append(i)
            backtrack()
            res.pop()

backtrack()