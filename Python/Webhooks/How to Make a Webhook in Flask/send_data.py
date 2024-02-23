import requests
import json

webhook_url = "http://127.0.0.1:5000/webhook"
#webhook_url = 'https://webhook.site/22e56b28-7016-48a2-805f-0357417c89d1'

data = { 'name': 'dog',
         'Channel URL': 'test' }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
print(r)