increment_list=[0 for x in range(110)]
number_of_socks=int(input())
color_list=[int(x) for x in input().split()]
for color in color_list:
    increment_list[color]+=1
ans=0
for i in increment_list:
    if i>1:
        ans+=i//2
print(ans)
