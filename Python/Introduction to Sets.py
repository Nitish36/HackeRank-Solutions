def average(array):
    # your code goes here
    filtered_content = set(array)
    sum = 0
    avg = 0
    for i in filtered_content:
        sum = sum + i
    
    avg = sum/len(filtered_content)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
