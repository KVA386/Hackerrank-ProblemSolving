def camelcase(s):
    ch=''
    li1=[]
    for i in s:  
        if i!=i.upper():
            ch+=i 
        else:
            li1.append(ch)
            ch=''
            ch+=i
    else:
        li1.append(ch)       
    print(len(li1))
s=input()
camelcase(s)
