def kangaroo(x1,v1,x2,v2):
    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"

x1,v1,x2,v2=map(int,input().split())
print(kangaroo(x1,v1,x2,v2))
