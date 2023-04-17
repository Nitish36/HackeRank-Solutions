# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
l = list(map(int,input().split()))
set1 = set(map(int,input().split()))
set2 = set(map(int,input().split()))
ctr = 0
for i in l:
    if i in set2 or i in set2:
        ctr = ctr -1
    
    if i in set1 or i in set1:
        ctr = ctr + 1

print(ctr)
        
