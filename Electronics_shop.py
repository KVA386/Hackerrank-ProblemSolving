def getMoneySpent(keyboards, drives, b):
    for i in keyboards:
        if i>=b:
            keyboards.remove(i)
    for i in drives:
        if i>=b:
            drives.remove(i)
    count=0
    li1=[]
    for i in range(0,len(keyboards)):
        for j in range(0,len(drives)):
            if (keyboards[i]+drives[j])<=b:
                x=(keyboards[i],drives[j])
                li1.append(x)
    if len(li1)==0:
        return -1
    li2=[]
    for i in range(0,len(li1)):
        li2.append(sum(li1[i]))
    print(max(li2))
b=int(input()) 
keyboards = list(map(int, input().rstrip().split())) 
drives = list(map(int, input().rstrip().split()))
getMoneySpent(keyboards, drives, b)

