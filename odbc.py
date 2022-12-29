import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=HCL-02-NEW-08\SQLEXPRESS01;'
                     'Database=FileSearchResults;'
                     'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('''
                INSERT INTO FileSearchResults_table(File_Location,SearchCount,NameofFile)
                VALUES
                ('E:\Demo_1\empty_file.txt',1,'empty_file.txt'),
                ("E:\Demo_1\Demo_2\Demo_3\empty_file.txt",3,'empty_file.txt')
                ''')
conn.commit();
#cursor.execute('Select * From FileSearchResults_table')
#File_input = 'empty_file.txt'