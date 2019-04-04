from tkinter import *
import re


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    # Create main GUI window
    def create_widgets(self):
        self.labN = Label(self, text="Name", bg="grey", fg="white")
        self.labN.grid(row=0, column=0)

        self.labT = Label(self, text="Telephone", bg="grey", fg="white")
        self.labT.grid(row=1, column=0)

        self.labS = Label(self, text="Search", bg="grey", fg="white")
        self.labS.grid(row=3, column=0)

        self.enN = Entry(self)
        self.enN.grid(row=0, column=1,padx="5",pady="5")

        self.enT = Entry(self)
        self.enT.grid(row=1, column=1,padx="10",pady="10")

        self.entry = Entry(self)
        self.entry.grid(row=3, column=1,padx="40",pady="10")

        self.labE = Label(self, text="Email Address", bg="grey", fg="white")
        self.labE.grid(row=2, column=0)

        self.enE = Entry(self)
        self.enE.grid(row=2, column=1)

        self.addB = Button(self, text="Add Contact", command=self.addF, bg="blue", fg="white")
        self.addB.grid(row=4, column=0)

        self.delB = Button(self, text="Delete Contact", command=self.delF, bg="light green", fg="white")
        self.delB.grid(row=4, column=1)

        self.editB = Button(self, text="Edit Contact", command=self.editF, bg="blue", fg="white")
        self.editB.grid(row=4, column=2)

        self.searchB = Button(self, text="Search", command=self.SearchF, bg="light green", fg="white")
        self.searchB.grid(row=3, column=2)

        self.scroll = Scrollbar(self)
        self.scroll.grid(row=6, column=1, columnspan=10)
        self.lbox = Listbox(self, yscrollcommand=self.scroll.set, width=25, height=10)
        self.scroll.config(command=self.lbox.yview)
        self.lbox.grid(row=6, column=0, padx=5, pady=2)

        self.ERROR = Label(self, text="",font=50, fg="red")
        self.ERROR.grid(row=5, column=1)

        self.display()

    def addF(self):
        self.name = self.enN.get()
        self.tel = self.enT.get()
        self.email = self.enE.get()
        # self.entry.delete(0,END)
        self.enN.delete(0, END)
        self.enT.delete(0, END)
        self.enE.delete(0, END)
        string=self.email
        pat=r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
        if self.name == "" or self.tel == "" or self.email == "":
            self.ERROR.config(text="One of the fields is empty")
        else:
            if re.match(pat,string):

                self.lbox.insert(END, self.name)
                f = open("db.txt", "a+")
                f.write(self.name + "\n")
                f.write(self.tel + "\n")
                f.write(self.email + "\n")
                f.close()
                self.ERROR.config(text="")
                self.display()
            else:
                self.ERROR.config(text="Invalid Email")

    def SearchF(self):
        search_term = self.entry.get()
        if (search_term != ''):
            f = open("db.txt", "r")
            f.seek(0, 0)
            temp = f.read()
            self.lbox.delete(0, END)
            temp1 = temp.split('\n')
            for x in range(len(temp1) - 1):
                if x % 3 == 0:
                    if search_term.lower() in temp1[x].lower():
                        self.lbox.insert(END, temp1[x + 1])
                        self.lbox.insert(END, temp1[x + 2])
        self.entry.delete(0, END)

        if search_term == "" :
            self.ERROR.config(text=" FIELD IS EMPTY!!!! ")

    def display(self):
        self.lbox.delete(0, END)
        with open("db.txt", "r") as f:
            f.seek(0, 0)
            temp = f.read()
            temp1 = temp.split('\n')
            for x in range(len(temp1) - 1):
                if x % 3 == 0:
                    self.lbox.insert(END, temp1[x])

    def delF(self):
        d_name = self.enN.get()
        self.enN.delete(0, END)

        f = open("db.txt", "r")
        f.seek(0, 0)
        temp = f.read()
        f.close()
        f = open("db.txt", "w")
        temp1 = temp.split('\n')
        f.seek(0, 0)
        name_index = temp1.index(d_name)
        tel_index = name_index
        email_index = name_index
        del temp1[name_index]
        del temp1[tel_index]
        del temp1[email_index]
        for newline in temp1:
            if newline == '':
                del temp1[temp1.index('')]

        for name in temp1:
            f.write(name + "\n")
        # f.write("\n")
        f.close()
        self.display()

    def editF(self):
        e_name = self.enN.get()
        e_tel = self.enT.get()
        e_email = self.enE.get()
        self.enN.delete(0, END)
        self.enT.delete(0, END)
        self.enE.delete(0, END)
        string=e_email
        pat=r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
        if re.match(pat,string):

            f = open("db.txt", "r")
            f.seek(0, 0)
            temp = f.read()
            f.close()
            f = open("db.txt", "w")
            temp1 = temp.split('\n')
            f.seek(0, 0)
            for newline in temp1:
                if newline == '':
                    del temp1[temp1.index('')]

            name_index = temp1.index(e_name)
            tel_index = (name_index + 1)
            email_index = (tel_index + 1)
            temp1[name_index] = e_name
            temp1[tel_index] = e_tel
            temp1[email_index] = e_email
            for name in temp1:
                f.write(name + "\n")
            f.close()
            self.display()
        else:
        	self.ERROR.config(text="Enter Valid E-mail Address")



root = Tk()
root.title('Phone Book')
app = Application(master=root)
print('Starting mainloop()')
app.mainloop()