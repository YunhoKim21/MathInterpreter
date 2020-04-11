import polynomial
import solve
import matplotlib.pyplot as plt
CanvasArray=[]

class Canvas:
    def __init__(self, name):
        self.polynomials=[]
        self.name=name

    def addPolynomial(self, polynomial):
        self.polynomials.append(polynomial)
    def show(self, a=-5, b=5):
        for polynomial in self.polynomials:
            x = a;
            dx = (b - a) / 100
            xarr = []
            yarr = []
            while x < b + dx:
                xarr.append(x)
                yarr.append(polynomial.applyX(x))
                x = x + dx
            plt.plot(xarr, yarr)
        plt.grid(b=True, which="both", axis="both")
        plt.show()
    def polarshow(self, a=-5, b=5):
        maxy=0
        for polynomial in self.polynomials:
            x = a;
            dx = (b - a) / 100
            xarr = []
            yarr = []
            while x < b + dx:
                xarr.append(x)
                yarr.append(polynomial.applyX(x))
                x = x + dx
            plt.polar(xarr, yarr)
            maxy=max(maxy, max(yarr))
        plt.grid(b=True, which="both", axis="both")
        axis = plt.gca()
        axis.set_ylim([0, maxy])
        plt.show()
def mkpol(problem):
    name=problem[7:]
    if name=="at" or name=="from" or name=="to":
        a=polynomial.polynomial()
        a.errorCode=10
        a.isError=True
        return a
    new=Canvas(name)
    CanvasArray.append(new)
    return False
def adpol(problem):
    index=problem.find("at")
    if index==-1:
        a=polynomial.polynomial()
        a.errorCode=11
        a.isError=True
        return a
    pol=solve.solve(problem[4:index])
    if pol.isError:
        return pol
    target=problem[index+2:].strip()
    for canvas in CanvasArray:
        if canvas.name==target:
            canvas.addPolynomial(pol)
            return False
    ret=polynomial.polynomial()
    ret.isError=True
    ret.errorCode=6
    ret.errorStatement=target
    return ret
def shpol(problem):
    if "from" in problem and "to" in problem:
        indexoffrom=problem.find("from")
        indexofto=problem.find("to")
        polname=problem[5:indexoffrom].strip()
        a=solve.solve(problem[indexoffrom+4:indexofto])
        if a.isError:
            return a
        if not a.isConstant():
            a.isError=True
            a.errorCode=9
            return a
        b=solve.solve(problem[indexofto+2:])
        if b.isError:
            return b
        if not b.isConstant():
            b.isError=True
            b.errorCode=9
            return b
        for canvas in CanvasArray:
            if canvas.name==polname:
                canvas.show(a.coefArr[0], b.coefArr[0])
                return False
        ret=polynomial.polynomial()
        ret.isError=True
        ret.errorCode=6
        ret.errorStatement=polname
        return ret
    polname=problem[5:].strip()
    for canvas in CanvasArray:
        if canvas.name==polname:
            canvas.show()
            return False
    ret = polynomial.polynomial()
    ret.isError = True
    ret.errorCode = 6
    ret.errorStatement = polname
    return ret
def shpolarpol(problem):
    #print("asfssfsdfd")
    if "from" in problem and "to" in problem:
        indexoffrom=problem.find("from")
        indexofto=problem.find("to")
        polname=problem[5:indexoffrom].strip()
        a=solve.solve(problem[indexoffrom+4:indexofto])
        if a.isError:
            return a
        b=solve.solve(problem[indexofto+2:])
        if b.isError:
            return b
        for canvas in CanvasArray:
            if canvas.name==polname:
                canvas.polarshow(a.coefArr[0], b.coefArr[0])
                return False
        ret=polynomial.polynomial()
        ret.isError=True
        ret.errorCode=6
        ret.errorStatement=polname
        return ret
    polname=problem[9:].strip()
    for canvas in CanvasArray:
        if canvas.name==polname:
            canvas.polarshow()
            return False
    ret = polynomial.polynomial()
    ret.isError = True
    ret.errorCode = 6
    ret.errorStatement = polname
    return ret
def clearcanvas(problem):
    canvasname=problem[5:].strip()
    for canvas in CanvasArray:
        if canvas.name==canvasname:
            canvas.polynomials=[]
            return False
    ret=polynomial.polynomial()
    ret.isError=True
    ret.errorCode=6
    ret.errorStatement=canvasname
    return ret
if __name__=="__main__":
    a=Canvas("a")
    p=polynomial.polynomial()
    p.coefArr[0]=100
    p.coefArr[1]=2
    n=polynomial.polynomial()
    n.coefArr[2]=1
    a.addPolynomial(n)
    a.addPolynomial(p)
    a.show()