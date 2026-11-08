import pandas as pd
import pandasql as ps
import pyodbc


######################################################################################################################
# import data

###############
## csv
csv_file_path = 'D:\Test.csv'
df = pd.read_csv(csv_file_path)
df = pd.read_csv(csv_file_path, index_col=None, header=0, skiprows=1, low_memory=False)

##############
## excel
xlsx_file_path = 'D:\Test.xlsx'
df = pd.read_excel(xlsx_file_path, sheet_name='name')  

##############
## multiple files
all_list = glob.glob(r"folder_name\file_name*.csv")
tr_tmp_list = []
for filename in all_list:
    tr_tmp_df = pd.read_csv(filename, index_col=None, header=0)
    tr_tmp_list.append(tr_tmp_df)
    print(filename)  
df_total = pd.concat(tr_tmp_list, axis=0, ignore_index=True)

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
df.to_csv("file_name.csv", index = False)

##############
## excel
df.to_excel('file_name.xlsx')


######################################################################################################################
# pandas preferences
pd.options.display.max_columns = None   # show all of the columns
pd.options.display.max_rows = None      # show all of the rows, use carefully with huge datasets
pd.options.display.max_rows = 200       # not more than 200 rows
pd.options.display.max_colwidth = None  # show full column value
requests.packages.urllib3.disable_warnings(InsecureRequestWarning) # turn off some of the warnings
#from requests.packages.urllib3.exceptions import InsecureRequestWarning

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
df[df["column_1"].isnull()]                 # check if null
    
## Diferent operations
df.drop_duplicates(inplace=True)    # drop duplicates. inplace=True - changes will be applied to the current DF
len(df)                             # get lenght of the DF
    
##############
## Columns

### data type
df['date'] = pd.to_datetime(df['datetime']).dt.date     # to date
df['some_numbers'] = df['some_numbers'].astype(str)     # to string

### rename
df.rename(columns={"column_1": "new_column_1"}, inplace=True)   # column_1 -> new_column_1
df.rename(columns={
    "column_1": "new_column_1",
    "column_2": "new_column_2"
}, inplace=True)

### delete
df.drop(columns = ['column_1', 'new_column_1'], inplace=True) 
df.drop_duplicates(inplace=True)

### dates
df['date'] = df['datetime'].dt.date                             # date from datetime
df['date_month'] = df['datetime'].dt.month                      # month
df['date_day_of_the_year'] = df['datetime'].dt.day_of_year      # day of the year
df['date_weekday'] = df['datetime'].dt.dayofweek                # day of week, 0 – Monday, 6 – Sunday
df['date_hour'] = df['datetime'].dt.hour                        # hour
df['days_since_smth'] = (df['date'] - df['reg_date']).dt.days   # number of days between two dates

df['timestamp_dt'] = pd.to_datetime(df['timestamp'])
df['timestamp_dt_sec'] = df['timestamp_dt'].dt.strftime('%Y-%m-%d %H-%M-%S')
df['timestamp_dt_min'] = df['timestamp_dt'].dt.strftime('%Y-%m-%d %H-%M')
df['timestamp_dt_hr'] = df['timestamp_dt'].dt.strftime('%Y-%m-%d %H')
df['timestamp_minute'] = df['timestamp_dt'].dt.minute
df['timestamp_sec'] = df['timestamp_dt'].dt.second

df['date_id_month'] = pd.to_datetime(df['date_id']).dt.month
df['days_since_registration_check'] = df['date_id_day_of_the_year'] - df['reg_date_day_of_the_year']

timezone_dif = -6
df['date_time'] = pd.to_datetime(df['RequestDate']) \
            + pd.Timedelta(hours=timezone_dif, minutes=0, seconds=0) 
			
df['some_date'] = df['date_time'].astype(str).str[:10]

### calcs (tbd)
df['discount_perc_item_price'] = 100 - round(order_df['net_price_per_item'] / order_df['gross_price_per_item'] * 100, 2)
# delete lambda x? df['items_gross_price'] = df.apply(lambda x: parse_shipping(x['shippings']), axis=1)   # using functions
df['bp_id'].fillna(df['email'], inplace = True)    # use email if bp_id is null
df['bp_id_new'] = np.where(df['bp_id'] == 'qwe', df['email'], df['bp_id']) # use email if bp_id = 'qwe' otherwise use bp_id

df["XX_rank"] = df.groupby(
    ['XX_MID', XX_email', 'XX_date', 'XX_amount']
    )["XX_date_time"].rank(method="first", ascending=True).astype(np.int64)

######### email address parsing
df['email_name'] = df['email'].apply(lambda x: x[:x.find('@')])
df['email_name_wo_bp'] = np.where(df['bp_id'] == '' \
                                           , df['email'].apply(lambda x: x[x.find('|')+1:x.find('@')]) \
                                           , None)
df['email_name_2'] = np.where(df['bp_id'] == '', \
                                       df['email_name_wo_bp'], df['email_name'])
df['email_name_3'] = np.where(df['email'].str.contains('\+') \
                                       , df['email'].apply(lambda x: x[:x.find('+')]) \
                                       , df['email_name_2'])
df['email_domain'] = df['email'].apply(lambda x: x[x.find('@'):])
df['email_normalized'] = df['email_name'].apply(lambda x: re.sub('[^a-zA-Z]+', '', x))
df['email_normalized_2'] = df['email_name_2'].apply(lambda x: re.sub('[^a-zA-Z]+', '', x))
df['email_normalized_3'] = df['email_name_3'].apply(lambda x: re.sub('[^a-zA-Z]+', '', x))

df['email_order_is_guest'] = df['email_order_name_raw'].apply(lambda x: int('|' in x))
df['email_order_name'] = np.where(
    df['email_order_is_guest'] == 1, 
    df['email_order_name_raw'].apply(lambda x: x[x.find('|')+1:]),
    df['email_order_name_raw'])
df['email_order_name_length'] = df['email_order_name'].apply(lambda x: len(x))
df['email_order_name_no_of_digits'] = \
    df['email_order_name'].apply(lambda x: sum(c.isdigit() for c in x))
df['email_order_name_no_of_other_symbols'] = \
    df['email_order_name'].apply(lambda x: sum(not c.isalnum() for c in x))
df['email_order_final'] = df['email_order_name'] + df['email_order_domain']

######### phone address parsing
df['phone_order_str'] = df['Phone Number'].astype(str)
df['phone_order_length'] = np.where(
    df['phone_order_str'] != "nan", 
    df['phone_order_str'].apply(lambda x: len(x)),
    0)

######### names address parsing
df['customer_name_str']  = df['Customer Name'].astype(str)
df['first_name']         = df.apply(lambda x: split_name(x['customer_name_str'], 'First name'), axis=1)
df['last_name']          = df.apply(lambda x: split_name(x['customer_name_str'], 'Last name'), axis=1)
df['first_name_length']  = df['first_name'].apply(lambda x: len(x))
df['first_name_parts']   = df['first_name'].apply(lambda x: len(x.split(' ')))
df['last_name_length']   = df['last_name'].apply(lambda x: len(x))
df['first_name_no_of_other_symbols'] = df['first_name'].apply(lambda x: sum(not c.isalnum() for c in x))
df['last_name_no_of_other_symbols']  = df['last_name'].apply(lambda x: sum(not c.isalnum() for c in x))


##############
## Group by
df.groupby(['column_1', 'column_2'])['column_3'].count()            # group by column_1 and column_2; count(column_3)
df.groupby('column_1', as_index=False).agg({'column_2': "count"})   # group by column_1; count(column_2)
### Rename column
df.groupby('column_1', as_index=False).agg(new_name = ('column_2', "count"))
    
##############
## Order by
df.sort_values('column_1', ascending = False)

##############
# lambda function
df['ProfileName_1'] = df['ProfileName'].apply(lambda x: x.split(',')[0])
df['ProfileName_1'].apply(lambda x: x[x.find('|')+1:])
     
##############
# where
df['Decision'] = np.where(
    df['ProfileName_1'].str.startswith('P'), 
    df['ProfileDecision_2'], 
    df['ProfileDecision_1'])
# case when 
conditions = [
    (df['XX_Decision'] == 'Approved') & (df['YY_Decision'] == 'ACCEPT'),
    (df['XX_Decision'] == 'Approved') & (df['YY_Decision'] == 'REJECT'),
    (df['XX_Decision'] == 'Rejected') & \
        (df['XX_response'].isin(("REASON_1", "REASON_2"))),
    (df['XX_Decision'] == 'Rejected') & \
        (~df['XX_response'].isin(("REASON_1", "REASON_2")))
]
choices = ['All Approved', 'Risk Declined', 'Risk Declined', 'Bank Declined']
df['Final_Decision'] = np.select(conditions, choices, default='error')

############## fill null values by 0
df['return'].fillna(0, inplace = True)
     
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

# data types
df["attr1"]  = df["attr111"].fillna(0).astype(np.int64)
df["attr1"]  = df["attr111"].astype(str) + "_" + df["attr112"].astype(str)


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



### info about dataframes
df.dtypes
# checking basic info
for x in [df, update_df_gender, df_sub_tender]:
    print(x.columns, end='\n\n')
    print(x.dtypes, end='\n\n')
    print(x.describe(include = 'all'), end='\n\n')
    print('---'*30)
#check missing values
print(pd.isnull(df.age).sum())
print(pd.notnull(df.date_of_birth).sum())

df.info()
df.describe()
df.columns

transactions_df.shape

# checking for duplicates
tmp_df = transactions_df.groupby(
    transactions_df.columns.tolist()
).size().reset_index().rename(columns={0:'records'})
print(tmp_df[tmp_df['records'] > 1].sort_values('records', ascending = False))
