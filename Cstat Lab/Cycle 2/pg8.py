def vaild_paranthesis(s):
    stack = []
    pairs = {")" : "(", "}" : "{", "]" : "["}

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            stack.pop()
        else:
            return false

    return not stack

expr = input("Enter para : ")
if vaild_paranthesis(expr):
    print("valid")
else:
    print("invalid")
