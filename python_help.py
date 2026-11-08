#################################
## regexp
#################################
import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
x

# read file
script_file = 'some_scripts.txt'   # file with SQL query
with open(script_file) as f:
    query_example = f.read()              # save query to 'query_faas' variable
f.close()


# dates
datetime.strptime('2022-03-01', '%Y-%m-%d').date()

# pandasql
import pandasql as ps
q = f""" select * from df """
ps.sqldf(q, locals())



def get_unique_values(input_list, list_len):
    output_list = list()
    output_str = ''
    prev_value = ''
    cur_value = ''
    for i in range(list_len):
        cur_value = str(input_list[i])
        if i == 0:
            output_list.append(cur_value)
            prev_value = cur_value
        elif prev_value == cur_value:
            pass
        else:
            output_list.append(cur_value)
            prev_value = cur_value
    
    output_str = ', '.join(output_list)
    
    return output_str

#get_unique_values([3, 2, 2, 8, 2, 8], 6)

udf_get_unique_values = udf(get_unique_values, StringType())




# Download CSV
import requests
import pandas as pd
from io import StringIO

rs = requests.Session()
some_url = "https://raw.githubusercontent.com/KonstantinOsenov/Python/5091a079f6eb3a6f0cf9964be48dbfb854f3dbd6/titanic.csv"
data = str(rs.get(some_url).content, 'utf-8')
csvobject = StringIO(data)
df_test = pd.read_csv(csvobject, index_col=False,)
display(df_test)



# Time range (from - to)
dt_now     = datetime.datetime.now()
#today      = datetime.datetime.strftime(dt_now, '%Y-%m-%d')
to_date    = datetime.datetime.strftime(dt_now, '%Y-%m-%d')

yesterday  = datetime.datetime.strftime(dt_now - timedelta(1), '%Y-%m-%d')
from_date  = yesterday

print("from_date -", from_date, "| to_date -", to_date)
