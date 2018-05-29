def balanced_bracket(input):
    matching = { ")":"(", "}":"{", "]":"["}
    stack = []
    for bracket in input:
        if bracket not in matching.values():
            if top(stack) == matching[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)
    return True
    
def top(stack):
    if stack !=[]:
        return stack[-1]
    else:
        return None
print(balanced_bracket('()[]{}(([])){[()][]}'))
print(balanced_bracket('())[]{}'))
print(balanced_bracket('[(])'))