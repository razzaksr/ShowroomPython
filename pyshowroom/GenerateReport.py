from tkinter import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from pymysql import *
class Report(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Sale's Report")
        self.geometry("500x300")
        f = font = ('Times New Roman', 15)
        self.head = Label(self, text="Sales Report", font=('Times New Roman', 20))
        self.head.grid(row=0, column=10)
        self.typefrom=Label(self,text="From Date",font=f)
        self.typefrom.grid(row=1,column=1)
        self.froms=Entry(self)
        self.froms.grid(row=1,column=2)
        self.typeto = Label(self, text="To Date", font=f)
        self.typeto.grid(row=1, column=3)
        self.to = Entry(self)
        self.to.grid(row=1, column=4)
        self.bt=Button(self,text="Generate Report",command=self.generate)
        self.bt.grid(row=1, column=5)
        self.ack=Label(self,text="Here is report which you asked")
        self.ack.grid(row=2,column=1)
        self.typeincome=Label(self,text="Total income")
        self.typeincome.grid(row=2,column=2)
        self.bs = Button(self, text="BAck", command=self.back)
        self.bs.grid(row=3, column=1)

    def back(self):
        self.destroy()
        import pyshowroom.Home as hm
        hm.home().mainloop()
    def generate(self):
        income=[]
        self.f1 = font = ('Times New Roman', 12, 'bold')
        self.f2 = font = ('Times New Roman', 11, 'italic')
        self.h1 = Entry(self, font=self.f1, width=12);
        self.h1.insert(END, "Invoice Number");
        self.h1.grid(row=4, column=0)
        self.h2 = Entry(self, font=self.f1, width=12);
        self.h2.insert(END, "Date");
        self.h2.grid(row=4, column=1)
        self.h3 = Entry(self, font=self.f1, width=12);
        self.h3.insert(END, "Model");
        self.h3.grid(row=4, column=2)
        self.h4 = Entry(self, font=self.f1, width=12);
        self.h4.insert(END, "Cost of the Bike");
        self.h4.grid(row=4, column=3)
        self.h5 = Entry(self, font=self.f1, width=12);
        self.h5.insert(END, "Consumer Name");
        self.h5.grid(row=4, column=4)
        self.h6 = Entry(self, font=self.f1, width=12);
        self.h6.insert(END, "Address");
        self.h6.grid(row=4, column=5)
        self.h7 = Entry(self, font=self.f1, width=12);
        self.h7.insert(END, "Payment Mode");
        self.h7.grid(row=4, column=6)
        self.h8 = Entry(self, font=self.f1, width=12);
        self.h8.insert(END, "Mobile Number");
        self.h8.grid(row=4, column=7)
        self.h9 = Entry(self, font=self.f1, width=12);
        self.h9.insert(END, "Paid amount");
        self.h9.grid(row=4, column=8)
        try:
            con = connect("localhost", "root", "", "showroom")
            cur = con.cursor()
            qry = "select * from sales where date between '%s' and '%s'"%(self.froms.get(),self.to.get())
            cur.execute(qry)
            ware = cur.fetchall()
            lin = 5
            for rows in range(len(ware)):
                for each in range(len(ware[rows])):
                    self.data = Entry(self, font=self.f2,width=12)
                    self.data.insert(END, ware[rows][each])
                    self.data.grid(row=lin, column=each)
                    if each == 8:income.append(ware[rows][each])
                lin += 1
            con.close()
            self.typeincome.configure(text="Total income is: "+str(sum(income)))
        except Exception as e:
            messagebox.showinfo("Error", e)

'''gen=Report()
gen.mainloop()'''