def insertionSort1(n, arr):
    
        temp=arr[n-1]

        for i in range(n-2,-1,-1):
            if arr[i]>temp:
                arr[i+1]=arr[i]
            else:
                arr[i+1]=temp
                break
            print(*arr)

        else:
            arr[0]=temp

        [print(i, end=' ') for i in arr]
        
arr=list(map(int,input().split()))

insertionSort1(len(arr),arr)
