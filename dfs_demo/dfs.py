import copy
result=[0]*3
arr=[[1,2,3],[4,5],[7,8,9]]
res=[]
def dfs(arr, depth):
    global res
    for i in range(len(arr[depth])):
        result[depth] = arr[depth][i]
        if depth != len(arr) - 1:
            dfs(arr, depth + 1)
        else:
            res.append(result.copy())

COUNT=0  
def perm(n,begin,end):  
    global COUNT,res
    if begin>=end:  
        res.append(n)
    else:  
        i=begin  
        for num in range(begin,end):  
            n[num],n[i]=n[i],n[num] 
            perm(n.copy(),begin+1,end)
            n[num],n[i]=n[i],n[num]
res=[]
N=8
n=[i for i in range(N)]
perm(n,0,len(n))

def check(l):
    return len(set(l))==len(l)

result = []

for i in res:
    s = [i[j]+j for j in range(N)]
    c = [i[j]-j for j in range(N)]
    if check(s) and check(c):
        print(i)
        result.append(i)

print(len(result))