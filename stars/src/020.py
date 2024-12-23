

pairs = {")":"(", "]":"[", "}":"{"}


def isValid(string: str):
    stack = []
    for char in string:
        if char in pairs:
            top = stack.pop() if stack else " "
            if pairs[char] != top:
                return False
            continue
        stack.append(char)
    return not stack


if __name__ == "__main__":
    string1 = "[{(())}]"
    string2 = "[((({}))]"
    string3 = "]){())}"
    
    print(isValid(string1))
    print(isValid(string2))
    print(isValid(string3))
    pass
    
    