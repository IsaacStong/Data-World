from tkinter import *

from pymongo import MongoClient
import DBconnect
import CreateClass

class mongoCreate():
    def __init__(self):
        pass

    def createpage(self):
        def quit():
            window.destroy()

        def createTable():
            try:
                obj = DBconnect.MongoDB()
                obj.create(tableName.get())
                top= Toplevel(window)
                top.geometry("500x200")
                top.title("Success")
                Label(top, text= "Table Created Successfully").place(x=150,y=80)
            except cx_Oracle.DatabaseError as e:
                    top= Toplevel(window)
                    top.geometry("500x200")
                    top.title("Failed")
                    Label(top, text= "The table you attempted to create already exists please try another name or use another operation.", font='Arial 8').place(x=0,y=80)
                    print(e)

        def back():
            quit()
            obj = CreateClass.createClass()
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
        welcome = Label(header, text="MongoDB Collection Creator", bg='dark gray')
        welcome.config(font=("Courier", 30))
        welcome.pack()
        
        #Entry boxes
        tableName = Entry(window, width=60)
        tableName.place(x=50, y=125)

        #Labels
        Label(window, text="Collection Name: ", fg='white', bg='black').place(x=50, y=100)

        #Buttons
        submit_but = Button(window, text='Submit', command=createTable, width=15)
        submit_but.place(x=50, y=200)
        back_but = Button(window, text='Back', command=back, width=15)
        back_but.place(x=200, y=200)

        window.mainloop()
