from tkinter import *

import cx_Oracle
import DBconnect
import DeleteClass

class oracleDelete():
    def __init__(self):
        pass

    def createpage(self):
        def quit():
            window.destroy()

        def deleteTable():
            DBconnect.OracleDB().delete(var.get())
            top= Toplevel(window)
            top.geometry("500x200")
            top.title("Success")
            Label(top, text= "Table Deleted Successfully").place(x=150,y=80)
            

        def back():
            quit()
            obj = DeleteClass.deleteClass()
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
        welcome = Label(header, text="Oracle Table Deleter", bg='dark gray')
        welcome.config(font=("Courier", 30))
        welcome.pack()
        
        #Option Menu
        table_list = DBconnect.OracleDB().getTables()
        var = StringVar()

        options = OptionMenu(window, var, *table_list)
        options.place(x=50, y=100)
        submit_but = Button(window, text='Submit', command=deleteTable)
        submit_but.place(x=50, y=150)
        back_but = Button(window, text='Back', command=back)
        back_but.place(x=100, y=150)
        
        

        window.mainloop()

