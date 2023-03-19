def permutationEquation(P):
    # Write your code here
    list1=[]
    p1=P.copy()
    p1.sort()
    
    for i in range(len(p1)):
        x=(P.index(p1[i]))+1
        y=P.index(x)+1
        list1.append(y)

    for i in list1:
        print(i)

n=int(input())
P=list(map(int,input().split())) 
permutationEquation(P)
