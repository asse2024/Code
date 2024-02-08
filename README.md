# Code
#  Server Send This data amount history to the partner it is done with python i test with local pc #

server.py

import requests
import json
webhook_url = "https://127.0.0.1/5000/webhook"
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

webhook.py

# import flask to create the connection between the partner site which created with POST #

from flask import Flask,request,abort, app
app = Flask(__name__)
@app.route('/webhook', methods =['POST'] )
def webhook():
    if request.method == 'POST':
        print (request.json);
        return 'success', 200
    else:
           abort(400)

if __name__:'__name__'
app.run()
