
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

###### JSON as input

def get_item_price(shipping_str):
    shipping_json = json.loads(shipping_str)
    sku_cnt = len(shipping_json['sku'])
    gross_price = 0
    for sku in range(sku_cnt):
        sku_price = shipping_json['sku'][sku]['sku_price']
        sku_qty = shipping_json['sku'][sku]['sku_qty']
        gross_price += sku_price * sku_qty
    return round(gross_price, 2)

def get_item_qty(shipping_str):
    shipping_json = json.loads(shipping_str)
    sku_cnt = len(shipping_json['sku'])
    items_cnt = 0
    for sku in range(sku_cnt):
        sku_qty = shipping_json['sku'][sku]['sku_qty']
        items_cnt += sku_qty
    return items_cnt

def get_city(shipping_str):
    shipping_json = json.loads(shipping_str)
    return shipping_json['ship_city']



def split_zip(full_zip):
    if "-" in full_zip:
        short_zip = full_zip.split("-")[0]
    else:
        short_zip = full_zip
    return short_zip

def split_name(name, part):
    if "," in name and name is not None:
        tmp = name.split(',')
        
        first_name = tmp[1].strip()
        if first_name == "(Empty)":
            first_name = ''
        
        last_name = tmp[0].strip()
        if last_name == "(Empty)":
            last_name = ''
    else:
        first_name = ''
        last_name = ''
        
    if part == 'First name':
        output = first_name
    elif part == 'Last name':
        output = last_name
    else:
        output = 'Error'
    return output
	
