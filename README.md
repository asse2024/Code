this project is for notify yaya wallet partner when a transaction is performed to the customer #
# it created with python programming language #



*************

import requests
import json
webhook_url = 'https://webhook.site/#!/view/b60760d9-c51c-49b6-be38-6ce7f71f400c/170c0e83-a25b-45b0-9ee9-5b840d50f3fc/1'
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

***********

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






