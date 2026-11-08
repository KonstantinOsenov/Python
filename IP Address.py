import urllib

GEO_IP_API_URL  = 'http://ip-api.com/json/'

# Can be also site URL like this : 'google.com'
IP_TO_SEARCH    = '118.70.151.42'

# Creating request object to GeoLocation API
req             = urllib.request.Request(GEO_IP_API_URL+IP_TO_SEARCH)
# Getting in response JSON
response        = urllib.request.urlopen(req).read()
# Loading JSON from text to object
json_response   = json.loads(response.decode('utf-8'))

# Print country
print(json_response['country'])
print(json_response)

def ipInfo(addr=''):
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    #will load the json response into data
    for attr in data.keys():
        #will print the data line by line
        print(attr,' '*13+'\t->\t',data[attr])

ipInfo('73.206.72.32')

#####################################################
#####################################################
#####################################################

### IP
import requests
import urllib.request
import json

# Country
def get_country_by_ip(ip):
    try:
        if ip in ip_cache.keys():
            #print(ip, ip_cache[ip], '- old')
            return ip_cache[ip]
        else:
            GEO_IP_API_URL  = 'http://ip-api.com/json/'
            IP_TO_SEARCH    = ip
            req             = urllib.request.Request(GEO_IP_API_URL+IP_TO_SEARCH)
            response        = urllib.request.urlopen(req).read()
            json_response   = json.loads(response.decode('utf-8'))
            ip_cache[IP_TO_SEARCH] = json_response['country']
            #print(IP_TO_SEARCH, json_response['country'], '- new')
            print(IP_TO_SEARCH, 'new')
            time.sleep(0.5)
            return json_response['country']
    except:
        print('Error, IP:', ip)
        return 'Error'

def get_country_by_ip_from_cache(ip):
    try:
         return ip_cache[ip]
    except:
        return 'Error'

# All info    
def get_all_by_ip(ip):
    try:
        if ip in json_cache.keys():
            #print(ip, ip_cache[ip], '- old')
            return json_cache[ip]
        else:
            GEO_IP_API_URL  = 'http://ip-api.com/json/'
            IP_TO_SEARCH    = ip
            req             = urllib.request.Request(GEO_IP_API_URL+IP_TO_SEARCH)
            response        = urllib.request.urlopen(req).read()
            json_response   = json.loads(response.decode('utf-8'))
            json_cache[IP_TO_SEARCH] = json_response
            #print(IP_TO_SEARCH, json_response['country'], '- new')
            print(IP_TO_SEARCH, 'new')
            time.sleep(1.5)
            return json_response
    except:
        print('Error, IP:', ip)
        return 'Error'


def get_all_by_ip_from_cache(ip, parameter):
    try:
        return json_cache[ip][parameter]
    except:
        return 'Error'
		
#get_all_by_ip('71.59.218.29')


# GET COUNTRY FROM IP
# read cache
with open('ip_cache.txt', 'r') as file:
    ip_cache = json.loads(file.read()) # use `json.loads` to do the reverse 
file.close() 

#ip_list_plus_sign = [
#'107.185.45.15'
#]

n = 1500
for ip in ip_list_plus_sign[n:n+100]:
#for ip in ip_list_plus_sign:
    get_country_by_ip(ip)

# save cache
with open('ip_cache.txt', 'w') as file:
    file.write(json.dumps(ip_cache))
file.close()


# GET full info FROM IP
# read cache
with open('json_cache.txt', 'r') as file:
    json_cache = json.loads(file.read()) # use `json.loads` to do the reverse 
file.close() 

#ip_list_plus_sign = [
#'77.111.244.22', '24.16.154.181'
#]

n = 6000
for ip in ip_list_plus_sign[n:n+2000]:
#for ip in ip_list_plus_sign:
    get_all_by_ip(ip)

# save cache
with open('json_cache.txt', 'w') as file:
    file.write(json.dumps(json_cache))
file.close()


# open cache with IPs
with open('json_cache.txt', 'r') as file:
    json_cache = json.loads(file.read()) # use `json.loads` to do the reverse 
file.close() 

def get_all_by_ip_from_cache(ip, parameter):
    try:
        return json_cache[ip][parameter]
    except:
        return 'Error'
		
df['IP_first_two_numbers'] = df['ip_address'].apply(lambda x: x[:x.find('.', x.find('.')+1)])
df['IP_country'] = df['ip_address'].apply(lambda x: get_country_by_ip(x))
df['IP_country'] = df['ip_address'].apply(lambda x: get_country_by_ip_from_cache(x))
df['IP_country'] = df['ip_address'].apply(lambda x: get_all_by_ip_from_cache(x, 'country'))
df['IP_isp']     = df['ip_address'].apply(lambda x: get_all_by_ip_from_cache(x, 'isp'))

