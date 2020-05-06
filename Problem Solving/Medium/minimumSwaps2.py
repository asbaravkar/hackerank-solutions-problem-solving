
def minimumSwaps(a):
    counter = 0
    temp = [0]*len(a)

    for i,v in enumerate(a): # index of a as value in temp
        temp[v-1] = i
    
    for i in range(len(a)):
        if a[i] != i+1:
            t = temp[i]
            a[i],a[t] = a[t], a[i]
            temp[i],temp[a[t]-1] = temp[a[t]-1],temp[i]
            counter += 1
    return counter

n=int(input())
a=[int(i) for i in input().split(' ')]
print(minimumSwaps(a))
