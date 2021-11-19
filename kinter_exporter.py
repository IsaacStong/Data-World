from cx_Oracle import DatabaseError
from data_exporter1 import DATA_EXPOTER
from ploader_class import pyloader
from tkinter import *
from tkinter.messagebox import showinfo
class kinter_exporter():

    def __init__(self):
        pass
    def for_exporter(self):
        def clear():
            pass



        def submit_to_sqlite(db_name, table_name, fields, data):
            if db_name=="":
                showinfo(title="Error",message="enter database name")

            elif table_name=="":
                showinfo(title="Error",message="enter table name")
            elif fields=="":
                showinfo(title="Error",message="enter fields name")
            else:
                obj = pyloader()
                message1 = obj.loadToSqlite(db_name, table_name, fields, data)
                if message1 == "done":
                    showinfo("DONE", "data is export to SQLITE")
                    quit()
                    obj = kinter_exporter()
                    obj.for_exporter()
                else:
                    showinfo(title="Error", message=message1)




        def submit_to_oracle(user_name, password, table_name, data, fields):
            if user_name=="":
                showinfo(title="Error",message="Enter user name")
            elif password=="":
                showinfo(title="Error",message="Enter password ")
            elif table_name=="":
                showinfo(title="Error",message="Enter table name")
            elif fields=="":
                showinfo(title="Error",message="Enter fields name")
            else:
                user_id = user_name + "/" + password
                obj = pyloader()
                message1 = obj.loadToOracle(user_id, table_name, fields, data)
                if message1 == "done":
                    showinfo("DONE", "data is export to Oracle")
                    quit()
                    obj = kinter_exporter()
                    obj.for_exporter()
                else:
                    showinfo(title="Error", message=message1)



        def submit_to_mongodb(hostname, address, db_name, table_name, data, fields):
            if db_name == "":
                showinfo(title="Error", message="enter database name")

            elif table_name == "":
                showinfo(title="Error", message="enter table name")
            elif fields == "":
                showinfo(title="Error", message="enter fields name")
            else:
                obj = pyloader()
                message1 = obj.loadToMongodb(hostname, address, db_name, table_name, fields, data)
                if message1 == "done":
                    showinfo("DONE", "data is export to Mongodb")
                    quit()
                    obj = kinter_exporter()
                    obj.for_exporter()
                else:
                    showinfo(title="Error", message=message1)




        def select_destination(data,table_name,fields):
            if destination.get()== 2:
                d_info = Label(content, text="Enter destination information", bg='black', fg='white')
                d_info.grid(row=5, column=4)
                db_labelSQLITE = Label(content, text="Enter data base name\n(like 'firstdb.db')", bg='black', fg='white')
                db_labelSQLITE.grid(row=6, column=3)
                db_nameSQLITE = Entry(content)
                db_nameSQLITE.grid(row=6, column=4)
                table_labelSQLITE = Label(content, text="Table name", bg='black', fg='white')
                table_labelSQLITE.grid(row=7, column=3)
                table_nameSQLITE = Entry(content)
                table_nameSQLITE.insert("end",table_name)
                table_nameSQLITE.configure(state=DISABLED)
                table_nameSQLITE.grid(row=7, column=4)
                fields_labelSQLITE = Label(content, text='Fields name you will have', bg='black', fg='white')
                fields_labelSQLITE.grid(row=8, column=3)
                fieldsSQLITE = Entry(content)
                fieldsSQLITE.insert("end",fields)
                fieldsSQLITE.configure(state=DISABLED)
                fieldsSQLITE.grid(row=8, column=4)
                submit_sqlite = Button(content, text="SUBMIT", command= lambda: submit_to_sqlite(db_nameSQLITE.get(),table_nameSQLITE.get(), fieldsSQLITE.get(),data))
                submit_sqlite.grid(row=12,column=4)

            elif destination.get()==1:
                d_info = Label(content, text="Enter destination information", bg='black', fg='white')
                d_info.grid(row=5, column=4)
                user_name_lableORACLE = Label(content, text="Enter username", bg='black', fg='white')
                user_name_lableORACLE.grid(row=6, column=3)
                user_nameORACLE = Entry(content)
                user_nameORACLE.grid(row=6, column=4)
                pass_labelORACLE = Label(content, text="Enter password", bg='black', fg='white')
                pass_labelORACLE.grid(row=7, column=3)
                passwordORACLE = Entry(content,show="*")
                passwordORACLE.grid(row=7, column=4)
                table_labelORACLE = Label(content, text="Table name", bg='black', fg='white')
                table_labelORACLE.grid(row=8, column=3)
                table_nameORACLE = Entry(content)
                table_nameORACLE.insert("end",table_name)
                table_nameORACLE.configure(state=DISABLED)
                table_nameORACLE.grid(row=8, column=4)
                fields_labelORACLE = Label(content, text='Fields name you will have ', bg='black', fg='white')
                fields_labelORACLE.grid(row=9, column=3)
                fieldsORACLE = Entry(content)
                fieldsORACLE.insert("end",fields)
                fieldsORACLE.configure(state=DISABLED)
                fieldsORACLE.grid(row=9, column=4)
                submit_oracle= Button(content, text="SUBMIT", command= lambda: submit_to_oracle(user_nameORACLE.get(), passwordORACLE.get(), table_nameORACLE.get(), data, fieldsORACLE.get()))
                submit_oracle.grid(row=12, column=4)

            elif destination.get()==3:
                d_info = Label(content, text="Enter destination information", bg='black', fg='white')
                d_info.grid(row=5, column=4)
                hostname = "localhost"
                address = 27017
                db_labelMONGODB = Label(content, text="Enter data base name\n(like 'firstdb')", bg='black', fg='white')
                db_labelMONGODB.grid(row=6, column=3)
                db_nameMONGODB = Entry(content)
                db_nameMONGODB.grid(row=6, column=4)
                table_labelMONGODB = Label(content, text="Table name", bg='black', fg='white')
                table_labelMONGODB.grid(row=7, column=3)
                table_nameMONGODB = Entry(content)
                table_nameMONGODB.insert("end",table_name)
                table_nameMONGODB.configure(state=DISABLED)
                table_nameMONGODB.grid(row=7, column=4)
                fields_labelMONGODB = Label(content, text='Fields name you will have', bg='black', fg='white')
                fields_labelMONGODB.grid(row=8, column=3)
                fieldsMONGODB = Entry(content)
                fieldsMONGODB.insert("end",fields)
                fieldsMONGODB.configure(state=DISABLED)
                fieldsMONGODB.grid(row=8, column=4)
                submit_mongodb = Button(content, text="SUBMIT",command= lambda: submit_to_mongodb(hostname,address,db_nameMONGODB.get(),table_nameMONGODB.get(), data, fieldsMONGODB.get()))
                submit_mongodb.grid(row=10, column=4)



        def get_from_s(db_name, table_name, fields):
            print(db_name, table_name, fields)
            obj_source = DATA_EXPOTER()
            data = obj_source.get_from_sqlite(db_name, table_name, fields)
            if isinstance(data,str):
                showinfo(title="Error",message=data)
            else:
                print(data)
                select_destination(data,table_name,fields)
        def get_from_o(user_name, password, table_name, fields):
            print( table_name, fields)
            obj_source = DATA_EXPOTER()
            data = obj_source.get_from_oracle(user_name, password, table_name, fields)
            if isinstance(data,str):
                showinfo(title="Error",message=data)
            else:
                print(data)
                select_destination(data,table_name,fields)
        def get_from_m(db_name,table_name,fields):
            print(db_name, table_name, fields)
            hostname = "localhost"
            address = 27017
            obj_source = DATA_EXPOTER()
            #data=obj_source.get_from_mongodb(hostname1,address1,db_name,table_name,fields)
            data = obj_source.get_from_mongodb(hostname,address, db_name,table_name, fields)
            if isinstance(data,str):
                showinfo(title="Error",message=data)
            else:
                print(data)
                select_destination(data,table_name,fields)











        def next_sep():


            if source.get() ==0:
                showinfo(title="Error",message='Select a source' )
            elif destination.get() ==0:
                showinfo(title="Error",message='Select a destination' )




            elif source.get() == destination.get():
                showinfo(title="Error",message='source and Destination can\'t be same')
                #-----------------------------------------------------------------------------------------------------------------------
            elif source.get() == 2 :  # if source is sqlite


                def get_tablesS(db_nameSQLITE):
                    def get_fields(table_nameSQLITE):
                        if table_nameSQLITE=="-Select-":
                            showinfo(message='Select table name')
                        else:
                            n_b1.grid_forget()
                            obj = DATA_EXPOTER()
                            fields_labelSQLITE = Label(content, text='Fields coming from table',
                                                       bg='black', fg='white')
                            fields_labelSQLITE.grid(row=8, column=1)
                            fields_name = obj.get_fields_from_sqlite(db_nameSQLITE, table_nameSQLITE)
                            if isinstance(fields_name,DatabaseError):
                                showinfo(title="Error",message=fields_name)
                            else:
                                n_b1.grid_forget()
                                fields_name = ",".join(fields_name)

                                fieldsSQLITE = Entry(content)
                                fieldsSQLITE.insert(END, fields_name)
                                fieldsSQLITE.configure(state=DISABLED)
                                fieldsSQLITE.grid(row=8, column=2)
                                get_data = Button(content, text="Get Data",
                                                  command=lambda: get_from_s(db_nameSQLITE, table_nameSQLITE,
                                                                             fields_name))
                                get_data.grid(row=9, column=2)


                    if db_nameSQLITE == "":
                        showinfo(message='Enter database name')
                        db_nameSQLITE.focus()
                    else:
                        obj = DATA_EXPOTER()
                        t_names = obj.get_tables_from_sqlite(db_nameSQLITE)
                        if isinstance(t_names,DatabaseError)or isinstance(t_names,list)==False:
                            showinfo(title="Error",message=t_names)
                        else:
                            table_labelSQLITE = Label(content, text="Select table name", bg='black', fg='white')
                            table_labelSQLITE.grid(row=7, column=1)
                            table_nameSQLITE = StringVar(content)
                            table_nameSQLITE.set("-Select-")
                            popupMenu = OptionMenu(content, table_nameSQLITE, *t_names)
                            popupMenu.grid(row=7, column=2)
                            n_b.grid_forget()
                            n_b1 = Button(content, text="NEXT", command=lambda: get_fields(table_nameSQLITE.get()))
                            n_b1.grid(row=7, column=3)




                    #-------------------------------------------------------------------------
                s_info=Label(content,text="Enter source information", bg='lemon chiffon')
                s_info.grid(row=5,column=2)
                db_labelSQLITE=Label(content,text="Enter data base name\n(like 'firstdb.db')", bg='black', fg='white')
                db_labelSQLITE.grid(row=6,column=1)
                db_nameSQLITE = Entry(content)
                db_nameSQLITE.grid(row=6, column=2)
                n_b=Button(content,text="NEXT",command=lambda:get_tablesS(db_nameSQLITE.get()))
                n_b.grid(row=6,column=3)





#--------------------------------------------------------------------------------------------------------------------------------------------

            elif source.get() == 1:  # if source is oracle
                def get_tablesO():
                    def get_fieldsO():
                        if table_nameORACLE.get()=="-Select-":
                            showinfo(title="Error", message="Select a table")
                        else:
                            fields_labelORACLE = Label(content, text='Fields coming from table ',
                                                       bg='lemon chiffon')
                            fields_labelORACLE.grid(row=9, column=1)
                            obj = DATA_EXPOTER()
                            fields_name = obj.get_fields_from_oracle(user_nameORACLE.get(), passwordORACLE.get(),
                                                                     table_nameORACLE.get())
                            if isinstance(fields_name,DatabaseError):
                                showinfo(title="Error",message=t_names)
                            else:
                                n_b1.grid_forget()
                                fields_name = ",".join(fields_name)
                                fieldsORACLE = Entry(content)
                                fieldsORACLE.insert("end", fields_name)
                                fieldsORACLE.configure(state=DISABLED)
                                fieldsORACLE.grid(row=9, column=2)
                                get_data = Button(content, text="Get Data",
                                                  command=lambda: get_from_o(user_nameORACLE.get(),
                                                                             passwordORACLE.get(),
                                                                             table_nameORACLE.get(),
                                                                             fieldsORACLE.get()))
                                get_data.grid(row=10, column=2)









                    if user_nameORACLE.get()=="":
                        showinfo(title="Error",message="User name can't be empty")
                        user_nameORACLE.focus()
                    elif passwordORACLE.get()=="":
                        showinfo(title="Error", message=" Password can't be empty")
                        passwordORACLE.focus()
                    else:
                        obj = DATA_EXPOTER()
                        t_names = obj.get_tables_from_oracle(user_nameORACLE.get(), passwordORACLE.get())
                        if isinstance(t_names,DatabaseError):
                            showinfo(title="Error",message=t_names)
                            user_nameORACLE.delete(0,"end")
                            passwordORACLE.delete(0, "end")
                            user_nameORACLE.focus()
                        else:
                            table_labelORACLE = Label(content, text="Select table name", bg='black', fg='white')
                            table_labelORACLE.grid(row=8, column=1)
                            table_nameORACLE = StringVar(content)
                            table_nameORACLE.set("-Select-")
                            popupMenu = OptionMenu(content, table_nameORACLE, *t_names)
                            popupMenu.grid(row=8, column=2)

                            n_b.grid_forget()
                            n_b1 = Button(content, text="NEXT", command=lambda: get_fieldsO())
                            n_b1.grid(row=8, column=3)







                s_info = Label(content, text="Enter source information", bg='black', fg='white')
                s_info.grid(row=5, column=1)
                user_name_lableORACLE=Label(content,text="Enter username", bg='black', fg='white')
                user_name_lableORACLE.grid(row=6,column=1)
                user_nameORACLE = Entry(content)
                user_nameORACLE.grid(row=6, column=2)
                pass_labelORACLE=Label(content,text="Enter password", bg='black', fg='white')
                pass_labelORACLE.grid(row=7, column=1)
                passwordORACLE=Entry(content,show="*")
                passwordORACLE.grid(row=7, column=2)
                n_b = Button(content, text="NEXT", command=lambda:  get_tablesO())
                n_b.grid(row=7, column=3)
                #----------------------------------------------------------------------------------------------------------

            elif source.get() == 3:  # if source is mongodb
                def get_tablesM():

                    def get_fieldsM():
                        if table_nameMONGODB.get()=="-Select-":
                            showinfo(title="Error",message="Select table name")
                        else:
                            n_b1.grid_forget()
                            obj = DATA_EXPOTER()
                            fields_labelMONGODB = Label(content, text='Fields coming from table',
                                                        bg='black', fg='white')
                            fields_labelMONGODB.grid(row=8, column=1)
                            fields_name = obj.get_fields_from_mongodb("localhost", 27017, db_nameMONGODB.get(),
                                                                      table_nameMONGODB.get())
                            if isinstance(fields_name,DatabaseError):
                                showinfo(title="Error",message=fields_name)
                            else:
                                n_b1.grid_forget()
                                fields_name = ",".join(fields_name)

                                fieldsMONGODB = Entry(content)
                                fieldsMONGODB.insert(END, fields_name)
                                fieldsMONGODB.configure(state=DISABLED)
                                fieldsMONGODB.grid(row=8, column=2)
                                get_data = Button(content, text="Get Data",
                                                  command=lambda: get_from_m(db_nameMONGODB.get(),
                                                                             table_nameMONGODB.get(),
                                                                             fields_name))
                                get_data.grid(row=9, column=2)





                    if db_nameMONGODB.get()=="":
                        showinfo(title="Eroor",message="Enter database name")
                        db_nameMONGODB.focus()
                    else:
                        obj = DATA_EXPOTER()
                        t_names = obj.get_tables_from_mongodb("localhost", 27017, db_nameMONGODB.get())
                        if isinstance(t_names,DatabaseError) or isinstance(t_names,list)==False:
                            showinfo(title="Error",message=t_names)
                        else:
                            table_labelMONGODB = Label(content, text="Select table name", bg='black', fg='white')
                            table_labelMONGODB.grid(row=7, column=1)
                            table_nameMONGODB = StringVar(content)
                            table_nameMONGODB.set("-Select-")
                            popupMenu = OptionMenu(content, table_nameMONGODB, *t_names)
                            popupMenu.grid(row=7, column=2)
                            n_b.grid_forget()
                            n_b1 = Button(content, text="NEXT", command=lambda: get_fieldsM())
                            n_b1.grid(row=7, column=3)






                s_info = Label(content, text="Enter source information", bg='black', fg='white')
                s_info.grid(row=5, column=1)


                db_labelMONGODB = Label(content, text="Enter data base name\n(like 'firstdb')",bg='black', fg='white')
                db_labelMONGODB.grid(row=6, column=1)
                db_nameMONGODB = Entry(content)
                db_nameMONGODB.grid(row=6, column=2)
                n_b = Button(content, text="NEXT", command=lambda: get_tablesM())
                n_b.grid(row=6, column=3)

        def quit():
            window.destroy()


        def cancel():
            quit()
            import MainClass


            obj = MainClass.main_project()
            obj.mainpage()







        window = Tk()

        window.geometry("800x500")
        window.title("DATA EXPORTER")
        window.resizable(0, 0)
        # header, content, footer
        header = Frame(window, bg='light gray')
        header.grid(row=0, sticky='news')

        content = Frame(window, bg='black')
        content.grid(row=1, sticky='news')

        footer = Frame(window, bg='light gray')
        footer.grid(row=2, sticky='news')

        window.columnconfigure(0, weight=5)

        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=8)
        window.rowconfigure(2, weight=1)
        welcome = Label(header, text="WELOME TO DATA EXPORTER", bg='light gray', fg='black')
        welcome.config(font=("Courier", 20))
        welcome.pack()

        source = IntVar(window,00)
        source_label = Label(content, text="Select source", bg='black', fg='white')
        source_label.grid(row=3,column=1)
        source1 = Radiobutton(content, text="Oracle", variable=source, value=1, bg='black', fg='white')
        source1.grid(row=3, column=2)
        source2 = Radiobutton(content, text="Sqlite", variable=source, value=2, bg='black', fg='white')
        source2.grid(row=3, column=3)
        source3 = Radiobutton(content, text="Mongodb", variable=source, value=3, bg='black', fg='white')
        source3.grid(row=3, column=4)

        destination = IntVar(content,00)
        destination_label = Label(content, text="Select destination", bg='black', fg='white')
        destination_label.grid(row=4, column=1)
        destination1 = Radiobutton(content, text="Oracle", variable=destination, value=1, bg='black', fg='white')
        destination1.grid(row=4, column=2)
        destination2 = Radiobutton(content, text="Sqlite", variable=destination, value=2, bg='black', fg='white')
        destination2.grid(row=4, column=3)
        destination3 = Radiobutton(content, text="Mongodb", variable=destination, value=3, bg='black', fg='white')
        destination3.grid(row=4, column=4)
        next_sepb=Button(content,text="Next", command=next_sep,width=10)
        next_sepb.grid(row=4,column=5)
        cancelB=Button(content,text="Back",command=cancel,width=10)
        cancelB.grid(row=4,column=7)
        print("*************",source.get(),destination.get())
        window.mainloop()

