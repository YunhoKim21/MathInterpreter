import tkinter as tk
import solve
class editwindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.Strings=[]
        for i in range(100):
            self.Strings.append("\n")
        self.parent=parent

        self.mainTextArea=tk.Text(self, height=10, width=parent.winfo_width())
        self.mainTextArea.pack()

        self.smallLabel=tk.Label(self, bg="white", text='>>> ', font=('Consolas', 10))
        self.smallLabel.place(x=0, y=parent.winfo_height()-20)

        self.inputentry=tk.Entry(self, width=str(parent.winfo_width()), bg='white', font=('Consolas', 10), bd=0)
        self.inputentry.bind("<Return>", self.calculate)
        self.inputentry.place(x=27, y=parent.winfo_height()-20)

        #self.scrollbar=tk.Scrollbar(parent, command=self.mainTextArea.yview)
        #self.mainTextArea.config(yscrollcommand=self.scrollbar.set)
        #self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.pack()
    def unify(self):
        ret=''
        for string in self.Strings:
            ret+='\n'+string
        return ret
    def calculate(self, *args):
        command=self.inputentry.get()
        if command=='':
            return
        self.Strings.append('>>> '+command)
        answer=solve.solve(command)
        if type(answer)!=type(True):
            self.Strings.append(str(solve.solve(command)).replace('\n', ''))
        self.mainTextArea.delete(1.0, tk.END)
        self.mainTextArea.insert(tk.END, self.unify())
        self.inputentry.delete(0, tk.END)
        self.mainTextArea.see(tk.END)
if __name__=="__main__":
    root=tk.Tk()
    root.geometry('400x600')
    root.update()
    editwindow(root).pack()
    root.mainloop()