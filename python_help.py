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
