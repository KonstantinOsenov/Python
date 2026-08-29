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
