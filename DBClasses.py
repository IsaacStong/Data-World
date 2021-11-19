import sqlite3

class dataBaseManager():

    #Initialization forms connection with File and creates cursor
    def __init__(self, connect):
        self.connection = sqlite3.connect(connect)
        self.cursor = self.connection.cursor()

    #Runs the database manager    
    def run(self):
        #Get Input
        print("1. INSERT \n 2. UPDATE \n 3. DELETE \n 4. SELECT \n 5. EXIT\n")
        ch = input("Please choose [1-5]: ")

        #Run Correct Tool
        if ch=='1':
            self.runInsert()
        elif ch=='2':
            self.runUpdate()
        elif ch=='3':
            self.runDelete()
        elif ch=='4':
            self.runSelect()
        elif ch=='5':
            self.connection.close()
            print("Connection Cut")
            exit()
        else:
            print("Please select valid input from list.\n")
            self.run()

    #Runs the insert tool
    def runInsert(self):
        try:
            #Collect input and create command
            cols = input("Column names you'd like inserted seperated by commas and a space: \n")
            vals = input("Values you'd like inserted seperated by commas, a space, and strings in double quotes, in same order as columns entered: \n")
            command = "INSERT INTO EMP("+cols+") VALUES("+vals+");"
            print(command)

            #Run DB Code
            self.cursor.execute(command)
            self.connection.commit()
            print('Record Inserted!')
        except sqlite3.OperationalError:
            print("\n Command couldn't be run try rechecking your syntax and making sure all your columns exist in the table. \n")
        finally:
            self.run()

    #Runs the update tool
    def runUpdate(self):
        try:
            #Collect input and create command
            new_values = input("Column names you'd like to update followed by new values in format (column1 = value1, column2 = value2) with string values in double quotes: ")
            condition = input("Condition you'd like to set for changing these values: ")
            command = "UPDATE EMP SET "+new_values+" WHERE "+condition+" ;"

    
            #Run DB Code
            self.cursor.execute(command)
            self.connection.commit()
            print("Update Finished!")
        except sqlite3.OperationalError:
            print("\n Command couldn't by run try rechecking your syntax and making sure all your columns exist in the table. ")
            print(" Remember updated values should be entered in form col=newval, col2=newval2, ...etc and a condition is required. \n")
        finally:
            self.run()

    #Runs the delete tool
    def runDelete(self):
        try:
            #Collect input and create command
            condition = input("Please enter deletion condition: ")
            command = "DELETE FROM EMP WHERE "+condition+";"

            #Run DB Code
            self.cursor.execute(command)
            self.connection.commit()
            print("Deletion Finished!")
        except sqlite3.OperationalError:
            print("\n Command couldn't by run try rechecking your syntax and making sure your conditon is populated and accurate this is required to avoid unwanted deletion. \n")
        finally:
            self.run()
    
    #Runs Select Tool showing all data in table
    def runSelect(self):
        try:
            #Collect input and create command
            command = "SELECT * FROM EMP;"
    
            #Run DB Code
            self.cursor.execute(command)
            r = self.cursor.fetchall()
            for i in r:
                print(i)
            print('Done!')
        finally:
            self.run()
