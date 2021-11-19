import sqlite3
import sys

import cx_Oracle
from cx_Oracle import IntegrityError
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class pyloader:
    def __init__(self):
        pass


    def loadToOracle(self,user_ID,table_name,fields,data):
        field_list=fields.split(',')
        s1 = ' VARCHAR2(20),'
        s2 = ''
        for i in field_list:
            s2 = s2 + i + s1

        fields_for_table = s2.rstrip(',')
        try:
            con = cx_Oracle.connect(user_ID)
            cur = con.cursor()
        except:
            return sys.exc_info()[1]
        try:#table already exist
            cur.execute("drop table "+table_name+"")
            create_table ="create table "+table_name+"("+fields_for_table+" )"

            cur.execute(create_table)
            con.commit()

        except:
            try:
                create_table = "create table "+table_name+"("+fields_for_table+" )"
                print(create_table)
                cur.execute(create_table)
                con.commit()
            except:
                print('fix the define Error in create table', sys.exc_info()[1])
                return sys.exc_info()[1]



        try:
            for row in data:
                print(row)
                row=tuple(row)

                data_to_insert = "insert into " + table_name + "(" + fields + ") values{}".format(row)

                cur.execute(data_to_insert)
                con.commit()
            print('your data saved in ORACLE')
            return "done"
        except IntegrityError:
            print('sorry can not add duplicate data')
            return sys.exc_info()[1]
        except:
            print('fix the define Error in insertion', sys.exc_info())
            return sys.exc_info()[1]
        finally:
            cur.close()
            con.close()

    def loadToSqlite(self,db_name,table_name,fields,data):
        fields_list=fields.split(',')
        s1 = ' VARCHAR(20),'
        s2 = ''
        for i in fields_list:
            s2 = s2 + i + s1

        fields_for_table = s2.rstrip(',')
        try:
            con_sqlite = sqlite3.connect(db_name)
            cur_sqlite = con_sqlite.cursor()
            try:
                cur_sqlite.execute("drop table "+ table_name)
                con_sqlite.commit()
                create_table = "CREATE TABLE  " + table_name + "(" + fields_for_table + ");"

                cur_sqlite.execute(create_table)
                con_sqlite.commit()
            except :

                print('in table creation')
                create_table = "CREATE TABLE  " + table_name + "(" + fields_for_table + ");"

                cur_sqlite.execute(create_table)
                con_sqlite.commit()

            try:
                for row in data:
                    row = tuple(row)
                    cur_sqlite.execute("insert into " + table_name + "(" + fields + ") values{};".format(row))

                    con_sqlite.commit()
            except:

                print('fix the define Error for insertion', sys.exc_info()[1])
                return sys.exc_info()[1]



            con_sqlite.close()

            print('your data saved in SQLITE')
            return "done"
        except:
            print('in insertion')

            print('fix the define Error', sys.exc_info()[1])
            return sys.exc_info()[1]
    def loadToMongodb(self,hostname,address,db_name,table_name,fields,data):
        fields = fields.split(',')
        fields_dict = dict()
        try:
            myclient = MongoClient(hostname, address)  # MongoClient('localhost', 27017)
            dblist = myclient.list_database_names()

            db = myclient[db_name]
            collist = db.list_collection_names()
            if table_name in collist:
                db[table_name].drop()
                my_table = db[table_name]
            else:
                my_table=db[table_name]

            for row in data:
                for index in range(len(fields)):
                    fields_dict[fields[index]] = str(row[index])

                db[table_name].insert_one(fields_dict)
                fields_dict = dict()

            myclient.close()
            print('your data saved in MONGODB')
            return "done"

        except DuplicateKeyError:
            print('sorry can not enter duplicate values')
            return sys.exc_info()[1]

        except:
            print('fix the define Error', sys.exc_info()[1])
            return sys.exc_info()[1]


