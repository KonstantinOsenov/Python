#################################
## regexp
#################################
import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
x

x='hello 42 I\'m a 32 string 30'
re.sub('[^0-9]+', '', x)
>> 423230

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



# Get country id by ISO code
def get_country_id(input_country_code_string):
    
    if input_country_code_string == "All":
        output_country_id_list = [x[0] for x in df_dim_country.collect()]
        return output_country_id_list
    
    input_country_code_list_tmp = input_country_code_string.split(",") 
    input_country_code_list = [x.strip() for x in input_country_code_list_tmp]
    #print(input_country_code_list)

    output_country_id_list = [x[0] for x in df_dim_country.filter(F.col("country_code").isin(input_country_code_list)).collect()]
    #print(output_country_id_list)

    return output_country_id_list

# get_country_id("IN, US")
# get_country_id("IN")
# get_country_id("All")


# remove letters from string (keep only digits)
def get_cart(s):
    out_s = re.findall(r'\d+', s)[0]
    return out_s
#get_cart("3404427911MXMASTER")
all_cb_df['cart_id'] = all_cb_df.apply(lambda x: get_cart(x['Order ID']), axis=1)


# pandas df to list
malicious_bp_to_block_list = tmp_df.business_partner_no.values.tolist()#[:5]
malicious_bp_to_block_list


# add column with random values
import random
db_qv_exa_df_len = db_qv_exa_df.shape[0]
random_list = random.sample(range(1, db_qv_exa_df_len+1), db_qv_exa_df_len)
db_qv_exa_df['random_number'] = random_list


# windows path 
from os import listdir
from os.path import isfile, join
mypath = project_path + r"\some path\folder"
files_list = listdir(mypath)
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
files_list

