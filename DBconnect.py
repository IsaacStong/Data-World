#SQLite
import sqlite3
class SQLiteDB:
    def __init__(self):
        self.connection = sqlite3.connect('TEST')
        self.cursor = self.connection.cursor()

    def insert(self, tableName, command):
        self.cursor.execute('INSERT INTO '+tableName+' VALUES ('+command+');')
        

    def create(self, tableName, tableCols):
        command = "CREATE TABLE "+str(tableName)+" ("+str(tableCols)+");"
        self.cursor.execute(command)

    def getTables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_list = []
        r = self.cursor.fetchall()
        for i in range(len(r)):
            table_list.append(r[i][0])
        return table_list

    def delete(self, tableName):
        self.cursor.execute('DELETE FROM '+tableName)

    def getColumns(self, tableName):
        column_list = []
        for i in self.cursor.execute('PRAGMA table_info('+tableName+');'):
            column_list.append(i[1:3])
        return column_list
        
        


#MongoDB
from pymongo import MongoClient
class MongoDB:
    def __init__(self):
        self.connection = MongoClient("localhost", 27017)
        self.db = self.connection['mydatabase']
        self.emp_rec = {}

    def insert(self, collection, command):
        self.record = {}
        for i in command.split(','):
            result = i.split(':')
            self.record[result[0]] = result[1]
                
        self.db[collection].insert_one(self.record)

    def create(self, collection_name):
        self.db[collection_name].insert_one({"Placeholder": "Test"})

    def delete(self, collection_name):
        self.db[collection_name].drop()

    def getTables(self):
        filter = {"name": {"$regex": r"^(?!system\.)"}}
        user_tables = self.db.list_collection_names(filter=filter)
        return user_tables



#Oracle
import cx_Oracle
class OracleDB():
    def __init__(self):
        self.connection = cx_Oracle.connect("SCOTT/TIGER")
        self.cursor = self.connection.cursor()

    def insert(self, tableName, command):
        self.cursor.execute('INSERT INTO '+tableName+' VALUES ('+command+');')

    def create(self, tableName, tableCols):
        command = "CREATE TABLE "+str(tableName)+" ("+str(tableCols)+");"
        self.cursor.execute(command)

    def getTables(self):
        self.cursor.execute("SELECT table_name FROM user_tables")
        table_list = []
        r = self.cursor.fetchall()
        for i in range(len(r)):
            table_list.append(r[i][0])
        return table_list

    def delete(self, tableName):
        self.cursor.execute('DELETE FROM '+tableName)

    def getColumns(self, tableName):
        column_list = []
        for i in self.cursor.execute("SELECT column_name, data_type FROM USER_TAB_COLUMNS WHERE table_name = '"+tableName+"'"):
            column_list.append(i[0:2])
        return column_list
