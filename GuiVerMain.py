# coding=<utf-8>
#TODO 매개화
from tkinter import *
from tkinter import ttk
import solve
import tkinter.font
import Variable
import clipboard
import polynomial
import ctypes
import time
from datetime import datetime

myappid = "test"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
window=Tk()
window.geometry("400x500+800+100")
window.resizable(False, False)
window.title("Dagulator window")
window.iconbitmap(default="icon2.ico")

strings=[]

recent=polynomial.polynomial()

stack=0
indexofwhile=0
for i in range(36):
    strings.append("")
now = datetime.now()
strings.append("Dagulator 1.0.1"+'  %s-%s-%s %s-%s-%s'%(now.year, now.month, now.day, now.hour, now.minute, now.second))
strings.append("Type --help, --licnese for more information, exit to quit")
def modstr(strings):
    for i in range(0, len(strings)):
        if len(strings[i])>30:
            a=strings[i][0:30]
            b=strings[i][30:]
            strings[i]=a
            strings.insert(i, b)
            #print(strings)

def getuni(strings):
    #modstr(strings)
    ret=""
    m=37
    for i in range(max(0, len(strings)-m),len(strings)):
        ret+=strings[i]+"\n"
    #print(ret)
    return ret
canvas=Canvas(window, width=400, height=500)
canvas.pack()
canvas.create_rectangle(0, 0, 400, 500, fill="white")
help=['-------- program features ---------',
'1. simple calculating',
'This program provides simple calculating including \"+\", \"-\", \"*\"',
', \"/\", \"^\", \"(\", \")\"',
'2. polynomial calculating',
'This program provides polynomial calculating',
'3. functions and constants',
'This program provides sine, cosine, sinh, cosh, exp function,',
'and e, pi',
'4. derivate and integrate',
'You can place \"derivate\" infront of function to derivate',
'\"derivate\"+function+\"at\"+number gives you derivative ',
'coefficient at number',
'you can place \"integrate\" infront of function to integrate',
'\"integrate\"+function+\"from\"+a+\"to\"+b gives you proper integral']

license='''Copyright (C) 2019 YunhoKim, HejunJo. All Rights Reserved.'''
version="1.0.1"
def calc(event):
    #print(strings)
    b=entry.get().strip()
    entry.delete(0, END)
    strings.append(">>> "+b)
    if b=="exit":
        window.destroy()
        exit(0)
    if b=="--memory":
        strings.append(str(len(Variable.variableArray)))
        label.config(text=getuni(strings))
        entry.delete(0, END)
        return
    if b=="--version":
        strings.append(version)
        label.config(text=getuni(strings))
        entry.delete(0, END)
        return
    if b=="--help":
        #print("fsfddsfsfsfsdfsdfsfsfs")
        for i in range(len(help)):
            strings.append(help[i])
        label.config(text=getuni(strings))
        entry.delete(0, END)
        return
    if b=="--license":
        strings.append(license)
        label.config(text=getuni(strings))
        entry.delete(0, END)
        return
    if b=="black theme":
        label.config(text=getuni(strings))
        entry.delete(0, END)
        canvas.create_rectangle(0, 0, 500, 500, fill="black")
        label.config(fg='white', bg='black')
        label2.config(fg='white', bg='black')
        entry.config(fg="white", bg="black", insertbackground="white")
        return
    if b=="white theme":
        label.config(text=getuni(strings))
        entry.delete(0, END)
        canvas.create_rectangle(0, 0, 500, 500, fill="white")
        label.config(fg="black", bg="white")
        label2.config(fg="black", bg="white")
        entry.config(fg="black", bg="white", insertbackground="black")
        return
    if b=="":
        #print(getuni(strings))
        label.config(text=getuni(strings))
        entry.delete(0, END)
        return


    if b=="copy":
        if ">>> "in strings[len(strings)-2]:
            clipboard.copy(strings[len(strings)-2].replace(">>> ", ""))
        else:
            clipboard.copy(strings[len(strings)-2])
        label.config(text=getuni(strings))
        entry.delete(0, END)
        return
    label.config(text=getuni(strings)) #update
    temp=solve.solve(b)

    if type(temp)==type(True):
        print(b)
    else:
        Variable.recent=temp
        a=str(temp).replace("\n", "")
        a.strip()
        strings.append(a)
        print(b, a)
    label.config(text=getuni(strings))
    entry.delete(0, END)
def run(a, ansarea):

    #global ansarea
    commands=a.split("\n")
    ret="\nrun started"
    for command in commands:

        if command=="" or command==" " or command.strip().replace("\n", "")=="":
            continue
        #print("command:" + command + "ans : " + str(solve.solve(command)))
        a=solve.solve(command)
        if type(a)!=type(False):
            if str(a).strip()!="":
                ret+='\n'+str(a)
    #ret+="\nrun ended"
    ansarea.insert(END, ret)

def newwindow():
    nwindow=Toplevel(window)
    nwindow.geometry("400x500")
    #print(nwindow.winfo_width())
    textarea = Text(nwindow, height=nwindow.winfo_reqheight()*2/3, width=nwindow.winfo_reqwidth())
    textarea.place(x=0, y=0)
    ansarea=Text(nwindow, height=nwindow.winfo_reqheight()/3, width=nwindow.winfo_reqwidth())
    ansarea.place(x=0, y=nwindow.winfo_reqheight())
    #ansarea.insert(END, "answer")
    nwindowmenubar=Menu(nwindow)
    nwindowmenu1=Menu(nwindowmenubar, tearoff=0)
    nwindowmenu1.add_command(label="new", command=newwindow)
    nwindowmenubar.add_cascade(label="file", menu=nwindowmenu1)
    scrollbar=Scrollbar(nwindow)
    scrollbar.pack(side="right", fill='y')

    nwindowmenu2=Menu(nwindowmenubar, tearoff=0)
    nwindowmenu2.add_command(label="run", command= lambda: run(textarea.get("1.0", END), ansarea))
    nwindowmenubar.add_cascade(label="run",menu=nwindowmenu2)
    nwindow.config(menu=nwindowmenubar)

    nwindow.mainloop()

label=Label(window, bg="white", justify='left', text=getuni(strings), font=(None, 10))
label.place(x=0, y=0)
label2=Label(window, bg="white", text=">>> ", font=(None, 10))
label2.place(x=0, y=482)
#label3=Label(window, bg="white", text="                       ")
#label3.place(x=30, y=495)
entry=Entry(window, bd=0, width=100, font=(None, 10))
entry.bind("<Return>", calc)
entry.place(x=27, y=484)
#window.lift()
menubar=Menu(window)
menu_1=Menu(menubar, tearoff=0)
menu_1.add_command(label="new", command=newwindow)
menubar.add_cascade(label="file", menu=menu_1)
window.config(menu=menubar)
window.mainloop()
