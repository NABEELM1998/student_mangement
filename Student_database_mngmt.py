#import modules
from cgitb import text
from email.headerregistry import Address
from msilib.schema import Error

from tkinter import *
import tkinter.messagebox
from tkinter.tix import COLUMN
from unicodedata import name
import pymysql
from setuptools import Command

windo = tkinter.Tk()
windo.geometry('750x450')
L = Label(windo,text="Enter a Student ID: ", font=('arial',30), fg='blue')
L.grid(row=0,column=0)
#Entry is for getting the input value from the user
E = Entry(windo,bd=5,width=50)
E.grid(row=0,column=1)

L1 = Label(windo,text="Enter a Student name: ", font=('arial',30), fg='blue')
L1.grid(row=1,column=0)
E1 = Entry(windo,bd=5,width=50)
E1.grid(row=1,column=1)

L2 = Label(windo,text="Enter a Student Address: ", font=('arial',30), fg='blue')
L2.grid(row=2,column=0)
E2 = Entry(windo,bd=5,width=50)
E2.grid(row=2,column=1)

def myButtonEvent(selection):
    print("Studeny id is: ",E.get())
    print("Studeny nAME is: ",E1.get())
    print("Studeny Address is: ",E2.get())
    id = E.get()
    name = E1.get()
    Addres = E2.get()
    if selection in ("Insert"):
        con = pymysql.connect(host='localhost',
                                user='root',
                                password='Nabeelm@86',
                                database='test',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()                                            #get the cursor object
        #cur.execute("select version()")
    # data = cur.fetchone() for checking we can use the database
    # print('My mysql version is ',data)
        query = "CREATE table if not exists student (id char(20) NOT NULL , name char(20), Address char(20))"
    #try:
        cur.execute(query)
        con.commit()  
    # except Error as e:
    #     print("Error occured at database table creation",e)
    #     con.rollback()
    #     con.close()

        insQuery = "Insert into student (id,name,Address) values ('%s','%s','%s')"%(id,name,Addres)
        try:
            cur.execute(insQuery)
            con.commit()
            con.close()
            print("Data Inserted succesfully")
        except Error as e:
            print("Error occured at inserting the data",e)
            con.rollback()
            con.close()
    elif (selection) in ("Update"):
        try:
            con = pymysql.connect(host='localhost',
                                    user='root',
                                    password='Nabeelm@86',
                                    database='test',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
            cur = con.cursor() 
            updQuery = "Update student set name = '%s'"%(name)+",Address = '%s'"%(Addres)+"where id = '%s'"%(id)
            cur.execute(updQuery)
            con.commit()
            con.close()
        except Error as e:
            print("Error occured during updating",e)
            con.rollback()
            con.close()

    elif (selection) in ("Delete"):
        try:
            con = pymysql.connect(host='localhost',
                                    user='root',
                                    password='Nabeelm@86',
                                    database='test',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
            cur = con.cursor() 
            DelQuery = "Delete from student where id = '%s'"%(id)
            cur.execute(DelQuery)
            con.commit()
            con.close()
        except Error as e:
            print("Error occured during deleting rows",e)
            con.rollback()
            con.close()
    
    elif (selection) in ("Select"):
        try:
            con = pymysql.connect(host='localhost',
                                    user='root',
                                    password='Nabeelm@86',
                                    database='test',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
            cur = con.cursor() 
            SelQuery = "Select * from student where id = '%s'"%(id)
            cur.execute(SelQuery)
            rows = cur.fetchall()
            address1 = ''
            name1 = ''
            id1 = ''
            for row in rows:
                id1 = row['id']
                name1 = row['name']
                address1 = row['Address']
            E.delete(0,END)
            E1.delete(0,END)
            E2.delete(0,END)

            E.insert(0,id1)
            E1.insert(0,name1)
            E2.insert(0,address1)
            con.close()
        except Error as e:
            print("Error occured during fetching rows",e)
            con.rollback()
            con.close()










BInsert = tkinter.Button(text='Insert',fg = 'black',bg = 'orange',font=('arial',20,'bold'),command = lambda:myButtonEvent('Insert'))
BInsert.grid(row = 5,column= 0)

BUpdate = tkinter.Button(text='Update',fg = 'black',bg = 'orange',font=('arial',20,'bold'),command = lambda:myButtonEvent('Update'))
BUpdate.grid(row = 5,column= 1)

BDelete = tkinter.Button(text='Delete',fg = 'black',bg = 'orange',font=('arial',20,'bold'),command = lambda:myButtonEvent('Delete'))
BDelete.grid(row = 7,column= 0)

BSelect = tkinter.Button(text='Select',fg = 'black',bg = 'orange',font=('arial',20,'bold'),command = lambda:myButtonEvent('Select'))
BSelect.grid(row = 7,column= 1)

mainloop()