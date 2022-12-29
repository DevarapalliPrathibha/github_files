import pyodbc
server = 'HCL-02-NEW-08\SQLEXPRESS01'
database = 'Details_of_Employee'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Employee_schema:
    def creating_table(self):
        # query=cursor.execute(''' create database Employee_details '''())
        try:
            values = cursor.execute('''select * from Employee_details_table ''')
            query1 = cursor.execute(''' use Employee_details''')
            query2 = cursor.execute('''create table Employee_details_table(                  
                                         Name varchar(100),
                                         Salary int,
                                         Project varchar(100))
                                    ''')
            cnxn.commit()
        except:
            print("table existed")
obj1 =Employee_schema()
obj1creating_table()