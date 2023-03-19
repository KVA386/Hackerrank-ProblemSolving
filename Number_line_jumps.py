def kangaroo(x1, v1, x2, v2):
     
    if x1>x2 and v1>v2:
        return "NO" 
    else:
       count1=0
       count2=0
       
       for i in range(0,10000):

          sum1=x1+v1 
          x1=sum1 
          count1+=1 
          sum2=x2+v2 
          x2=sum2 
          count2+=1 

          if x1==x2:
            return "YES"
       else:
           return "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
