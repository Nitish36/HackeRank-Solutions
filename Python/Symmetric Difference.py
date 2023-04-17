# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
set1 = set(map(int,input().split(' ')))
N = int(input())
set2 = set(map(int,input().split(' ')))

set3 = sorted(set1.symmetric_difference(set2))

for x in set3:
    print(x)
