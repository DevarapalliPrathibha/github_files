import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'HCL-02-NEW-08\SQLEXPRESS01'
database = 'FileSearchResults'
username = 'capstone'
password = 'Capstone@123'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

print(cnxn)
cursor = cnxn.cursor()


# reshape

array_stats =np.array( [[1,2,3,7], [4,5,-6,4]])

print(array_stats.reshape((4,2)))

# stacking

a_v1 = np.array([1,2,3,4])

a_v2 = np.array([1,2,3,4])

print(np.array([a_v1, a_v2]))


print(np.hstack([a_v1, a_v2]))
























print(cursor)

cursor.execute('''
                INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                VALUES
                ('E:\Demo_1\Demo_2\Demo_3\empty_file.txt',3,'pinky')
                ''')
cnxn.commit()

values=cursor.execute('select * from FileSearchResults_table')
for i in values:
    print(i)