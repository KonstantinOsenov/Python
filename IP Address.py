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
