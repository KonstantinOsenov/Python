import pandas as pd
import pandasql as ps
import pyodbc


######################################################################################################################
# import data

##############
## csv
csv_file_path = 'D:\Test.csv'
df = pd.read_csv(csv_file_path)

##############
## excel

##############
## DataBase (ExA example)

### 1. Connect to DB (ODBC)
"""
You need to install ODBC driver for a connection to DB
https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
"""
driver = 'ODBC Driver 17 for SQL Server'
server = 'Server_name'
database = 'DB_name'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
cnxn_exa = pyodbc.connect(connection_string)

### 2. SQL query (2 ways)

#### SQL Query
sql_query = 'select top(5) location_id, location_name from exa.dim_location'

#### SQL Query from the file
script_file = 'ExA sql_query with discount.txt'  # file with your query
with open(script_file) as f:
    sql_query = f.read()
f.close()

### 3. Get data
df = pd.read_sql(sql_query, cnxn_exa)


######################################################################################################################
# export data

##############
## csv
df.to_csv("file_name.csv")

##############
## excel
df.to_excel('file_name.xlsx')


######################################################################################################################
# pandas preferences
pd.options.display.max_columns = None   # show all of the columns
pd.options.display.max_rows = None      # show all of the rows, use carefully with huge datasets
pd.options.display.max_rows = 200       # not more than 200 rows
pd.options.display.max_colwidth = None  # show full column value


######################################################################################################################
# Pandas DataFrame

##############
## General info
df.columns                      # column list
df.dtypes                       # column data types
df.shape                        # number of rows and columns
df.describe(include = 'all')    # quick overview of data in DF

##############
## Read
df                              # Whole DF
df.head()                       # First rows
df[['column_1', 'column_2'']]   # Read only 2 columns

##############
## Filters
df[df['country_code'] == 'US']              # by value
df[df.index.isin((53, 55))]                 # by index
df[~df.index.isin((53, 55))]                # '~' - NOT (not in (53, 55))
df[df['column_1'].str.contains('ball')]     # substr 'ball' in column_1

## Diferent operations
df.drop_duplicates(inplace=True)    # drop duplicates. inplace=True - changes will be applied to the current DF
    
##############
## Columns

### data type
df['date'] = pd.to_datetime(df['datetime']).dt.date     # to date
df['some_numbers'] = df['some_numbers'].astype(str)     # to string

### rename
df.rename(columns={"column_1": "new_column_1"}, inplace=True)   # column_1 -> new_column_1

### delete
df.drop(columns = ['column_1', 'new_column_1'], inplace=True) 

### dates
df['date'] = df['datetime'].dt.date                             # date from datetime
df['date_month'] = df['datetime'].dt.month                      # month
df['date_day_of_the_year'] = df['datetime'].dt.day_of_year      # day of the year
df['date_weekday'] = df['datetime'].dt.dayofweek                # day of week, 0 – Monday, 6 – Sunday
df['date_hour'] = df['datetime'].dt.hour                        # hour
df['days_since_smth'] = (df['date'] - df['reg_date']).dt.days   # number of days between two dates

### calcs (tbd)
df['discount_perc_item_price'] = 100 - round(order_df['net_price_per_item'] / order_df['gross_price_per_item'] * 100, 2)
# delete lambda x? df['items_gross_price'] = df.apply(lambda x: parse_shipping(x['shippings']), axis=1)   # using functions
df['bp_id'].fillna(df['email'], inplace = True)    # use email if bp_id is null
df['bp_id_new'] = np.where(df['bp_id'] == 'qwe', df['email'], df['bp_id']) # use email if bp_id = 'qwe' otherwise use bp_id


##############
## Group by
df.groupby(['column_1', 'column_2'])['column_3'].count()            # group by column_1 and column_2; count(column_3)
df.groupby('column_1', as_index=False).agg({'column_2': "count"})   # group by column_1; count(column_2)
### Rename column
df.groupby('column_1', as_index=False).agg("new_name" = ('column_2', "count"))
    
##############
## Order by
df.sort_values('column_1', ascending = False)
    
    
##############
## Visualization (TBD)
df.plot(x="column_1", y="column_2");
df.plot.bar(rot=0)
df.plot.bar()

##############
## Merge / Join
new_df = pd.merge(
    df_1, 
    df_2, 
    how = 'left',
    left_on = 'cust_id', 
    right_on = 'cust_no')
    
    
######################################################################################################################
# PandaSQL
query = """ select * from df """
ps.sqldf(query, locals())       # you can save results as a new DF (new_df = ps.sqldf(query, locals()))

    
    
    





######################################################################################################################
# ToDo ToDo todotodotodotodo later
from datetime import datetime

asd = '2020-02-02 0:01:16'
datetime_object = datetime.strptime(asd, '%Y-%m-%d %H:%M:%S')

#date('2020-02-02')
#'2020-02-02'.to_date()
print(datetime_object)
print(datetime_object.weekday())


# in some cases you shoul use tuple as colum name
.sort_values(('user_id', 'count'), ascending = False)


# Выбор всех колонок в df + переименование итоговой суммы
df_2 = consumption_data_df.groupby(consumption_data_df.columns.tolist()).size().reset_index().\
    rename(columns={0:'records'})


    

# Если надо проселектить колонку "на лету" без создания DF, то надо использовать Tuple
combined_cleaned_df.groupby(['SMP_Station'], as_index=False).agg({
    'artist-track': ['count', 'nunique']
})[[('SMP_Station',''), ('artist-track',   'count'), ('artist-track',   'nunique')]]


# Define data types in DF
data_types = {
    'month': 'string', 
    'id': np.int32, 
    'sum': np.float64
}
df = pd.read_csv('some_data.csv', dtype=data_types)
print(df)
print('-------')
print(df.dtypes)


# union all from several data sources
tmp_list = list()
for filename in ('first_dataset.csv', 'second_dataset.csv'):
    tmp_df = pd.read_csv(filename, index_col=None, header=0)
    tmp_list.append(tmp_df)
tmp_list
final_df = pd.concat(tmp_list, axis=0, ignore_index=True)
final_df

