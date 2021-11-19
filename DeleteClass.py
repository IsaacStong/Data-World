from tkinter import *

import MainClass
import SQLiteDelete
import OracleDelete
import MongoDelete

class deleteClass():
    def __init__(self):
        pass

    def createpage(self):
        def quit():
            window.destroy()
        
        def oracleDelete():
            quit()
            obj = OracleDelete.oracleDelete()
            obj.createpage()

        def mongoDelete():
            try:
                quit()
                obj = MongoDelete.mongoDelete()
                obj.createpage()
            except TypeError:
                top= Toplevel(window)
                top.geometry("500x200")
                top.title("Failed")
                Label(top, text= "It looks like you have no MongoDB Collections.").place(x=150,y=80)

        def sqliteDelete():
            quit()
            obj = SQLiteDelete.sqliteDelete()
            obj.createpage()
            

        def back():
            quit()
            obj = MainClass.main_project()
            obj.mainpage()

        window = Tk()
        window.geometry("600x300")
        window.title("DATA WORLD")
        window.resizable(0, 0)
        #header, content, footer
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
        welcome = Label(header, text="Table Deleter", bg='dark gray')
        welcome.config(font=("Courier", 30))
        welcome.pack()
        oracle_but = Button(content, text="Oracle", command=oracleDelete,width=15, height=2)
        oracle_but.place(x=75, y=40)
        mongo_but = Button(content, text="MongoDB", command=mongoDelete,width=15, height=2)
        mongo_but.place(x=375, y=40)
        sqlite_but = Button(content, text="SQLite", command=sqliteDelete,width=15, height=2)
        sqlite_but.place(x=225, y=40)
        back_but = Button(content, text='Back', command=back, width=15, height=2)
        back_but.place(x=225, y=100)
        

        #Run Window
        window.mainloop()
