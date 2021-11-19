from tkinter import *

import MainClass
import SQLiteInsert
import OracleInsert
import MongoInsert


class insertClass():
    def __init__(self):
        pass

    def createpage(self):
        def quit():
            window.destroy()
        
        def oracleInsert():
            quit()
            obj = OracleInsert.oracleInsert()
            obj.createpage()

        def mongoInsert():
            quit()
            obj = MongoInsert.mongoInsert()
            obj.createpage()

        def sqliteInsert():
            quit()
            obj = SQLiteInsert.sqliteInsert()
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
        welcome = Label(header, text="Table Insertor", bg='dark gray')
        welcome.config(font=("Courier", 30))
        welcome.pack()
        oracle_but = Button(content, text="Oracle", command=oracleInsert,width=15, height=2)
        oracle_but.place(x=75, y=40)
        mongo_but = Button(content, text="MongoDB", command=mongoInsert,width=15, height=2)
        mongo_but.place(x=375, y=40)
        sqlite_but = Button(content, text="SQLite", command=sqliteInsert,width=15, height=2)
        sqlite_but.place(x=225, y=40)
        back_but = Button(content, text='Back', command=back, width=15, height=2)
        back_but.place(x=225, y=100)
        

        #Run Window
        window.mainloop()
