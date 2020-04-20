import math
s=input()
n=int(input())
a_per_word=s.count('a')
count=math.floor(n/len(s))
total_count_a=count*a_per_word
remaining_length=n%len(s)
for a in range(remaining_length):
    if s[a]=='a':
        total_count_a+=1
print(total_count_a)
