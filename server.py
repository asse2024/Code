import requests
import json
webhook_url = 'https://github.com/asse2024/Code/blob/main/Server'
data = {'id': '1dd2854e-3a79-4548-ae36-97e4a18ebf81',
  'amount': 100,
  'currency': 'ETB',
  'created_at_time': 1673381836,
  'timestamp': 1701272333,
  'cause': 'Testing',
  'full_name': 'Abebe Kebede',
  'account_name': 'abebekebede1',
  'invoice_url': 'https://yayawallet.com/en/invoice/xxxx'}
r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type':'application/json'})
