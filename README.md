
***Partner Nofication Project***

     * The ability of independent online systems to communicate with one 
       another and share transaction data to the customer
       
     * this sample project is used notify (emailing service) of yaya platform to the partner on the charge of the transaction  
       
     * This provides a way for one system (the source) to "speak" (HTTP request) to customer url (the destination) when an event occurs, and share information (request payload) about 
       the event that occurred.
    
     * this project is  to notify customer for the transaction to be perform
  
     * It created with python programming languagege and import flask and requests
     
   
     * The project is two python class server and webhook it notify the transaction detail to the partner from the server 
     
     * it tested to local machine (http:\\127.0.0.1:5000\webhook) and to the https:\\webhook.site with json format.
       
****Requests****

     this project is used webhook is an HTTP and HTTPS request, triggered by an event in a payement notfication system and sent to a destination system URL 
    
****JSON****

     for sending content type file format 

***Post Method***
      
      POST method webhook in the project body to handle the request of the transaction
     

***test result in [https://webhook.site](https://webhook.site/#!/view/b60760d9-c51c-49b6-be38-6ce7f71f400c/170c0e83-a25b-45b0-9ee9-5b840d50f3fc/1) Raw Content***

{

    "id": "1dd2854e-3a79-4548-ae36-97e4a18ebf81",
     
      "amount": 100,
     
      "currency": "ETB",
  
      "created_at_time": 1673381836,
  
      "timestamp": 1701272333,
  
      "cause": "Testing",
  
      "full_name": "Abebe Kebede",
  
      "account_name": "abebekebede1",
  
      "invoice_url": "https://yayawallet.com/en/invoice/xxxx"
  
}

***test result in http://127.0.0.1:5000/webhook/***

***Step 1*** 

     ***run webhook.py****+
      
    from flask import Flask,request,abort, app
    app = Flask(__name__)
    @app.route('/webhook', methods =['POST'] )
    def webhook():
          if request.method == 'POST':
              print (request.json);
              return 'success', 200
         else:
           abort(400)
    **Main Method*
    if __name__:'__main__'
    app.run()

 ***Step 2***
 
    Result To the Partner 
    
    ****Run server.py***

    import requests
    import json
    webhook_url = 'http://172.0.0.1:5000/webhook'
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

     **********Result********
      WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
      * Running on http://127.0.0.1:5000
      Press CTRL+C to quit
      {'id': '1dd2854e-3a79-4548-ae36-97e4a18ebf81', 'amount': 100, 'currency': 'ETB', 'created_at_time': 1673381836, 'timestamp': 1701272333, 'cause': 'Testing', 'full_name':{'id': 
      '1dd2854e-3a79-4548-ae36-97e4a18ebf81', 'amount': 100, 'currency': 'ETB', 'created_at_time': 1673381836, 'timestamp': 1701272333, 'cause': 'Testing', 'full_name':
      'Abebe Kebede', 'account_name': 'abebekebede1', 'invoice_url': 'https://yayawallet.com/en/invoice/xxxx'}
      127.0.0.1 - - [08/Feb/2024 15:03:55] "POST /webhook HTTP/1.1" 200 -

****Signature Create for secured the webhook****
****Plivo Signature****

      the request that will create for webhook that can manage the http by authentication 
      of the customer to heck the tansaction and to 
      give permission

           from http.server import BaseHTTPRequestHandler, HTTPServer
           import square
           from square.utilities.webhooks_helper import is_valid_webhook_event_signature

         # The URL where event notifications are sent.
         NOTIFICATION_URL = 'https://yayawallet.com/webhook'

          # The signature key defined for the subscription.
         SIGNATURE_KEY = 'asdf1234'

          class MainHandler(BaseHTTPRequestHandler):
          def do_POST(self):
          length = int(self.headers.get('content-length', 0))
          body = self.rfile.read(length).decode('utf-8')
          square_signature = self.headers.get('x-square-hmacsha256-signature')

          is_from_square = is_valid_webhook_event_signature(body,
                                                          square_signature,
                                                          SIGNATURE_KEY,
                                                          NOTIFICATION_URL)

           if is_from_square:
            # Signature is valid. Return 200 OK.
            self.send_response(200)
            print("Request body: {}".format(body))
         else:
              # Signature is invalid. Return 403 Forbidden.
               self.send_response(403)

            self.end_headers()

        # Start a simple server for local testing.
        # Different frameworks may provide the raw request body in other ways.
        # INSTRUCTIONS
        # 1. Run the server:
        # python server.py
        # 2. Send the following request from a separate terminal:
        #    curl -vX POST localhost:8000 -d  -H "X-Square-HmacSha256-Signature: 2kRE5qRU2tR+tBGlDwMEw2avJ7QM4ikPYD/PJ3bd9Og="
        server = HTTPServer(("127.0.0.1", 5000), MainHandler)
        server.serve_forever()

