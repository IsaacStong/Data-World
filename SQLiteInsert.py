from tkinter import *

import sqlite3
import DBconnect
import InsertClass

class sqliteInsert():
    def __init__(self):
        pass

    def createpage(self):
        def quit():
            window.destroy()

        def insert():
            try:
                DBconnect.SQLiteDB().insert(var.get(), command.get())
                top= Toplevel(window)
                top.geometry("500x200")
                top.title("Success")
                Label(top, text= "Record Inserted Successfully").place(x=150,y=80)
            except sqlite3.OperationalError:
                top= Toplevel(window)
                top.geometry("500x200")
                top.title("Failed")
                Label(top, text= "Did you input the correct number of values and the right types?").place(x=150,y=80)

        def getColumns():
            col_list = DBconnect.SQLiteDB().getColumns(var.get())
            columns.config(state='normal')
            columns.delete(0, END)
            columns.insert(0, col_list)
            columns.config(state='disable')
            

        def back():
            quit()
            obj = InsertClass.insertClass()
            obj.createpage()


        window = Tk()
        window.geometry("650x350")
        window.title("DATA WORLD")
        window.resizable(0, 0)
        #Page Format
        header = Frame(window, bg='dark gray')
        header.grid(row=0, sticky='news')

        content = Frame(window, bg='black')
        content.grid(row=1, sticky='news')

        footer = Frame(window, bg='dark gray')
        footer.grid(row=2, sticky='news')

        window.columnconfigure(0, weight=5)

        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=8)
        window.rowconfigure(2, weight=1)
        welcome = Label(header, text="SQLite Table Inserter", bg='dark gray')
        welcome.config(font=("Courier", 30))
        welcome.pack()
        
        #Option Menu
        table_list = DBconnect.SQLiteDB().getTables()
        var = StringVar()

        options = OptionMenu(window, var, *table_list)
        options.place(x=50, y=100)
        columns_but = Button(window, text='Get Columns', command=getColumns)
        columns_but.place(x=50, y=150)
        columns = Entry(window, state='disable', width=60)
        columns.place(x=50, y=200)
        Label(window, text='Enter a value for each column above with string values in quotes and values seperated by commas', bg='black', fg='white').place(x=50, y=225)
        command = Entry(window, width=60)
        command.place(x=50, y=250)
        submit_but = Button(window, text='Submit', command=insert)
        submit_but.place(x=50, y=275)
        back_but = Button(window, text='Back', command=back)
        back_but.place(x=100, y=275)
        
        

        window.mainloop()

