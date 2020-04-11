import matplotlib.pyplot as plt
import math
class polynomial:
    numOfCoefs = 50
    solveError=0.000000000000001

    def __init__(self):
        self.coefArr = [0] * self.numOfCoefs
        self.isNone=False
        self.isError=False
        self.errorCode=0
    def __eq__(self, other):
        for i in range(0, self.numOfCoefs):
            if self.coefArr[i]!=other.coefArr[i]:
                return False
        return True
    def __ne__(self, other):
        if self==other:
            return False
        return True
    def sqrt(self):
        ret=polynomial()
        ret.coefArr[0]=math.sqrt(self.coefArr[0])
        return ret
    def getDegree(self):
        ret=0
        for i in range(0, self.numOfCoefs):
            if self.coefArr[i]!=0:
                ret=i
        return ret
    def __truediv__(self, other):
        if self.isError:
            return self
        if other.isError:
            return other
        ret = polynomial()
        if other.coefArr[0]==0:
            ret.isError=True
            ret.errorCode=2
            return ret
        for i in range(0, self.numOfCoefs):
            ret.coefArr[i]=float(self.coefArr[i])/float(other.coefArr[0])
        return ret
    def biSection(self, a, b):
        fa=self.applyX(a)
        fb=self.applyX(b)
        fc=self.applyX((a+b)/2)
        if fa*fb>0:
            return False
        if fc==0:
            return (a+b)/2
        if b-a<self.solveError:
            return (b+a)/2
        if fc*fa>0:
            return self.biSection((a+b)/2, b)
        else:
            return self.biSection(a,(a+b)/2)
    def advancedNewtonMethod(self):
        ansarr=[]
        f0=self.newtonMethod(0)
        if f0:
            ansarr.append(f0)
        plus=1
        minus=-1
        while len(ansarr)<5 and plus<10:
            plusans=self.newtonMethod(plus)
            minusans=self.newtonMethod(minus)
            addplus=True
            for pans in ansarr:
                if abs(pans-plusans)<0.0001:
                    addplus=False
            if addplus and plusans:
                ansarr.append(plusans)
            addminus=True
            for pans in ansarr:
                if abs(pans-minusans)<0.0001:
                    addminus=False
            if addminus and minusans:
                ansarr.append(minusans)
            plus+=1
            minus-=1
        return ansarr
    def newtonMethod(self, xt):
        if self.applyX(xt)==0:
            return xt
        derivative=self.derivate()
        try:
            xtp=xt-self.applyX(xt)/derivative.applyX(xt)
        except:
            return False
        if abs(xt-xtp)<self.solveError:
            return xtp
        try:
            return self.newtonMethod(xtp)
        except:
            return False
    def __add__(self, other):
        if self.isError:
            return self
        if other.isError:
            return other
        ret = polynomial()
        for i in range(0, self.numOfCoefs):
            ret.coefArr[i] = self.coefArr[i] + other.coefArr[i]
        return ret

    def __sub__(self, other):
        if self.isError:
            return self
        if other.isError:
            return other
        ret = polynomial()
        for i in range(0, self.numOfCoefs):
            ret.coefArr[i] = self.coefArr[i] - other.coefArr[i]
        return ret

    def __mul__(self, other):
        if self.isError:
            return self
        if other.isError:
            return other
        ret = polynomial()
        for i in range(0, self.numOfCoefs):
            for j in range(0, self.numOfCoefs - i):
                if self.coefArr[i] != 0 and other.coefArr[j] != 0:
                    ret.coefArr[i + j] += self.coefArr[i] * other.coefArr[j]
        return ret

    def applyX(self, x):
        ret = 0
        for i in range(0, self.numOfCoefs):
            ret += self.coefArr[i] * pow(x, i)
        return ret
    
    def power(self, n):
        ret=polynomial()
        ret.coefArr[0]=1
        for i in range(0, int(n)):
            ret=ret*self
        return ret
    
    def integrate(self):
        ret = polynomial()
        for i in range(0, self.numOfCoefs - 1):
            ret.coefArr[i + 1] = self.coefArr[i] / (i + 1)
        return ret

    def derivate(self):
        ret = polynomial()
        for i in range(1, self.numOfCoefs):
            ret.coefArr[i - 1] = self.coefArr[i] * i
        return ret

    def applyPol(self, other):
        if self.isError:
            return self
        if other.isError:
            return other
        ret = polynomial()
        for i in range(0, self.numOfCoefs):
            temp = polynomial()
            temp.coefArr[0] = self.coefArr[i]
            for j in range(0, i):
                temp = temp*other
            ret = ret+temp
        return ret
    
    def __str__(self):
        ret = ""
        if self.isError:
            if self.errorCode==1:
                return "Error : word \""+self.errorStatement+"\" not defined\n"
            if self.errorCode==2:
                return "Error : cannot divide to 0\n"
            if self.errorCode==3:
                return "Error : \"to\" not found"
            if self.errorCode==4:
                return "Error : invalid range"
            if self.errorCode==5:
                return "Error : invalid brackets"
            if self.errorCode==6:
                return "Error : cannot find Canvas \""+self.errorStatement+"\""
            if self.errorCode==7:
                return "Error : invalid variable name"
            if self.errorCode==8:
                return "Error : cannot assign to literal"
            if self.errorCode==9:
                return "Error : only constant numbers can be in range"
            if self.errorCode==10:
                return "Error : invalid canvas name"
            if self.errorCode==11:
                return "Error : \"at\" missing"
            if self.errorCode==12:
                return "Error : unappropriate number for function factorial"
            if self.errorCode==13:
                return "Error : invalid numbers for function combination"
            if self.errorCode==14:
                return "Error : invalid numbers for function permutation"
            else:
                return "Error : undefined error"
        if self:
            return "0"
        for i in range(0, self.numOfCoefs):
            if self.coefArr[i] != 0:
                if i == 0:
                    ret += str(self.coefArr[0])
                elif i == 1:
                    if self.coefArr[1]==1.0:
                        ret+="+x"
                    else:
                        if self.coefArr[1]>0:
                            ret+="+"
                        if self.coefArr[1]!=1 and self.coefArr[i]!=-1:
                            ret += str(self.coefArr[1])
                        if self.coefArr[i]==-1:
                            ret+='-'
                        ret += "*x"
                else:
                    if self.coefArr[i]>0:
                        ret+="+"
                    if self.coefArr[i]!=1 and self.coefArr[i]!=-1:
                        ret +=str(self.coefArr[i])
                        ret += "*"
                    if self.coefArr[i]==-1:
                        ret+='-'
                    ret +="x^"
                    ret += str(i)
        global recent
        recent=ret
        ret+='\n'
        return ret

    def __bool__(self):
        for i in range(self.numOfCoefs):
            if self.coefArr[i]!=0:
                return False
        return True
    def plot(self, a, b):
        x=a; dx=(b-a)/1000
        xarr=[]
        yarr=[]
        while x<b+dx:
            xarr.append(x)
            yarr.append(self.applyX(x))
            x=x+dx
        plt.plot(xarr, yarr)
        plt.grid(b=True, which="both", axis="both")
        plt.show()
    def polarplot(self, a , b):
        #print("polar")
        x = a
        dx = (b - a) / 1000
        xarr = []
        yarr = []
        while x < b + dx:
            xarr.append(x)
            yarr.append(self.applyX(x))
            x = x + dx
        plt.polar(xarr, yarr)
        axis = plt.gca()
        axis.set_ylim([0, max(yarr)])
        plt.grid(b=True, which="both", axis="both")
        plt.show()

    def isConstant(self):
        for i in range(1, self.numOfCoefs):
            if self.coefArr[i]!=0:
                return False
        return True