import requests

# Get request (REST)
# parameters
api_url = 'http://api.openweathermap.org/data/2.5/weather'
api_params = {
    'q': 'Stockholm', 
    'appid': 'c39ff7a666bd95bd32e98b01ba5f4db1',
    'units': 'metric'
}

# send request and get response
response = requests.get(url=api_url, params=api_params)

# status of request/response
print(f'response code is {response.status_code}', end='\n\n')
temperature = response.json()['main']['temp']

# data from response
print(f'temperature is {temperature} degree', end='\n\n')
print('full response:')
response.json()


# 1 row
response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=stockholm&appid=c39ff7a666bd95bd32e98b01ba5f4db1&units=metric')
response.json()


############# Azure App Insights logs
# ID and KEY for INSIGHTS FRE
appId = ""      #enter APP ID here
appKey = "" #enter APIKEY for that same app here

kql_query = """ ..... """
params = {"query": kql_query}
headers = {'X-Api-Key': appKey}
url = f'https://api.applicationinsights.io/v1/apps/{appId}/query'

# send request, get response
response = requests.get(url, headers=headers, params=params, verify=False).json()

logs_df = pd.DataFrame(
    data = response['tables'][0]['rows'],
    columns = list(map(lambda x: x['name'], response['tables'][0]['columns']))
).drop_duplicates()
logs_df
