from tkinter import *
from tkinter import messagebox

from pyshowroom.Home import home


class enter(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Login")
        self.geometry("500x400")
        self.head=Label(self,text="Login to Showroom home")
        self.head.pack(side=TOP,padx=10,pady=20)
        self.user=Entry(self)
        self.user.pack(side=TOP,padx=10,pady=40)
        self.pas=Entry(self,show="*")
        self.pas.pack(side=TOP,padx=10,pady=60)
        self.bt=Button(self,text="Login",command=self.log)
        self.bt.pack(side=TOP, padx=10, pady=80)
    def log(self):
        if self.user.get()=='annamalai' and self.pas.get()=='salem':
            self.destroy()
            hm=home()
            hm.mainloop()
        else:messagebox.showinfo("error","Invalid login")

log=enter()
log.mainloop()