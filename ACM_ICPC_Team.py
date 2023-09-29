n,m=list(map(int,input().split(" ")))
li2=[]

for i in range(0,n):
    n1=str(input().strip(""))
    li2.append(n1)

count1=[]
for i in range(len(li2)-1):
        for j in range(i+1,len(li2)):
            count=0
            for k in range(m):
                if  li2[i][k]=="1" or li2[j][k]=="1":
                   count+=1
            count1.append(count)
            
max1=max(count1)
print(max1) 
print(count1.count(max1))






