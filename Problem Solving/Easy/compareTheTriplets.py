def compareTriplet(a,b):
    apt,bpt=0,0
    for i in range(len(a)):
        if a[i]>b[i]:
            apt+=1
        elif a[i]<b[i]: bpt+=1
    print(apt,bpt)

a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
compareTriplet(a,b)
