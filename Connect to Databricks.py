import requests
import json

HOST = 'https://adb-123123.15.azuredatabricks.net'
TOKEN = '123123-2'
endpoint = f'{HOST}/api/2.0/sql/queries'

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

# data = {
#     "query": "SELECT 1",
#     "data_source": {
#         "catalog_name": "hive_metastore",
#         "schema_name": "default"
#     },
#     "output_format": "json"
# }

data = {
  "query": {
    "description": "Example description",
    "display_name": "Example query",
    # "parameters": [
    #   {
    #     "name": "foo",
    #     "text_value": {
    #       "value": "bar"
    #     },
    #     "title": "foo"
    #   }
    # ],
    #"parent_path": "/Workspace/Users/user@acme.com",
    "query_text": "SELECT 1",
    "run_as_mode": "OWNER",
    "tags": [
      "Tag 1"
    ]#,
   # "warehouse_id": "a7066a8ef796be84"
  }
}

response = requests.post(endpoint, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    query_result = response.json()
    print("Query executed successfully. Results:")
    print(query_result)
else:
    print(f"Failed to execute query. Status code: {response.status_code}, Message: {response.text}")

# https://docs.databricks.com/api/workspace/statementexecution/executestatement

import requests
import json

HOST = 'https://adb-123123.15.azuredatabricks.net'
TOKEN = '123-2'
endpoint = f'{HOST}/api/2.0/sql/statements/'

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

data = {
  "on_wait_timeout": "CANCEL",
  "statement": """  select * from abc.abc limit 10   """, #"SELECT * FROM range(100)",
  "wait_timeout": "30s",
  "warehouse_id": "123123"
}

response = requests.post(endpoint, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    query_result = response.json()
    print("Query executed successfully. Results:")
    print(query_result)
else:
    print(f"Failed to execute query. Status code: {response.status_code}, Message: {response.text}")


[x["name"] for x in query_result['manifest']['schema']['columns']]
query_result['result']['data_array']

import pandas as pd
test_df = pd.DataFrame(data=query_result['result']['data_array'],
                   columns=[x["name"] for x in query_result['manifest']['schema']['columns']])
test_df

