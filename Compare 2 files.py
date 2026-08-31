## there are 2 files in the directory and you don't really know what is inside etc.
## 1. Only two csv files in the directory (not relevant if I find a way to choose files)
## 2. column names must be the same

# 1
import pandas as pd
from os import listdir
import csv

# 2
def read_csv_file(file_name):
    with open(file_name, 'r') as csvfile:
        delimiter = csv.Sniffer().sniff(csvfile.read(5000)).delimiter
        file_df = pd.read_csv(file_name, sep=delimiter)
        file_columns = list(file_df.columns)
    csvfile.close()
    return file_df, file_columns


# 3
# Get file names
files_list = list()
files_list_tmp = listdir()
for file in files_list_tmp:
    if file.endswith(".csv"):
        files_list.append(file)

# 4
# Read files and choose only common columns
file_1_df, file_1_columns = read_csv_file(files_list[0])
file_2_df, file_2_columns = read_csv_file(files_list[1])
common_columns = list(set(file_1_columns).intersection(file_2_columns))
file_1_df = file_1_df[common_columns]
file_2_df = file_2_df[common_columns]
file_1_df['file_1'] = 'file_1'
file_2_df['file_2'] = 'file_2'


# 5
# Get missing rows in the second file
missing_rows_in_file2 = pd.merge(
    file_1_df, 
    file_2_df,
    how = 'left',
    on = common_columns)
missing_rows_in_file2 = missing_rows_in_file2[missing_rows_in_file2['file_2'].isnull()][common_columns]
final_file_name = f"{len(missing_rows_in_file2)} rows are missing in the file '{files_list[1]}'"
missing_rows_in_file2.to_excel(final_file_name + '.xlsx', index=False)

# 6
# Get missing rows in the first file
missing_rows_in_file1 = pd.merge(
    file_1_df, 
    file_2_df,
    how = 'right',
    on = common_columns)
missing_rows_in_file1 = missing_rows_in_file1[missing_rows_in_file1['file_1'].isnull()][common_columns]
final_file_name = f"{len(missing_rows_in_file1)} rows are missing in the file '{files_list[0]}'"
missing_rows_in_file1.to_excel(final_file_name + '.xlsx', index=False)
