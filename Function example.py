
# source csv-files
common_path = r'D:\case_data_sets_excel'
customers_csv = common_path + r'\Customers.csv'
emails_csv = common_path + r'\Email Engagement.csv'
transactions_csv = common_path + r'\Transactions_mini.csv'

with open(customers_csv) as f:
    lines = f.readlines()
    
type(lines)

new_list = list(map(lambda x: x*2, lines))
new_list

