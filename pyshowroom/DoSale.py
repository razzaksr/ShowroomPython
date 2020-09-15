from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from pymysql import *

class Sale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("New Sale Invoice")
        self.geometry("500x300")
        f = font = ('Times New Roman', 15)
        self.head = Label(self, text="New Sale Bill", font=('Times New Roman', 20))
        self.head.grid(row=0, column=10)
        self.typedate=Label(self,text="Tell us date of the sale")
        self.typedate.grid(row=1,column=8)
        self.date=Entry(self)
        self.date.grid(row=1,column=30)
        self.typemodel=Label(self,text="Choose the model")
        self.typemodel.grid(row=2,column=8)
        self.model=Combobox(self)
        self.model.grid(row=2,column=30)
        self.getp=Button(self,text="Get Price",command=self.getPrice)
        self.getp.grid(row=2,column=40)
        self.price=Entry(self)
        self.price.grid(row=2,column=50)
        try:
            con=connect("localhost","root","","showroom")
            qry="select modelName from vehicle"
            cur=con.cursor()
            cur.execute(qry)
            mods=cur.fetchall()
            tmp=[]
            for h in mods:print(h);tmp.append(h)
            self.model['values']=tmp

        except Exception as e:
            messagebox.showinfo("Error",e)
        self.typename=Label(self,text="Customer Name")
        self.typename.grid(row=3,column=8)
        self.name=Entry(self)
        self.name.grid(row=3,column=30)
        self.typeadd = Label(self, text="Customer Address")
        self.typeadd.grid(row=4, column=8)
        self.add = Entry(self)
        self.add.grid(row=4, column=30)
        self.typemode = Label(self, text="Mode of payment")
        self.typemode.grid(row=5, column=8)
        self.mode = Entry(self)
        self.mode.grid(row=5, column=30)
        self.typemobile = Label(self, text="Customer Mobile Number")
        self.typemobile.grid(row=6, column=8)
        self.mobile = Entry(self)
        self.mobile.grid(row=6, column=30)
        self.typepaid = Label(self, text="Amount paid")
        self.typepaid.grid(row=7, column=8)
        self.paid = Entry(self)
        self.paid.grid(row=7, column=30)
        self.inv=Button(self,text="Sale",command=self.bill)
        self.inv.grid(row=8,column=8)
        self.bk = Button(self, text="Back", command=self.back)
        self.bk.grid(row=8, column=15)

    def bill(self):
        try:
            con=connect("localhost","root","","showroom")
            qry="""insert into sales(date,modelName,onRoadPrice,consumerName,address,paymentMode,mobileNumber,paid) values('%s','%s','%f','%s','%s','%s','%d','%d')"""%(self.date.get(),self.model.get(),float(self.price.get()),self.name.get(),self.add.get(),self.mode.get(),int(self.mobile.get()),int(self.paid.get()))
            cur=con.cursor()
            check=cur.execute(qry)
            if check!=0:messagebox.showinfo("Info","Bill getnerated")
            else:messagebox.showinfo("Error","Bill has not generated")

        except Exception as e:
            messagebox.showinfo("Error",e)

    def back(self):
        self.destroy()
        import pyshowroom.Home as hm
        hm.home().mainloop()

    def getPrice(self):
        try:
            con=connect("localhost","root","","showroom")
            qry="select onRoadPrice from vehicle where modelName='%s'"%(self.model.get())
            cur=con.cursor()
            cur.execute(qry)
            amount=cur.fetchone()
            self.price.insert(0,str(amount[0]))

        except Exception as e:
            messagebox.showinfo("Error",e)

'''s=Sale()
s.mainloop()'''