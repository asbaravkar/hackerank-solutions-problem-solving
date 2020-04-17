def minMaxSum(arr):
    minSum,maxSum=0,0
    for i in range(len(arr)-1):
        minSum+=arr[i]
        maxSum+=arr[len(arr)-1-i]
    print(minSum,maxSum)

arr=[int(i) for i in input().split()]
arr.sort()
minMaxSum(arr)
