from tkinter import *
import sqlite3

import DBClasses
import CreateClass
import InsertClass
import DeleteClass
import kinter_exporter
import new_excel

class main_project():
    def __init__(self):
        pass

    def mainpage(self):
        def quit():
            window.destroy()

        def create():
            quit()
            obj = CreateClass.createClass()
            obj.createpage()


        def insert():
            quit()
            obj = InsertClass.insertClass()
            obj.createpage()

        def delete():
            quit()
            obj = DeleteClass.deleteClass()
            obj.createpage()


        def export():
            quit()
            obj = kinter_exporter.kinter_exporter()
            obj.for_exporter()


        def createExcel():
            quit()
            obj = new_excel.kinter_excel()
            obj.make_excel()


        window = Tk()
        window.geometry("600x300")
        window.title("DATA WORLD")
        window.resizable(0, 0)
        # header, content, footer
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
        welcome = Label(header, text="Data World", bg='dark gray')
        welcome.config(font=("Courier", 30))
        welcome.pack()
        insert_but = Button(content, text="Insert", command=insert,width=15, height=2)
        insert_but.place(x=150, y=100)
        create_but = Button(content, text="Create", command=create,width=15, height=2)
        create_but.place(x=75, y=40)
        delete_but = Button(content, text="Delete", command=delete,width=15, height=2)
        delete_but.place(x=225, y=40)
        exporter = Button(content, text="Exporter", command=export,width=15, height=2)
        exporter.place(x=375, y=40)
        create_exc = Button(content, text="Create Excel", command=createExcel,width=15, height=2)
        create_exc.place(x=300, y=100)
        
        

        window.mainloop()

obj=main_project()
obj.mainpage()
        
