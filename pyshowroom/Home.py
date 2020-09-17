# Home module

from tkinter import *
from tkinter import messagebox

from pyshowroom.DoSale import Sale
from pyshowroom.GenerateReport import Report
from pyshowroom.GetEnquiry import Enquiry
from pyshowroom.StockAdd import NewStock


class home(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Home for Event management")
        self.geometry("500x400")
        self.head = Label(text="Home for Showroom", font=('Monotype Cursiva', 30))
        self.head.pack(expand=True, fill=BOTH)
        self.bar = Menu(self)
        self.menu1 = Menu(self.bar, tearoff=0)
        self.menu2 = Menu(self.bar, tearoff=0)
        self.menu1.add_command(label="Adding Stock", command=self.newone)
        self.menu1.add_command(label="Enquiry", command=self.enquiry)
        self.menu2.add_command(label="Sale", command=self.sale)
        self.menu2.add_command(label="GetReports", command=self.reports)
        self.menu1.add_command(label="Exit", command=self.shut)
        self.bar.add_cascade(label="Stock", menu=self.menu1)
        self.bar.add_cascade(label="Sales Operation", menu=self.menu2)
        self.config(menu=self.bar)

    def shut(self):
        self.destroy()

    def newone(self):
        self.destroy()
        self.new = NewStock()
        self.new.mainloop()

    def enquiry(self):
        self.destroy()
        self.enq = Enquiry()
        self.enq.mainloop()

    def sale(self):
        self.destroy()
        self.s = Sale()
        self.s.mainloop()

    def reports(self):
        self.destroy()
        self.rep = Report()
        self.rep.mainloop()