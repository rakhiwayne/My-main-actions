import os
import requests
import json
print("Pipeline running successfully")
print('Inside Python Script')
api_key = os.getenv('api_key')
api_key1 = os.getenv('api_key1')
if not api_key1:
    print("no such key as api_key1")
if api_key:
    print('api_key is loaded')
    print(len(api_key))
url = os.getenv('url')
print(f"url : {url}")
api_data = requests.get(url)
print(f"status code for api hit {api_data.status_code}")
if api_data.status_code == 200:
    json_data = api_data.json()
    with open('test_data_saved/api_octocat.json', 'w') as writer:
        json.dump(json_data, writer, indent=4)
    print("file saved sucess fully at test_data_saved/api_octocat.json")
else:
    print(f'API hit failed for {url}')
