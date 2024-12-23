
def func(string):
    right = 0
    left  = 0
    max_length = 0
    for i in range(len(string)):
        right = i
        if string[right] not in string[left:right]:

            max_length += 1
            print(string[left:max_length])
            continue
        
        max_length = max(max_length, right-left)
        step = string.find(string[right], left)
        left += (step+1)
        
def func2(string):
    right = 0
    left  = 0
    max_length = 0
    for i in range(len(string)):
        right = i
        if string[right] in string[left:right]:
            
            index = string.find(string[right], left)
            left = index+1
            print(string[left:right+1])
            
            max_length = max(max_length, right-left+1)
            continue
        
        max_length += 1
        print(string[left:right+1])
        
        
    

if __name__ == "__main__":
    print(func2("abcadbcbb"))  # 输出: 3
    # print(func("bbbbb"))     # 输出: 1
    # print(func("pwwkew"))    # 输出: 3
