from tkinter import *

from pymongo import MongoClient
import DBconnect
import InsertClass

class mongoInsert():
    def __init__(self):
        pass

    def createpage(self):
        def quit():
            window.destroy()

        def insert():
            DBconnect.MongoDB().insert(var.get(), command.get())
            top= Toplevel(window)
            top.geometry("500x200")
            top.title("Success")
            Label(top, text= "Record Inserted Successfully").place(x=150,y=80)

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
        welcome = Label(header, text="Mongo Table Inserter", bg='dark gray')
        welcome.config(font=("Courier", 30))
        welcome.pack()
        
        #Option Menu
        table_list = DBconnect.MongoDB().getTables()
        var = StringVar()

        options = OptionMenu(window, var, *table_list)
        options.place(x=50, y=150)
        Label(window, text='Enter values in following order column_name:value seperated by commas: ', bg='black', fg='white').place(x=50, y=175)
        command = Entry(window, width=60)
        command.place(x=50, y=200)
        submit_but = Button(window, text='Submit', command=insert)
        submit_but.place(x=50, y=225)
        back_but = Button(window, text='Back', command=back)
        back_but.place(x=100, y=225)
        
        

        window.mainloop()
