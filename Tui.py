#TODO
import solve
import sys, os
import time
from datetime import datetime
run=True
now=datetime.now()
# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

print("Dagulator 1.0.1"+'  %s-%s-%s %s-%s-%s'%(now.year, now.month, now.day, now.hour, now.minute, now.second))
print("Type --help, --licnese for more information, exit to quit")
while run:
    enablePrint()
    #print(">>> ", end="")
    a=input(">>> ")
    blockPrint()
    ans=solve.solve(a)
    if a!="":
        enablePrint()
    if type(True)!=type(ans):
        print(ans.__str__().replace("\n", ""))
        #print(">>> ", end="")
    blockPrint()