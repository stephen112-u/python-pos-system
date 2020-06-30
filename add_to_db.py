# import all the modules
from tkinter import * 
import sqlite3
import tkinter.messagebox
conn = sqlite3.connect("store.db")
cur = conn.cursor()

class Database:
    def __init__(self, master, *args, **kwarg):
    
        self.master = master
        self.heading = Label(master, text="Add to the database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=400, y=0)

        #labbels and entries for the window
        
        self.name = Label(master, text="Enter Product Name", font=('arial 18 bold'))
        self.name.place(x=0, y=70)

        self.stock = Label(master, text="Enter Product Stock", font=('arial 18 bold'))
        self.stock.place(x=0, y=120)

        self.cp = Label(master, text="Enter Product Cost Price", font=('arial 18 bold'))
        self.cp.place(x=0, y=170)

        self.sp = Label(master, text="Enter Product Selling Price", font=('arial 18 bold'))
        self.sp.place(x=0, y=220)

        self.vender = Label(master, text="Enter Product Vender Name", font=('arial 18 bold'))
        self.vender.place(x=0, y=270)

        self.vender_phoneNo = Label(master, text="Enter Product Vender Phone No.", font=('arial 18 bold'))
        self.vender_phoneNo.place(x=0, y=320)


        #entries for the labels
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=380, y=70)

        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=380, y=120)

        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=380, y=170)

        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=380, y=220)

        self.vender_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vender_e.place(x=380, y=270)

        self.vender_phone_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vender_phone_e.place(x=380, y=320)

        #button to add to the database
        self.btn_add = Button(master, text="Add To Database", width=25, height=2, bg='steelblue', fg='white', command=self.get_items)
        self.btn_add.place(x=520, y=370)

        #text box for the logs
        self.tBox = Text(master, width=60, height=18)
        self.tBox.place(x=750, y=70)
    def get_items(self, *args, **keargs):  
        #get from entries
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vender = self.vender_e.get()
        self.vender_phoneNo = self.vender_phone_e.get()
        
        self.total_cp = float(self.cp) * float(self.stock)
        self.total_sp = float(self.sp) * float(self.stock)
        self.assumed_profit = float(self.total_sp - self.total_cp)

        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
        else:
            sql = "INSERT INTO Inventory (Name, Stock, cp, sp, Vender, Total_cp, Total_sp,Assumed_profit, Vender_phoneNo )VALUES(?,?,?,?,?,?,?,?,?)"
            cur.execute(sql, (self.name, self.stock, self.cp, self.sp, self.vender, self.total_cp, self.total_sp, self.assumed_profit, self.vender_phoneNo))
            conn.commit()
            tkinter.messagebox.showinfo("success", "Successfully add to the database")
    

root = Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Add to the database")
root.mainloop()
