import polynomial
import solve

variableArray = []
recent = polynomial.polynomial()


class Variable:
    def __init__(self, functionBody, functionName):
        self.functionBody = functionBody
        self.functionName = functionName


a = polynomial.polynomial()


def factorial(n):
    if n == 0:
        return 1
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac
def twotwo(n):
    sum=1
    for i in range(1, n+1):
        if(n%2==1):
            sum*=i
    return sum


for i in range(0, 50):
    if i % 4 == 1:
        a.coefArr[i] = 1 / factorial(i)
    if i % 4 == 3:
        a.coefArr[i] = -1 / factorial(i)
b = Variable(a, "sin")
variableArray.append(b)
a = polynomial.polynomial()
for i in range(0, 50):
    if i % 4 == 2:
        a.coefArr[i] = -1 / factorial(i)
    if i % 4 == 0:
        a.coefArr[i] = 1 / factorial(i)
b = Variable(a, "cos")
variableArray.append(b)
a = polynomial.polynomial()
for i in range(0, 50):
    a.coefArr[i] = 1 / factorial(i)
b = Variable(a, "exp")

variableArray.append(b)
a = polynomial.polynomial()
a.coefArr[0] = 3.14159265358979
b = Variable(a, "PI")
variableArray.append(b)
a = polynomial.polynomial()
a.coefArr[0] = 2.71828182846
b = Variable(a, "e")
variableArray.append(b)

a=polynomial.polynomial()
for i in range(0, 50):
    if i % 2 == 0:
        a.coefArr[i] = 1 / factorial(i)
b=Variable(a, "cosh")
variableArray.append(b)
a=polynomial.polynomial()
for i in range(0, 50):
    if i % 2 == 1:
        a.coefArr[i] = 1 / factorial(i)
b=Variable(a, "sinh")
variableArray.append(b)
'''
a = polynomial.polynomial()
for i in range(0, 8):
    if i==0:
        a.coefArr[i]=1
    elif i==1:
        a.coefArr[i]=1/2
    elif i%2==0:
        a.coefArr[i]=-factorial(2*i -3)/(factorial(i)*factorial(i-2)*2**(2*i-2))
    else:
        a.coefArr[i]=factorial(2*i-3)/(factorial(i)*factorial(i-2)*2**(2*i-2))
b = Variable(a, "sqrt")
'''
variableArray.append(b)
def addValue(sentence):
    index = sentence.find("=")
    valueName = sentence[0:index].strip()
    for i in range(0, len(variableArray)):
        if variableArray[i].functionName == valueName:
            functionBody = solve.solve(sentence[index + 1:])
            if functionBody.isError:
                return functionBody
            variableArray[i].functionBody = functionBody
    if "+" in valueName or "-" in valueName or "*" in valueName or "/" in valueName or "^" in valueName or " " in valueName:
        print("Error : invalid variable name 1")
        ret = polynomial.polynomial()
        ret.isError = True
        ret.errorCode = 7
        return ret
    if "integrate" in valueName or "derivate" in valueName or "show variable" in valueName or "to" in valueName or "from" in valueName or "Canvas" in valueName or "ans" in valueName:
        print("Error : invalid variable name 2")
        ret = polynomial.polynomial()
        ret.isError = True
        ret.errorCode = 7
        return ret
    if "x"==valueName or "game"==valueName or "exit"==valueName:
        print("Error : invalid variable name ")
        ret = polynomial.polynomial()
        ret.isError = True
        ret.errorCode = 7
        return ret
    try:
        float(valueName)
        print("Error : can't assign to literal")
        ret = polynomial.polynomial()
        ret.isError = True
        ret.errorCode = 8
        return ret
    except:
        pass
    valueBody = solve.solve(sentence[index + 1:])
    if valueBody.isError:
        print(valueBody)
        return valueBody
    if "[" in valueName and "]" in valueName:
        length=solve.solve(valueName[valueName.find("[")+1: valueName.find("]")])
        for i in range(int(length.coefArr[0])):
            tempstring=valueName[0:valueName.find("[")]+"["+str(i)+"]"
            #print(tempstring)
            v=Variable(valueBody, tempstring)
            variableArray.append(v)
        return False
    v = Variable(valueBody, valueName)
    variableArray.append(v)
    return False


def showVariable():
    for variable in variableArray:
        print(variable.functionName, end=" : ")
        print(variable.functionBody, end="")
