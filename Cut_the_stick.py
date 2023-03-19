def cutTheSticks(arr):
    # Write your code here
    print(len(arr))
    while len(arr)>1:
        min1=min(arr)
        list1=[]
        for i in range(0,len(arr)):
            
            if abs(arr[i]-min1)>0:
                list1.append(abs(arr[i]-min1))
        arr=list1 

        if len(arr)!=0:
         print(len(arr))
         
n=int(input())
a1=list(map(int,input().split()))[:n]
x=cutTheSticks(a1)


