

def isvalid(s):
    if len(s) % 2 == 1:
        return False
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = list()
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
            print(ch)
        else:
            stack.append(ch)
            print(stack)
    return not stack


if __name__ == '__main__':
    string = '({[]})'
    print(isvalid(string))



