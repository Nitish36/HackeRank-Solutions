def count_substring(string, sub_string):
    
    ctr = 0
    for i in range(len(string)):
        ctr = ctr+string.count(sub_string,i,i+len(sub_string))
    return ctr

if __name__ == '__main__':
