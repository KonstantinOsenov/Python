import pyodbc

pyodbc.drivers()

driver = 'ODBC Driver 17 for SQL Server' # need to install
# f.ex. https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
server = 'server_name'
database = 'db_name'

con_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
cnxn = pyodbc.connect(con_string)

cursor = cnxn.cursor()
cursor.execute('select top(100) * from abc.abc')

for i in cursor:
    print(i)

# with user and password

user = '' # !!! fill in the username
psw = '' # !!! fill in the password

con_az_sql_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Uid={user};Pwd={psw};'

# another option with a "popup" window when you need to enter credentials
con_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID=<email_address>;Authentication=ActiveDirectoryInteractive;'
cnxn = pyodbc.connect(con_string)

df = pd.read_sql("select 1 from abc.abc", cnxn)
print(len(exa_df))
exa_df.head(10)
