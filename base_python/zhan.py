#栈--默写练习

def is_valid(s):
    pairs = {")":"(","]":"[","}":"{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if top != pairs[ch]:
                return False
        else:
            stack.append(ch)
    if len(stack) == 0:
        return True
    else:
        return False