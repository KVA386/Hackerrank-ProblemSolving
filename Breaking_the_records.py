'''

Input :
9
10 5 20 20 4 5 2 25 1

Output:
2 4

'''
import math
import os
import random
import re
import sys

def breakingRecords(scores):
    count1=0
    count2=0
    min1=scores[0] 
    max1=scores[0]
    for i in scores:
        if i<min1:
            count1+=1
            min1=i 
        if i>max1:
            count2+=1 
            max1=i   
        if i==min1 or i==max1:
            continue    
   
    return count2,count1

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
