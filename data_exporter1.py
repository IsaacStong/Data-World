import  sqlite3
import sys

import cx_Oracle
from cx_Oracle import IntegrityError
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class DATA_EXPOTER:
    def __init__(self):

        pass
    def get_tables_from_sqlite(self, db_name):
        try:
            con_sqlite = sqlite3.connect(db_name)
            cur_sqlite = con_sqlite.cursor()
            SELECT = "SELECT name FROM sqlite_master WHERE type='table';"

            cur_sqlite.execute(SELECT)
            result = cur_sqlite.fetchall()
            data=[]


            for row in result:
                data.append(row[0])
            if data:
                return data
            else:
                return "Database does not exist or there is no table in database"
        except:
            return sys.exc_info()[1]



    def get_fields_from_sqlite(self,db_name,table_name):
        try:
            con_sqlite = sqlite3.connect(db_name)
            cur_sqlite = con_sqlite.cursor()
            select_data = "select DISTINCT * from " + table_name + ";"

            table = cur_sqlite.execute(select_data)
            lstColumns = list(map(lambda x: x[0], table.description))

            return lstColumns
        except:
            return sys.exc_info()[1]




    def get_from_sqlite(self,db_name,table_name,fields):
        if fields:
            try:
                con_sqlite = sqlite3.connect(db_name)
                cur_sqlite = con_sqlite.cursor()
                select_data = "select DISTINCT " + fields + " from " + table_name + ";"
                cur_sqlite.execute(select_data)
                result = cur_sqlite.fetchall()
                return result
            except:
                print('fix the define Error', sys.exc_info()[1])
                return sys.exc_info()[1]
        else:
            try:
                con_sqlite = sqlite3.connect(db_name)
                cur_sqlite = con_sqlite.cursor()
                select_data = "select DISTINCT * from " + table_name + ";"

                table=cur_sqlite.execute(select_data)
                lstColumns = list(map(lambda x: x[0], table.description))
                result = cur_sqlite.fetchall()
                return result
            except:
                print('fix the define Error', sys.exc_info()[1])
                return sys.exc_info()[1]






    def put_in_sqlite(self,db_name,table_name,data,fields):
        try:
            con_sqlite = sqlite3.connect(db_name)
            cur_sqlite = con_sqlite.cursor()
            for row in data:
                field1 = str(row[0])
                field2 = row[1]
                field3 = str(row[2])
                cur_sqlite.execute("insert into " + table_name + "("+fields+") values(?,?,?);",
                                   (field1, field2, field3))
                con_sqlite.commit()
            con_sqlite.close()

            print('your data saved in SQLITE')
        except:
            print('fix the define Error', sys.exc_info()[0])


#---------------------------------------------------------------------------------------
    def get_tables_from_oracle(self, username, password):
        try:
            con_o = cx_Oracle.connect(username + '/' + password)
            cur_o = con_o.cursor()
            SELECT = "select table_name from user_tables order by table_name"

            cur_o.execute(SELECT)
            result = cur_o.fetchall()
            data = []
            for i in result:
                data.append(i[0])
            return data
        except:
            return sys.exc_info()[1]



    def get_fields_from_oracle(self, username, password, table_name):
        try:
            con_o = cx_Oracle.connect(username + '/' + password)
            cur_o = con_o.cursor()
            table = cur_o.execute('select DISTINCT * from ' + table_name)
            lstColumns = list(map(lambda x: x[0], table.description))
            return lstColumns
        except:
            return sys.exc_info()[1]




    def get_from_oracle(self,user_name,password,table_name,fields):

        if fields:
            try:
                con_o = cx_Oracle.connect(user_name + '/' + password)
                cur_o = con_o.cursor()

                cur_o.execute('select DISTINCT ' + fields + ' from ' + table_name)
                result = cur_o.fetchall()

                return result
            except:
                print('fix the define Error', sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
                return sys.exc_info()[1]
        else:
            try:
                con_o = cx_Oracle.connect(user_name + '/' + password)
                cur_o = con_o.cursor()

                cur_o.execute('select  * from ' + table_name)

                result = cur_o.fetchall()

                return result
            except:
                print('fix the define Error', sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
                return sys.exc_info()[1]



    def put_in_oracle(self,user_name,password,table_name,data,fields):
        try:
            con_o = cx_Oracle.connect('' + user_name + '/' + password + '')
            cur_o = con_o.cursor()
            for row in data:
                field1 = str(row[0])
                field2 = row[1]
                field3 = str(row[2])
                data_to_insert = "insert into " + table_name + "("+fields+") values(" + field1 + ",'" + field2 + "'," + field3 + ")"
                cur_o.execute(data_to_insert)
                con_o.commit()
            print('your data saved in ORACLE')
        except IntegrityError:
            print('sorry can not add duplicate data')
        except:
                print('fix the define Error', sys.exc_info())

#-----------------------------------------------------------------------------------
    def get_tables_from_mongodb(self,hostname,address,db_name):
        try:
            myclient = MongoClient(hostname, address)  # MongoClient('localhost', 27017)
            dblist = myclient.list_database_names()

            if db_name in dblist:
                db = myclient[db_name]
                collist = db.list_collection_names()
                return collist
            else:
                return "Database does not exist or \n there is no table in database"
        except:
            return sys.exc_info()[1]



    def get_fields_from_mongodb(self,hostname,address,db_name,table_name):
        try:
            client_m = MongoClient(hostname, address)  # MongoClient('localhost', 27017)
            db = client_m[db_name]
            cursor = db[table_name].find()

            lstColumns = []
            for values in cursor:

                for key in values:
                    if key != '_id':
                        lstColumns.append(key)

            lstColumns = set(lstColumns)
            return list(lstColumns)
        except:
            return sys.exc_info()[1]

    def get_from_mongodb(self,hostname,address,db_name,table_name,fields):
        if fields:
            fields = fields.split(',')
            fields_dict = dict()
            for value in fields:
                fields_dict[value] = 1

            data = []

            try:
                client_m = MongoClient(hostname, address)  # MongoClient('localhost', 27017)
                db = client_m[db_name]
                cursor = db[table_name].find({}, fields_dict)
                print(cursor)
                for index in cursor:
                    row = []
                    print(index)
                    row.append(index[fields[0]])
                    row.append(index[fields[1]])
                    row.append(index[fields[2]])
                    data.append(row)

                print(data)
                return data
            except:
                print('fix the define Error', sys.exc_info()[0])
                return sys.exc_info()[1]
        else:
            data = []
            lstColumns=[]

            try:
                client_m = MongoClient(hostname, address)  # MongoClient('localhost', 27017)
                db = client_m[db_name]
                cursor = db[table_name].find()
                print(cursor)
                for values in cursor:
                    print(values)
                    row = []
                    for key in values:
                        if key != '_id':

                            lstColumns.append(key)
                            row.append(values[key])

                    data.append(row)

                print(data)
                lstColumns=set(lstColumns)
                return data
            except:
                print('fix the define Error', sys.exc_info()[0])
                return sys.exc_info()[1]

    def put_in_mongodb(self,hostname,address,db_name,table_name,data,fields):
        fields = fields.split(',')
        fields_dict = dict()
        try:
            client_m = MongoClient(hostname, address)  # MongoClient('localhost', 27017)
            db = client_m[db_name]

            for row in data:
                fields_dict[fields[0]] = str(row[0])
                fields_dict[fields[1]]  = row[1]
                fields_dict[fields[2]]  = str(row[2])
                db[table_name].insert_one(fields_dict)
                fields_dict = dict()
            client_m.close()
            print('your data saved in MONGODB')
        except DuplicateKeyError:
            print('sorry can not enter duplicate values')

        except:
            print('fix the define Error', sys.exc_info()[0])


