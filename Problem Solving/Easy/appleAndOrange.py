def countApplesAndOranges(s,t,a,b,dist_a,dist_b):
    count_a,count_b=0,0
    for i in range(len(dist_a)):
        if (a+dist_a[i]) in range(s,t+1):
            count_a+=1
    for i in range(len(dist_b)):
        if (b+dist_b[i]) in range(s,t+1):
            count_b+=1
    print(count_a)
    print(count_b)


s,t=map(int, input().split())
a,b=map(int, input().split())
m,n=map(int, input().split())
dist_a=[int(i) for i in input().split()]
dist_b=[int(i) for i in input().split()]
countApplesAndOranges(s,t,a,b,dist_a,dist_b)
