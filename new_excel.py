import os
import tkinter as tk
from tkinter import *
from fpdf import FPDF
from tkinter import filedialog
from create_excel import create_excel
from data_exporter1 import DATA_EXPOTER
from tkinter.messagebox import showinfo

class kinter_excel():
    def __init__(self):
        pass

    def make_excel(self):

        def create_excel_from_oracle():



            def quit_O():
                top_o.destroy()
            def cancel_O():
                quit_O()
                obj=kinter_excel()
                obj.make_excel()

            def create_excelO(user_name, password, table_name):
                print(table_name)
                table_name = str(table_name)
                print(table_name)

                fields = ""
                obj_source = DATA_EXPOTER()
                data = obj_source.get_from_oracle(user_name, password, table_name, fields)

                fields_list = obj_source.get_fields_from_oracle(user_name, password, table_name)
                if isinstance(data, list):
                    if isinstance(fields_list, list):
                        obj = create_excel()
                        message1=obj.create__excel_ofData(table_name, fields_list, data)
                        if message1=="done":
                            showinfo("DONE", table_name + ".xlsx excel IS CREATED")
                            cancel_O()

                            file_name = os.path.abspath("excel\\"+table_name + ".xlsx")
                            os.startfile(file_name)
                        else:
                            showinfo(title="Error",message=message1)







                    else:
                        showinfo(title="Error", message=fields_list)


                else:
                    showinfo(title="Error", message=data)


            def get_tablesO():

                def resetO():
                    user_nameO.delete(0, 'end')
                    password.delete(0, 'end')
                    table_labelORACLE.grid_forget()
                    popupMenu.grid_forget()
                    pdf.grid_forget()
                    get_b.grid(row=1, column=2)
                    user_nameO.focus()

                obj = DATA_EXPOTER()
                t_names = obj.get_tables_from_oracle(user_nameO.get(), password.get())
                if isinstance(t_names,list):
                    table_labelORACLE = Label(content, text="select table name", bg='light gray')
                    table_labelORACLE.grid(row=2, column=0)
                    table_nameORACLE = StringVar(content)
                    table_nameORACLE.set("-select-")
                    popupMenu = OptionMenu(content, table_nameORACLE, *t_names)
                    popupMenu.grid(row=2, column=1)
                    pdf = Button(content, text="Create EXCEL",
                                 command=lambda: create_excelO(user_nameO.get(), password.get(), table_nameORACLE.get()))
                    pdf.grid(row=3, column=1)
                    reset_b = Button(content, text="reset", command=resetO)
                    reset_b.grid(row=3, column=0)
                else:
                    showinfo(title="Error",message=t_names)
                    user_nameO.delete(0, 'end')
                    password.delete(0, 'end')


                    user_nameO.focus()







            top_o = Tk()
            top_o.geometry("600x300")
            top_o.title("Create excel")
            top_o.resizable(0, 0)

            # header, content, footer
            header = Frame(top_o, bg='light gray')
            header.grid(row=0, sticky='news')

            content = Frame(top_o, bg='black')
            content.grid(row=1, sticky='news')

            footer = Frame(top_o, bg='light gray')
            footer.grid(row=2, sticky='news')

            top_o.columnconfigure(0, weight=5)

            top_o.rowconfigure(0, weight=1)
            top_o.rowconfigure(1, weight=8)
            top_o.rowconfigure(2, weight=1)
            welcome = Label(header, text="CREATE EXCEL FROM ORACLE", bg='light gray', fg='black')
            welcome.config(font=("Courier", 20))
            welcome.pack()
            
            l1 = Label(content, text="Enter user name", bg="black", fg='white')
            l1.grid(row=0, column=0)
            user_nameO = Entry(content)
            user_nameO.grid(row=0, column=1)
            pas_l = Label(content, text="Enter Password", bg="black", fg='white')
            pas_l.grid(row=1, column=0)
            password = Entry(content,show="*")

            password.grid(row=1, column=1)
            get_b = Button(content, text="Get Tables", command=get_tablesO)
            get_b.grid(row=1, column=2)
            cancle_bO=Button(content,text="Back", command=cancel_O)
            cancle_bO.grid(row=1,column=3)
            #password.bind("<FocusOut>", get_tablesO)





#-------------------------------------------------------------------------------------------------------------------------------------------




        def create_excel_from_sqlite():


            def quit_S():
                top_s.destroy()
            def cancel_S():
                quit_S()
                obj=kinter_excel()
                obj.make_excel()

            def create_excelS(db_name, table_name):

                fields = ""
                obj_source = DATA_EXPOTER()
                data = obj_source.get_from_sqlite(db_name, table_name, fields)
                fields_list = obj_source.get_fields_from_sqlite(db_name, table_name)

                if isinstance(data, list):
                    if isinstance(fields_list, list):
                        obj = create_excel()
                        message1=obj.create__excel_ofData(table_name, fields_list, data)
                        if message1=="done":
                            showinfo("DONE", table_name + ".xlsx excel IS CREATED")

                            file_name = os.path.abspath("excel\\"+table_name + ".xlsx")
                            os.startfile(file_name)
                            cancel_S()
                        else:
                            showinfo(title="Error",message=message1)






                    else:
                        showinfo(title="Error", message=fields_list)


                else:
                    showinfo(title="Error", message=data)

            def get_tablesO():
                def resetS():
                    db_name.delete(0, 'end')
                    table_labelS.grid_forget()
                    popupMenu.grid_forget()
                    pdf.grid_forget()
                    get_b.grid(row=0,column=2)



                    db_name.focus()


                obj = DATA_EXPOTER()
                t_names = obj.get_tables_from_sqlite(db_name.get())
                if isinstance(t_names,list):
                    get_b.grid_forget()
                    table_labelS = Label(content, text="select table name", bg='light gray')
                    table_labelS.grid(row=2, column=0)
                    table_nameS = StringVar(content)
                    table_nameS.set("-Select-")
                    popupMenu = OptionMenu(content, table_nameS, *t_names)
                    popupMenu.grid(row=2, column=1)
                    pdf = Button(content, text="Create EXCEL",
                                 command=lambda: create_excelS(db_name.get(), table_nameS.get()))
                    pdf.grid(row=3, column=1)
                    reset_b = Button(content, text="reset", command=resetS)
                    reset_b.grid(row=3, column=0)
                else:
                    showinfo(title="Error",message=t_names)
                    db_name.delete(0,'end')
                    db_name.focus()



            top_s = Tk()
            top_s.geometry("600x300")
            top_s.title("Create excel")
            top_s.resizable(0, 0)
            # header, content, footer
            header = Frame(top_s, bg='light gray')
            header.grid(row=0, sticky='news')

            content = Frame(top_s, bg='black')
            content.grid(row=1, sticky='news')

            footer = Frame(top_s, bg='light gray')
            footer.grid(row=2, sticky='news')

            top_s.columnconfigure(0, weight=5)

            top_s.rowconfigure(0, weight=1)
            top_s.rowconfigure(1, weight=8)
            top_s.rowconfigure(2, weight=1)
            welcome = Label(header, text="CREATE EXCEL FROM SQLITE", bg='light gray', fg='black')
            welcome.config(font=("Courier", 20))
            welcome.pack()

            l1 = Label(content, text="Enter database name", bg="black", fg='white')
            l1.grid(row=0, column=0)
            db_name = Entry(content)
            db_name.grid(row=0, column=1)
            get_b=Button(content,text="Get Tables",command=get_tablesO)
            get_b.grid(row=0, column=2)
            cancel_b1=Button(content,text="Back",command=cancel_S)
            cancel_b1.grid(row=0,column=3)
            #db_name.bind("<FocusOut>", get_tablesO)



#----------------------------------------------------------------------------------------------------------------------------------




        def create_excel_from_mongodb():




            def quit_M():
                top_m.destroy()
            def cancel_M():
                quit_M()
                obj=kinter_excel()
                obj.make_excel()

            def create_excelM(db_name, table_name):


                hostname = "localhost"
                address = 27017
                fields = ''
                obj_source = DATA_EXPOTER()
                data = obj_source.get_from_mongodb(hostname, address, db_name, table_name, fields)
                fields_list = obj_source.get_fields_from_mongodb(hostname, address, db_name, table_name)

                if isinstance(data, list):
                    if isinstance(fields_list, list):
                        obj = create_excel()
                        message1=obj.create__excel_ofData(table_name, fields_list, data)
                        if message1=="done":
                            showinfo("DONE", table_name + ".xlsx excel IS CREATED")

                            file_name = os.path.abspath("excel\\"+table_name + ".xlsx")
                            os.startfile(file_name)
                            cancel_M()
                        else:
                            showinfo(title="Error",message=message1)






                    else:
                        showinfo(title="Error", message=fields_list)


                else:
                    showinfo(title="Error", message=data)

            def get_tablesO():

                def resetM():
                    db_name.delete(0, 'end')
                    table_labelM.grid_forget()
                    popupMenu.grid_forget()
                    pdf.grid_forget()
                    get_b.grid(row=0,column=2)

                    db_name.focus()

                obj = DATA_EXPOTER()
                t_names = obj.get_tables_from_mongodb("localhost",27017,db_name.get())
                if isinstance(t_names,list):
                    get_b.grid_forget()
                    table_labelM = Label(content, text="select table name", bg='light gray')
                    table_labelM.grid(row=2, column=0)
                    table_nameM = StringVar(content)
                    table_nameM.set("-select-")
                    popupMenu = OptionMenu(content, table_nameM, *t_names)
                    popupMenu.grid(row=2, column=1)
                    pdf = Button(content, text="Create EXCEL",
                                 command=lambda: create_excelM(db_name.get(), table_nameM.get()))
                    pdf.grid(row=3, column=1)
                    reset_b = Button(content, text="reset", command=resetM)
                    reset_b.grid(row=3, column=0)
                else:
                    showinfo(title="Error",message=t_names)
                    db_name.delete(0,'end')
                    db_name.focus()



            top_m = Tk()
            top_m.geometry("600x300")
            top_m.title("Create excel")
            top_m.resizable(0, 0)
            # header, content, footer
            header = Frame(top_m, bg='light gray')
            header.grid(row=0, sticky='news')

            content = Frame(top_m, bg='black')
            content.grid(row=1, sticky='news')

            footer = Frame(top_m, bg='light gray')
            footer.grid(row=2, sticky='news')

            top_m.columnconfigure(0, weight=5)

            top_m.rowconfigure(0, weight=1)
            top_m.rowconfigure(1, weight=8)
            top_m.rowconfigure(2, weight=1)
            welcome = Label(header, text="CREATE EXCEL FROM MONGODB", bg='light gray', fg='black')
            welcome.config(font=("Courier", 20))
            welcome.pack()

            l1 = Label(content, text="Enter database name", bg="black", fg='white')
            l1.grid(row=0, column=0)
            db_name = Entry(content)
            db_name.grid(row=0, column=1)
            get_b = Button(content, text="Get Tables", command=get_tablesO)
            get_b.grid(row=0, column=2)
            cancel2=Button(content,text="Back",command=cancel_M)
            cancel2.grid(row=0,column=3)




#---------------------------------------------------------------------------------------------------------------------
        def create_excel_from_file():
            def create_pdf():

                data = []
                file_name_list = file_name.get().split(".")
                if file_name_list[-1].lower() == "txt":

                    good = 1
                else:
                    showinfo(message='Sorry enter or select only txt file ')
                    file_name.delete(0, 'end')
                    file_name.focus()
                    good = 0
                if good == 1:
                    file_name1 = os.path.abspath(file_name.get())
                    if os.path.isfile(file_name1) == False:
                        showinfo(message='file' + file_name.get() + 'does not exist')
                        resetF()
                    elif table_name.get()=="":
                        showinfo(title="Error",message="Enter table name")


                    elif os.path.isfile(file_name1):
                        fh = list(open(file_name1, 'r'))
                        if v.get() == 1:
                            for index in range(len(fh)):
                                if index == 0:
                                    fields_fromFile = fh[index].rstrip().split(separator.get())
                                    if len(fields_fromFile) == 1:
                                        showinfo(message='Sorry Wrong separator Entered')
                                        separator.delete(0, "end")
                                        separator.focus()
                                        flag = 0

                                    else:
                                        #fields_fromFile = ','.join(fields_fromFile)
                                        flag = 1

                                else:
                                    if flag == 0:
                                        break
                                    row = []
                                    row = fh[index].rstrip().split(separator.get())
                                    if len(row) == 1:
                                        showinfo(message='Sorry Wrong separator Entered')
                                        separator.delete(0, "end")
                                        separator.focus()
                                        flag = 0

                                    else:
                                        data.append(row)
                                        flag = 1
                            if flag == 1:
                                obj = create_excel()
                                message1=obj.create__excel_ofData(table_name.get(), fields_fromFile, data)
                                if message1=="done":
                                    showinfo("DONE", table_name.get() + ".xlsx excel IS CREATED")
                                    file_name1 = os.path.abspath("excel\\"+table_name.get() + ".xlsx")
                                    os.startfile(file_name1)
                                    resetF()
                                else:showinfo(title="Error",message=message1)



                        elif v.get() == 0:
                            if fields.get()=="":
                                showinfo(title="Error",message="Enter fields")
                                flag = 0
                            else:
                                flag = 0
                                for index in range(len(fh)):
                                    row = []
                                    row = fh[index].rstrip().split(separator.get())
                                    if len(row) == 1:
                                        showinfo(message='Sorry Wrong separator Entered')
                                        separator.delete(0, "end")
                                        separator.focus()
                                        flag = 0
                                        break

                                    else:
                                        data.append(row)
                                        flag = 1


                            if flag == 1:
                                fields_fromFile=(fields.get()).split(",")
                                obj = create_excel()
                                message1=obj.create__excel_ofData(table_name.get(), fields_fromFile, data)
                                if message1=="done":
                                    showinfo("DONE", table_name.get() + ".xlsx excel IS CREATED")
                                    file_name1 = os.path.abspath(table_name.get() + ".xlsx")
                                    os.startfile(file_name1)
                                    resetF()
                                else:
                                    showinfo(title="Error",message=message1)

                                                                #to_destination(fields.get(), data)
                        else:
                            showinfo(message='make a selection for header')
                            resetF()

                #***************************************************************************************************************************************




            # ------------------------------------------------------
            #----------------------------------------
            def resetF():
                file_name.delete(0, 'end')
                separator.delete(0, 'end')

                table_name.delete(0, 'end')
                fields.delete(0, 'end')
                l4.grid_forget()
                table_name.grid_forget()
                l5.grid_forget()
                fields.grid_forget()
                pdf.grid_forget()
                file_name.focus()
                next_step.grid(row=4, column=1)
            #bb----------------------------------------
            def nextstep_forPDF():
                if file_name.get()=="":
                    showinfo(title="Error",message="Enter a file name")
                    file_name.focus()
                elif separator.get()=="":
                    showinfo(title="Error", message="Enter a separator")
                    separator.focus()


                elif v.get() == 1:
                    l4.grid(row=2, column=0)
                    table_name.grid(row=2, column=1)

                    next_step.grid_forget()
                    pdf.grid(row=4, column=1)
                    reset_b.grid(row=4, column=0)

                elif v.get() == 0:
                    l4.grid(row=2, column=0)
                    table_name.grid(row=2, column=1)

                    l5.grid(row=3, column=0)
                    fields.grid(row=3, column=1)
                    next_step.grid_forget()
                    pdf.grid(row=4, column=1)
                    reset_b.grid(row=4, column=0)
            def fnBrowseButton():
                filename = filedialog.askopenfilename()
                absPath.set(filename)
            def quit_F():
                top.destroy()
            def cancel_F():
                quit_F()
                obj=kinter_excel()
                obj.make_excel()

            top = Tk()
            top.geometry("600x400")
            top.title("Create excel")
            top.resizable(0, 0)
            # header, content, footer
            header = Frame(top, bg='light gray')
            header.grid(row=0, sticky='news')

            content = Frame(top, bg='black')
            content.grid(row=1, sticky='news')

            footer = Frame(top, bg='light gray')
            footer.grid(row=2, sticky='news')

            top.columnconfigure(0, weight=5)

            top.rowconfigure(0, weight=1)
            top.rowconfigure(1, weight=8)
            top.rowconfigure(2, weight=1)
            welcome = Label(header, text="CREATE EXCEL FROM TEXT FILE", bg='light gray', fg='black')
            welcome.config(font=("Courier", 20))
            welcome.pack()



            # ***************************************
            absPath = StringVar(content)
            file_name_lable = Label(content, text="Select A file", bg="black", fg='white', anchor=W, justify=LEFT,
                                    width=20)
            file_name_lable.grid(row=0, column=0)
            file_name = Entry(content, textvariable=absPath,state=DISABLED)
            file_name.grid(row=0, column=1)
            buttonFileName = Button(content, text='Browse...', command=fnBrowseButton)
            buttonFileName.grid(row=0, column=2)
            sep = Label(content, text="Enter separator in file", bg="black", fg='white', justify=LEFT, anchor=W, width=20)
            sep.grid(row=0, column=3)
            separator = Entry(content)
            separator.grid(row=0, column=4)

            header_lable = Label(content, text="Is There Header In File", bg="black", fg='white', justify=LEFT, anchor=W,
                                 width=20)
            header_lable.grid(row=1, column=0)

            v = IntVar(content, 00)
            destination = StringVar(content, '**')
            header_value1 = Radiobutton(content, text="Yes", value=1, variable=v, bg="black", fg='white', justify=LEFT,
                                        anchor=W)
            header_value1.grid(row=1, column=1)
            header_value0 = Radiobutton(content, text="No", value=0, variable=v, bg="black", fg='white', justify=LEFT,
                                        anchor=W)
            header_value0.grid(row=1, column=2)
            next_step = Button(content, text="Next", command=nextstep_forPDF)
            next_step.grid(row=4, column=1)
            cancelf=Button(content,text="Cancel",command=cancel_F)
            cancelf.grid(row=4,column=2)
            reset_b = Button(content, text="Reset", command=resetF)
            reset_b.grid(row=4, column=0)
            l4 = Label(content, text="Enter table Name", bg='light gray')
            # l4.grid(row=2, column=0)
            table_name = Entry(content)
            # table_name.grid(row=2, column=1)

            l5 = Label(content, text="Enter Fields with comma", bg='light gray')
            # l5.grid(row=3, column=0)
            fields = Entry(content)
            # fields.grid(row=3, column=1)
            pdf = Button(content, text="Create EXCEL", command=create_pdf)

            # pdf.grid(row=2, column=2)


            top.mainloop()

        #-----------------------------------------------------

        def quit():
            window.destroy()


        def cancel():
            quit()
            import MainClass


            obj = MainClass.main_project()
            obj.mainpage()

        def action():

            if source.get() == 4:
                quit()

                create_excel_from_file()
            elif source.get() == 1:
                quit()
                create_excel_from_oracle()
            elif source.get() == 2:
                quit()

                create_excel_from_sqlite()
            elif source.get() == 3:
                quit()

                create_excel_from_mongodb()
            else:
                showinfo(title="Error",message="Select a source")



        window = Tk()

        window.geometry("600x200")
        window.title("CREATE EXCEL")
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
        welcome = Label(header, text="CREATE EXCEL HERE", bg='light gray', fg='black')
        welcome.config(font=("Courier", 20))
        welcome.pack()

        source = IntVar(window, 00)
        source_label = Label(content, text="Select source",bg="black", fg='white')
        source_label.grid(row=3, column=1)
        source1 = Radiobutton(content, text="Oracle", variable=source, value=1,bg="black", fg='white')
        source1.grid(row=3, column=2)
        source2 = Radiobutton(content, text="Sqlite", variable=source, value=2,bg="black", fg='white')
        source2.grid(row=3, column=3)
        source3 = Radiobutton(content, text="Mongodb", variable=source, value=3,bg="black", fg='white')
        source3.grid(row=3, column=4)
        source4 = Radiobutton(content, text="Text File", variable=source, value=4,bg="black", fg='white')
        source4.grid(row=3, column=5)
        next_b = Button(content, text="Next", command=action)
        next_b.grid(row=3, column=6)
        cancel_b = Button(content, text="Back", command=cancel)
        cancel_b.grid(row=3, column=7)
