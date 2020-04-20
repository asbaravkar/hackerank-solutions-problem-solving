def plusMinus(n,arr):
    p,ne,z=0,0,0
    for i in arr:
        if i<0:
            ne+=1
        elif i>0:
            p+=1
        else:
            z+=1
    print(p/n,"\n",ne/n,"\n",z/n)

n=int(input())
arr=[int(i) for i in input().split()]
plusMinus(n,arr)
