def maximumToys(money,costs):
    total_money,track=0,0
    for i in costs:
        total_money+=i
        track+=1
        if total_money>money:
            total_money-=i
            track-=1
    return track


n,money=[int(i) for i in input().split(' ')]
costs=[int(i) for i in input().split(' ')]
# 1 12 5 111 200 1000 10
costs.sort()
# print(costs)
print(maximumToys(money,costs))
