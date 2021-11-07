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
