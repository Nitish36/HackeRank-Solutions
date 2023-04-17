cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a = 0
    b = 1
    l = []
    if n == 1:
        return [0]
    if n==0:
        return l
    l.append(a)
    l.append(b)
    c = 0
    for i in range(3,n+1,1):
        c = a+b
        l.append(c)
        a = b
        b = c
        
    return l
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
