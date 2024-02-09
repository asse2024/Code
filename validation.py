import hmac
from flask import Flask, request

app = Flask(__name__)


@app.route('/receive-seatable-webhook', methods=['POST'])
def receive():

    secret = 'secret'
    seatable_signature = request.headers.get('X-Seatable-Signature', '').replace('sha256=', '')

    signature = hmac.new(
        secret.encode('utf-8'), request.data, digestmod='sha256').hexdigest()

    signature_compare = hmac.compare_digest(signature, seatable_signature)

    if signature_compare:
        print(request.json)
        return 'success', 200
        # do something
  
    return {
    'success':signature_compare
    }










