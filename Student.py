# frontend

import tkinter as tk
import tkinter.messagebox
import backend

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student DBMS")
        self.root.geometry("2350x750+0+0")
        self.root.config(bg="cadet blue")

# ===============================Labels================================

    StdID = tk.StringVar()
    Firstname = tk.StringVar()
    Surname = tk.StringVar()
    DoB = tk.StringVar()
    Age = tk.StringVar()
    Gender = tk.StringVar()
    Address = tk.StringVar()
    Mobile = tk.StringVar()
    
# ===============================Function=============================
    def iExit():
        iExit = tkinter.messagebox.askyesno("Student Database Management System", "R u sure u want to exit?")
        if iExit > 0:
            root.destroy()
            return
        def ClearData():
            self.txtStdID.delete(0, tk.END)
            self.txtfna.delete(0, tk.END)
            self.txtSna.delete(0, tk.END)
            self.txtDoB.delete(0, tk.END)
            self.txtAge.delete(0, tk.END)
            self.txtGender.delete(0, tk.END)
            self.txtAdr.delete(0, tk.END)
            self.txtMob.delete(0, tk.END)

        def addData():
            if (len(StdID.get()) != 0):
                backend.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(),Age.get(),Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0, tk.END)
                studentlist.insert(tk.END,(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(),Mobile.get()))

        def DisplayData():
            studentlist.delete(0, tk.END)
            for row in backend.viewData():
                studentlist.insert(tk.END, row, str(""))

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection(sd[0])
            sd = studentlist.get(searchStd)
            self.txtStdID.delete(0, tk.END)
            self.txtStdID.insert(tk.END, sd[1])
            self.txtfna.delete(0, tk.END)
            self.txtfna.insert(tk.END, sd[2])
            self.txtSna.delete(0, tk.END)
            self.txtSna.insert(tk.END, sd[3])
            self.txtDoB.delete(0, tk.END)
            self.txtDoB.insert(tk.END, sd[4])
            self.txtAge.delete(0, tk.END)
            self.txtAge.insert(tk.END, sd[5])
            self.txtGender.delete(0, tk.END)
            self.txtGender.insert(tk.END, sd[6])
            self.txtAdr.delete(0, tk.END)
            self.txtAdr.insert(tk.END, sd[7])
            self.txtMob.delete(0, tk.END)
            self.txtMob.insert(tk.END, sd[8])

        def DeleteData():
            if (len(StdID.get()) != 0):
                global sd
                backend.DeleteData(sd[0])
                ClearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0, tk.END)
            for row in backend.searchData(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(),Gender.get(), Address.get(),Mobile.get()):
                studentlist.insert(tk.END, row, str(""))

        def update():
            if (len(StdID.get()) != 0):
                backend.deleteRec(sd[0])
            if (len(StdID.get()) != 0):
                backend.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(),Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0, tk.END)
                studentlist.insert(tk.END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(),
                Address.get(),Mobile.get()))

# ==============================Frames==================================

        MainFrame = tk.Frame(self.root, bg="cadet blue")
        MainFrame.grid()
            
        TitFrame = tk.Frame(MainFrame, bd=2, padx=34, pady=8, bg="Ghost White")
        TitFrame.pack(side=tk.TOP)

        self.lblTit = tk.Label(TitFrame, font=('arial', 47, 'bold'), text="Student Database Management System", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = tk.Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White")
        ButtonFrame.pack(side=tk.BOTTOM)

        DataFrame = tk.Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg="Cadet blue")
        DataFrame.pack(side=tk.BOTTOM)

        DataFrameLEFT = tk.LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, bg="Ghost White",font=('arial', 20, 'bold'), text="Student Membership Info\n")
        DataFrameLEFT.pack(side=tk.LEFT)

        DataFrameRIGHT = tk.LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="Ghost White",font=('arial', 20,'bold'), text="Student Details\n")
        DataFrameRIGHT.pack(side=tk.RIGHT)

# =======================Labels and Entry Widget============================

        self.lblStdID = tk.Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Student ID", padx=2, pady=2,bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=tk.W)
        self.txtStdID = tk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)
        
        self.lblfna = tk.Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Firstname", padx=2, pady=2,bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=tk.W)
        self.txtfna = tk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtfna.grid(row=1, column=1)

        self.lblSna = tk.Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Surname", padx=2, pady=2, bg="Ghost White")
        self.lblSna.grid(row=2, column=0, sticky=tk.W)
        self.txtSna = tk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Surname, width=39)
        self.txtSna.grid(row=2, column=1)

        self.lblDoB = tk.Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date of Birth", padx=2, pady=2,bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=tk.W)
        self.txtDoB = tk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = tk.Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age", padx=2, pady=2, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=tk.W)
        self.txtAge = tk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = tk.Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender", padx=2, pady=2,bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=tk.W)
        self.txtGender = tk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)

        self.lblAdr = tk.Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Address", padx=2, pady=2, bg="Ghost White")
        self.lblAdr.grid(row=6, column=0, sticky=tk.W)
        self.txtAdr = tk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width=39)
        self.txtAdr.grid(row=6, column=1)

        self.lblMob = tk.Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mobile", padx=2, pady=2, bg="Ghost White")
        self.lblMob.grid(row=7, column=0, sticky=tk.W)
        self.txtMob = tk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMob.grid(row=7, column=1)

# ====================Listbox and Scroll Widget============================

        scrollbar = tk.Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')
        studentlist = tk.Listbox(DataFrameRIGHT, width=41, height=16, font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist.yview)
        
# ========================Button Widget============================

    self.btnAddData = tk.Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="red", command=addData)
    self.btnAddData.grid(row=0, column=0)
    
    self.btnDisplayData = tk.Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="red", command=DisplayData)
    self.btnDisplayData.grid(row=0, column=1)
    
    self.btnClearData = tk.Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="red", command=ClearData)
    self.btnClearData.grid(row=0, column=2)
    
    self.btnDeleteData = tk.Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="red", command=DeleteData)
    self.btnDeleteData.grid(row=0, column=3)
    
    self.btnSearchData = tk.Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="red", command=searchDatabase)
    self.btnSearchData.grid(row=0, column=4)
    
    self.btnUpdateData = tk.Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="red", command=update)
    self.btnUpdateData.grid(row=0, column=5)

    self.btnExit = tk.Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4, bg="red", command=iExit)
    self.btnExit.grid(row=0, column=6)

if __name__ == '__main__':
    root = tk.Tk()
    application = Student(root)
    root.mainloop()
