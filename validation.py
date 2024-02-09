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
#    python server.py
# 2. Send the following request from a separate terminal:
#    curl -vX POST localhost:5000 -d  -H "X-Square-HmacSha256-Signature: 2kRE5qRU2tR+tBGlDwMEw2avJ7QM4ikPYD/PJ3bd9Og="
server = HTTPServer(("127.0.0.1", 8000), MainHandler)
server.serve_forever()
