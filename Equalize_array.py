def equalizeArray(arr):
    count=0
    li1=[]
    set1=set(arr)
    print(set1)
    for i in set1:
        li1.append(arr.count(i))
    print(li1)
    if len(set(arr))==len(arr):
        return len(arr)-1
    if len(set1)==1:
        return 0
    for i in li1:
        if i<max(li1):
            count+=i
    return count
    
x=int(input())
arr=list(map(int,input().split(" ")))
result=equalizeArray(arr)
print(result)
