# Enter your code here. Read input from STDIN. Print output to STDOUT
N =int(input())
stamp = []
for i in range(N):
    s = input()
    stamp.append(s)
set_stamp = set(stamp)

print(len(set_stamp))
