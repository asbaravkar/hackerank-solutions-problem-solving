def birthdayCakeCandles(n,arr):
    tall=max(arr)
    candles=arr.count(tall)
    return candles

n=int(input())
arr=[int(i) for i in input().split()]
print(birthdayCakeCandles(n,arr))
