# Adding new event

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from pymysql import *

class NewStock(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Adding New Stock")
        self.geometry("500x300")
        f = font = ('Times New Roman', 15)
        self.head = Label(self, text="Adding New Stock", font=('Times New Roman', 20))
        self.head.grid(row=0, column=10)
        self.typemodel = Label(self, text="Enter Model of the bike", font=f)
        self.typemodel.grid(row=1, column=8)
        self.model = Entry(self)
        self.model.grid(row=1, column=30)
        self.typemodtype = Label(self, text="Tell us model type", font=f)
        self.typemodtype.grid(row=2, column=8)
        self.radiovar = StringVar();self.radiovar.set("")
        self.radio1 = Radiobutton(self, var=self.radiovar, value="Gear", text="Gear Type")
        self.radio1.grid(row=2, column=30)
        self.radio2 = Radiobutton(self, var=self.radiovar, value="Gear less", text="Gear Less Type")
        self.radio2.grid(row=2, column=40)
        self.typeyear = Label(self, text="Enter the model year", font=f)
        self.typeyear.grid(row=3, column=8)
        self.year = Entry(self)
        self.year.grid(row=3, column=30)
        self.typecc = Label(self, text="Enter the Capacity of engine", font=f)
        self.typecc.grid(row=4, column=8)
        self.cc = Entry(self)
        self.cc.grid(row=4, column=30)
        self.typemilage = Label(self, text="Enter the Average milage", font=f)
        self.typemilage.grid(row=5, column=8)
        self.milage = Entry(self)
        self.milage.grid(row=5, column=30)
        self.typequan = Label(self, text="Enter the Quantity", font=f)
        self.typequan.grid(row=6, column=8)
        self.quan = Entry(self)
        self.quan.grid(row=6, column=30)
        self.typewaren = Label(self, text="Choose Warranty", font=f)
        self.typewaren.grid(row=7, column=8)
        self.waran = Combobox(self)
        self.waran['values'] = ('Select Warranty year', '1', '2', '3', '4', '5')
        self.waran.grid(row=7, column=30)
        self.typeprice = Label(self, text="Enter the Price", font=f)
        self.typeprice.grid(row=8, column=8)
        self.price = Entry(self)
        self.price.grid(row=8, column=30)
        self.bt = Button(self, text="Add to Stock", command=self.enroll)
        self.bt.grid(row=9, column=30)
        self.bs = Button(self, text="BAck", command=self.back)
        self.bs.grid(row=10, column=30)

    def back(self):
        self.destroy()
        '''from eventmanage.eventsHome import home
        #Toplevel(home).mainloop()
        #home().mainloop()'''
        #import eventmanage.eventsHome as hm
        import pyshowroom.Home as hm
        hm.home().mainloop()

    def enroll(self):
        try:
            con = connect('localhost', 'root', '', 'showroom')
            qry = """insert into vehicle(modelName,type,modelYear,engineCapacity,averageMilage,quantity,warrenty,onRoadPrice) values('%s','%s',%d,%d,%d,%d,%d,%f)""" % (self.model.get(),str(self.radiovar.get()),int(self.year.get()),int(self.cc.get()),int(self.milage.get()),int(self.quan.get()),int(self.waran.get()),float(self.price.get()))
            cur = con.cursor()
            out = cur.execute(qry)
            if out != 0:
                messagebox.showinfo("Status", "Stock added")
            else:
                messagebox.showinfo("Status", "Stock Not addded")
        except Exception as e:
            con.rollback();print(e)
        finally:
            con.close()


'''n = NewStock()
n.mainloop()'''
