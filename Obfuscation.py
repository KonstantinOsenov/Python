import random

def real_part_phone_number(phone):
    try:
        if len(phone) < 8:
            return ''
        new_phone = phone[:-7]
        return new_phone
    except:
        pass
    
def get_tobe_masked_part_phone_number(phone):
    try:
        if len(phone) < 8:
            return ''
        new_phone = phone[-7:]
        return new_phone
    except:
        pass
        
def get_random_list(input_list, len_of_values):
    len_input_list = len(input_list)
    if len_of_values == 1:
        new_list = random.sample(range(10**(len_of_values - 1) - 1, 10**(len_of_values)), len_input_list)
    else:
        new_list = random.sample(range(10**(len_of_values - 1), 10**(len_of_values)), len_input_list)
    new_list_str = list(map(str, new_list))
    return new_list_str

def create_dict_encr(df_name, column_name):
    try:
        dict_with_codes = dict()
        
        tmp_df = df_name.copy()
        tmp_df['attr_len'] = tmp_df.apply(lambda x: len(x[column_name]), axis=1)
        column_lengths_of_values_list = list(pd.unique(tmp_df['attr_len']))
        
        for l in column_lengths_of_values_list:
            if l > 0:
                #print(l)
                list_of_values = list(pd.unique(tmp_df[column_name][tmp_df['attr_len']==l]))
                list_of_new_values = get_random_list(list_of_values, l)
                #print(list_of_values)
                #print(list_of_new_values)
            
                zip_lists = zip(list_of_values, list_of_new_values)
                for x in zip_lists:
                    dict_with_codes[x[0]] = x[1]
            else:
                print('len = 0')
            
        return dict_with_codes
    except:
        print('error')
        
def simple_func(some_value, input_dict):
    try:
        out_value = input_dict[some_value]
        return out_value
    except:
        return ''

print(real_part_phone_number('1234567890'))
print(random_number_gen_same_length(99))
print(get_random_list(['3199967', '8085787', '8204710'], 7))

letters_numbers = string.ascii_uppercase + string.digits

def create_random_string(s):
    len_s = len(s)
    masked_s = ''.join(random.choice(letters_numbers) for i in range(len_s))
    return masked_s

def get_random_list_of_strings(list_s):
    out_list = [create_random_string(s) for s in list_s]
    return out_list

def create_dict_encr_string(df_name, column_name):
    try:
        dict_with_codes = dict()
        
        tmp_df = df_name.copy()
        list_of_values = list(pd.unique(tmp_df[column_name]))
        list_of_new_values = get_random_list_of_strings(list_of_values)
        
        zip_lists = zip(list_of_values, list_of_new_values)
        for x in zip_lists:
            dict_with_codes[x[0]] = x[1]
            
        return dict_with_codes
    except:
        print('error')

# additional attributes
customer_df_masked = customer_df.copy()
#customer_df_masked['phone_len'] = customer_df.apply(lambda x: len(x['Phone Number']), axis=1)
customer_df_masked['real_part_phone_number'] = \
                customer_df_masked.apply(lambda x: get_real_part_phone_number(x['Phone Number']), axis=1)
customer_df_masked['tobe_masked_part_phone_number'] = \
                customer_df_masked.apply(lambda x: get_tobe_masked_part_phone_number(x['Phone Number']), axis=1)
customer_df_masked['email_1part'] = customer_df.apply(lambda x: x['Email'].split("@")[0], axis=1)
customer_df_masked['email_2part'] = customer_df.apply(lambda x: x['Email'].split("@")[1], axis=1)
customer_df_masked['last_name'] = customer_df_masked.apply(lambda x: x['Customer Name'].split(',')[0], axis=1)
customer_df_masked['first_name'] = customer_df_masked.apply(lambda x: x['Customer Name'].split(',')[1].strip(), axis=1)
customer_df_masked['bp_id_to_mask'] = customer_df_masked['business_partner_no'].astype('string')
customer_df_masked

customer_df_masked = customer_df.copy()
#customer_df_masked['phone_len'] = customer_df.apply(lambda x: len(x['Phone Number']), axis=1)
customer_df_masked['real_part_phone_number'] = customer_df.apply(lambda x: real_part_phone_number(x['Phone Number']), axis=1)
customer_df_masked['tobe_masked_part_phone_number'] = customer_df.apply(lambda x: tobe_masked_part_phone_number(x['Phone Number']), axis=1)
##customer_df_masked['email_1part'] = customer_df.apply(lambda x: x['Email'].split("@")[0], axis=1)
#customer_df_masked['email_1part_len'] = customer_df.apply(lambda x: len(x['email_1part']), axis=1)
#customer_df_masked['email_2part'] = customer_df.apply(lambda x: x['Email'].split("@")[1], axis=1)
customer_df_masked


# email
dict_email = create_dict_encr_string(customer_df_masked, 'email_1part')

# save dict (for decrypt)
with open('dict_email.txt', 'w') as file:
    file.write(json.dumps(dict_email))
file.close()

# read dict
#with open('dict_email.txt', 'r') as file:
#    dict_email_from_file = json.loads(file.read()) 
#file.close() 

customer_df_masked['masked_email_1part'] = customer_df_masked.apply\
            (lambda x: simple_func(x['email_1part'], dict_email), axis=1)
customer_df_masked['masked_email'] = \
            customer_df_masked['masked_email_1part'] + '@' + customer_df_masked['email_2part']
customer_df_masked[['Email', 'masked_email', 'email_1part', 'email_2part', 'masked_email_1part']]

# phone
#create_dict_encr(customer_df_to_test, 'phone')
dict_phone = create_dict_encr(customer_df_masked, 'tobe_masked_part_phone_number')

# save dict (for decrypt)
with open('dict_phone.txt', 'w') as file:
    file.write(json.dumps(dict_phone))
file.close()

# read dict
with open('dict_phone.txt', 'r') as file:
    dict_phone_from_file = json.loads(file.read()) 
file.close() 

customer_df_masked['masked_part_phone_number'] = customer_df_masked.apply\
            (lambda x: simple_func(x['tobe_masked_part_phone_number'], dict_phone), axis=1)
customer_df_masked['masked_phone'] = \
            customer_df_masked['real_part_phone_number'] + customer_df_masked['masked_part_phone_number']
customer_df_masked.sort_values('tobe_masked_part_phone_number')

# IP masking

orders_df_masked = orders_df.copy()
orders_df_masked['IP_1_part'] = orders_df_masked.apply(lambda x: x['ip_address_clc2'].split('.')[0], axis=1)
orders_df_masked['IP_2_part'] = orders_df_masked.apply(lambda x: x['ip_address_clc2'].split('.')[1], axis=1)
orders_df_masked['IP_3_part'] = orders_df_masked.apply(lambda x: x['ip_address_clc2'].split('.')[2], axis=1)
orders_df_masked['IP_4_part'] = orders_df_masked.apply(lambda x: x['ip_address_clc2'].split('.')[3], axis=1)
orders_df_masked

#create_dict_encr(customer_df_to_test, 'phone')
dict_ip_3_part = create_dict_encr(orders_df_masked, 'IP_3_part')
dict_ip_4_part = create_dict_encr(orders_df_masked, 'IP_4_part')

# save dict (for decrypt)
with open('dict_ip_3_part.txt', 'w') as file:
    file.write(json.dumps(dict_ip_3_part))
file.close()

# read dict
with open('dict_ip_3_part.txt', 'r') as file:
    dict_ip_3_part_from_file = json.loads(file.read()) 
file.close() 

# save dict (for decrypt)
with open('dict_ip_4_part.txt', 'w') as file:
    file.write(json.dumps(dict_ip_4_part))
file.close()

# read dict
with open('dict_ip_4_part.txt', 'r') as file:
    dict_ip_4_part_from_file = json.loads(file.read()) 
file.close() 

orders_df_masked['masked_IP_3_part'] = orders_df_masked.apply(lambda x: simple_func(x['IP_3_part'], dict_ip_3_part), axis=1)
orders_df_masked['masked_IP_4_part'] = orders_df_masked.apply(lambda x: simple_func(x['IP_4_part'], dict_ip_4_part), axis=1)
orders_df_masked

orders_df_masked['masked_ip'] = orders_df_masked.apply(lambda x: '.'.join((
    x['IP_1_part'],
    x['IP_2_part'],
    x['masked_IP_3_part'],
    x['masked_IP_4_part'])), axis=1)
orders_df_masked

