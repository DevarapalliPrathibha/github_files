import pyodbc
import structure
server = 'HCL-02-NEW-08\SQLEXPRESS01'
database = 'Details_of_Employee'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Employee:
    project = ['html', 'python', 'excel']
    bonus = 2
    def __init__(self, Name, Salary, Project):
        self.Name = Name
        self.Salary = Salary
        self.Project = Project
    def tablecreation(self):
        createobj.creating_table()
    def insert_Employee_Details(self):
        query = '''  
                    INSERT INTO Employee_details_table (Name,Salary,Project)
                    VALUES
                    ({0},{1},{2})  '''
        insert_query = query.format(self.Name, self.Salary, self.Project)
        cursor.execute(insert_query)
        cnxn.commit()
    def display_employee_details(self):
        query = '''select * from Employee_details_table where Name = '{0}' '''
        query1 = query.format(self.Name)
        values = cursor.execute(query1)
        for fileinfo in values:
            print("details from DB")

            print("Name={}".format(fileinfo.Name),"Salary={}".format(fileinfo.Salay),("Project={}".format(fileinfo.Project))
    def change_project(self):
        new_project = input()
        try:
            query = '''select * from Employee_details_table where Name='{0}' '''
            searchquery = query.format(self.Name)
            values = cursor.execute(searchquery)
            for fileinfo in values:
                oldproject = fileinfo.Project
                if new_project == oldproject:
                    raise sameproject
                elif (new_project not in self.project):
                    raise Notinlist
                else:
                    query = '''UPDATE Employee_details_table SET Project='{0}' WHERE Name='{1}' '''
                    query1 = query.format(new_project, self.Name)
                    cursor.execute(query1)
                    cnxn.commit()
                    print("new project")
        except Notinlist:
            print("Not listed")
        except sameproject:
            print("same project")
        except:
            pass


obj = structure.Employee_schema()
obj = Employee("prathibha", 619, 200000, "Java")
obj.insert_Employee_Details()
# obj.display_employee_details()
# obj.change_project()

