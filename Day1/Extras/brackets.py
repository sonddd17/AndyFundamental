

keys = [')','(','}','{',']','[']
def isBallance(text):
    counts = {}
    texts = text.lower().replace(" ","")
    
    for i in range (0,len(texts)):
        if texts[i] in keys:
            counts[i] = texts[i]
    print(counts[0])
    if counts.get(0) != counts.get(len(texts)-1):
        return False
    return True
    # for key, value in counts:
        

print(isBallance("(a[b]{c})"))


def is_balanced_simple(text):
    stack = []
    for char in text:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

