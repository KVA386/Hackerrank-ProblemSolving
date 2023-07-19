def getTotalX(a, b):
    count = 0
    for x in range(max(a), max(b) + 1):
        flag= True
        for i in a:
            if x % i != 0:
                flag = False
                break
        if flag:
            for j in b:
                if j % x != 0:
                    flag = False
                    break
        
        if flag:
            count+= 1
        
    return count

    
a=[2,6]
b=[24,36]
v=getTotalX(a,b)
print(v)