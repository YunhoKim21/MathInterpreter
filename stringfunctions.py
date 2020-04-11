
def doesCharExist(input, char):
    value = 0
    for i in range(0, len(input)):
        if input[i] == "(":
            value += 1
        if input[i] == ")":
            value -= 1
        if input[i] == char and value == 0:
            return True
    return False
def checkBrackets(input):
    value=0
    for i in range(0, len(input)):
        if input[i]=="(":
            value+=1
        if input[i]==")":
            value-=1
        if value<0:
            return False
    if value==0:
        return True
    return False
def doesStringExist(input, char):
    value=0
    for i in range(0, len(input)):
        if input[i]=="(":
            value+=1
        if input[i]==")":
            value-=1
        if input[i:i+len(char)]==char and value==0:
            return True
    return False
def whereIsString(input, char):
    value=0
    for i in range(0, len(input)):
        if input[i]=="(":
            value+=1
        if input[i]==")":
            value-=1
        if input[i:i+len(char)]==char and value==0:
            return i
def isNumber(input):
    try:
        float(input)
        return True
    except:
        return False
def whereIsChar(input, char):
    value = 0
    input=input[::-1]
    for i in range(0, len(input)-1):
        if input[i] == "(":
            value += 1
        if input[i] == ")":
            value -= 1
        if input[i] == char and value == 0:
            return len(input)-i-1
    return False

def isThereBrackets(input):
    value = 0
    if len(input)==1 or len(input)==0:
        return False
    for i in range(0, len(input) - 1):
        if input[i] == "(":
            value += 1
        if input[i] == ")":
            value -= 1
        if value == 0:
            return False
    return True
def lastIndexOf(input, target):
    input=input[::-1]
    target=target[::-1]
    index=input.find(target)
    if index==-1:
        return -1
    return len(input)-index-len(target)
