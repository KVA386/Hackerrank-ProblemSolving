def minimumDistances(a):
    n=len(a)
    minimum=n+1        
    index=dict()   

    for i in range(n):
        if a[i] in index:
            if i-index[a[i]] < minimum :    #
                minimum = i-index[a[i]]
            index[a[i]]=i   
        else:
            index[a[i]]=i 
              
    if minimum==n+1:        #If no matching elements return -1
        return -1
    return minimum
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
