
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

