def is_valid(s):
    stack = []
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif char == '}':
            if not stack or stack[-1] != '{':
                return False
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

while True:
    s = input("Enter the input string: ")
    b = is_valid(s)
    if b:
        print("Valid String")
    else:
        print("Invalid String")
