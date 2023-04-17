# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
set1 = set(map(int,input().split()))

M = int(input())
set2 = set(map(int,input().split()))

set3 = set1.symmetric_difference(set2)

print(len(set3))
