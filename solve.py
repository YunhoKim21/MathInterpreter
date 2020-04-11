import polynomial
import stringfunctions as sf
import Variable
import clipboard
import math
import Canvas

def solve(problem):
    ret = polynomial.polynomial()
    problem = problem.strip()
    if '#' in problem:
        problem=problem[0:problem.find("#")]
    problem=problem.replace(")(", ")*(")
    problem = problem.replace(")x", ")*x")
    problem = problem.replace("x(", "x*(")
    if sf.checkBrackets(problem)==False:
        ret.errorCode=5
        ret.isError=True
        return ret
    while (sf.isThereBrackets(problem)):
        problem = problem[1:len(problem) - 1]
    if problem=="":
        return ret
    if "=" in problem and not ("==" in problem) and not ("!=" in problem):
        return Variable.addValue(problem)
    if problem[0:7]=="Canvas ":
        return Canvas.mkpol(problem)
    if problem[0:5]=="draw ":
        return Canvas.adpol(problem)
    if problem[0:5]=="show ":
        return Canvas.shpol(problem)
    if problem[0:10]=="polarshow ":
        return Canvas.shpolarpol(problem)
    if problem[0:6]=="clear ":
        return Canvas.clearcanvas(problem)
    if problem[0:5]=="plot ":
        if "from" in problem and "to" in problem:
            index1=problem.find("from")
            index2=problem.find("to")
            a=solve(problem[index1+4:index2])
            b=solve(problem[index2+2:])
            if a.coefArr[0]>=b.coefArr[0]:
                ret.isError=True
                ret.errorCode=4
                return ret
            solve(problem[5:index1]).plot(a.coefArr[0], b.coefArr[0])
            return False
        solve(problem[5:]).plot(-5, 5)
        return False
    if problem[0:10]=="polarplot ":

        if "from" in problem and "to" in problem:
            index1=problem.find("from")
            index2=problem.find("to")
            a=solve(problem[index1+4:index2])
            b=solve(problem[index2+2:])
            if a.coefArr[0]>=b.coefArr[0]:
                ret.isError=True
                ret.errorCode=4
                return ret
            solve(problem[10:index1]).polarplot(a.coefArr[0], b.coefArr[0])
            return False
        solve(problem[10:]).polarplot(-5, 5)
        return False
    if problem[0:6]=="solve ":
        function=solve(problem[6:])
        if function.isError:
            return function
        newtonMethodans = function.advancedNewtonMethod()
        if len(newtonMethodans)!=0:
            return str(newtonMethodans)+"\n"
        biSectionans=function.biSection(0, 5)
        if biSectionans:
            return "bisection : "+str(biSectionans)+"\n"
        else:
            return "no roots found\n"
    if problem[0:9]=="derivate ":
        newstr = problem[8:]
        if "at" in newstr:
            index1=newstr.find("at")
            a=solve(newstr[index1+2:])
            f=solve(newstr[0:index1]).derivate().applyPol(a)
            return f
        else:
            return solve(problem[9:]).derivate()
    if problem[0:10]=="integrate ":
        if "from" in problem and "to" in problem:
            index1=problem.find("from")
            index2=problem.find("to")
            a=solve(problem[index1+4:index2])
            b=solve(problem[index2+2:])
            funct=solve(problem[9:index1]).integrate()
            print(funct)
            return funct.applyPol(b)-funct.applyPol(a)

        else:
            return solve(problem[9:]).integrate()
    if sf.doesCharExist(problem, ">"):
        index=sf.whereIsChar(problem, ">")
        if solve(problem[:index]).coefArr[0] > solve(problem[index+1:]).coefArr[0]:
            ret.coefArr[0]=1
            return ret
        return ret
    if sf.doesCharExist(problem, "<"):
        index=sf.whereIsChar(problem, "<")
        if solve(problem[:index]).coefArr[0] < solve(problem[index+1:]).coefArr[0]:
            ret.coefArr[0]=1
            return ret
        return ret
    print(problem)
    if sf.doesStringExist(problem, "=="):
        index=sf.whereIsString(problem, "==")
        if solve(problem[:index])==solve(problem[index+2:]):
            ret.coefArr[0]=1
            return ret
        return ret
    if sf.doesStringExist(problem, "!="):
        index=sf.whereIsString(problem, "!=")
        if solve(problem[:index])!=solve(problem[index+2:]):
            ret.coefArr[0]=1
            return ret
        return ret
    if sf.doesCharExist(problem, '+'):
        index = sf.whereIsChar(problem, '+')
        return solve(problem[:index]) + solve(problem[index + 1:])

    if sf.doesCharExist(problem, '-'):
        index = sf.whereIsChar(problem, '-')
        return solve(problem[:index]) - solve(problem[index + 1:])
    if sf.doesCharExist(problem, 'c'):
        index = sf.whereIsChar(problem, 'c')
        n=solve(problem[:index]).coefArr[0]
        r=solve(problem[index+1:]).coefArr[0]
        if n<r or n<0 or r<0:
            ret.isError=True
            ret.errorCode=13
            return ret
        try:
            res=int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
        except:
            ret.isError=True
            ret.errorCode=13
            return ret
        ret.coefArr[0]=res
        return ret
    if sf.doesCharExist(problem, 'p'):
        index = sf.whereIsChar(problem, 'p')
        n=solve(problem[:index]).coefArr[0]
        r=solve(problem[index+1:]).coefArr[0]
        if n<r or n<0 or r<0:
            ret.isError=True
            ret.errorCode=14
            return ret
        try:
            res=int(math.factorial(n)/(math.factorial(r)))
        except:
            ret.isError=True
            ret.errorCode=14
            return ret
        ret.coefArr[0]=res
        return ret
    if sf.doesCharExist(problem, '*'):
        index = sf.whereIsChar(problem, '*')
        return solve(problem[:index]) * solve(problem[index + 1:])
    if sf.doesCharExist(problem, '/'):
        index = sf.whereIsChar(problem, '/')
        return solve(problem[:index]) / solve(problem[index + 1:])
    if sf.doesCharExist(problem, '^'):
        index = sf.whereIsChar(problem, "^")
        return solve(problem[:index]).power(solve(problem[index + 1:]).coefArr[0])
    if problem[0:4]=="sqrt":
        a=solve(problem[5:-1])
        return a.sqrt()
    if problem[-1]=='!':
        try:
            a = solve(problem[0:-1])
            ret.coefArr[0]=math.factorial(a.coefArr[0])
        except:
            ret.errorCode=12
            ret.isError=True
        return ret
    for variable in Variable.variableArray:
        if problem==variable.functionName:
            return variable.functionBody
    for variable in Variable.variableArray:
        if problem[0:len(variable.functionName)]==variable.functionName:
            if problem[len(variable.functionName)]=="(":
                a=solve(problem[len(variable.functionName)+1:-1])
                return variable.functionBody.applyPol(a)
    if problem == "x":
        ret.coefArr[1] = 1
        return ret
    if problem=="ans":
        return Variable.recent
    try:
        ret.coefArr[0] = float(problem)
    except:
        ret.isError = True
        ret.errorStatement = problem
        ret.errorCode = 1
    return ret