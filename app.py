import os
print("Pipeline running successfully")
print('Inside Python Script')
api_key = os.getenv('api_key')
api_key1 = os.getenv('api_key1')
if not api_key1:
    print("no such key as api_key1")
if api_key:
    print('api_key is loaded')
    print(len(api_key))