from flask import Flask, request, make_response
import plivo
from plivo import plivoxml

app = Flask(__name__)

@app.route("/speak/", methods=["GET", "POST"])
def validate_signature():
   auth_token = "<auth_token>"
   signature = request.headers.get("X-Plivo-Signature-V3")
   nonce = request.headers.get("X-Plivo-Signature-V3-Nonce")
   webhook_url = request.url
   http_method = request.method

   if http_method == "GET":
       valid_signature = plivo.utils.validate_v3_signature(
           http_method, webhook_url, nonce, auth_token, signature
       )
   elif http_method == "POST":
       params = request.form.to_dict()
       valid_signature = plivo.utils.validate_v3_signature(
           http_method, webhook_url, nonce, auth_token, signature, params
       )
   else:
       return "Method not allowed", 405

   print(f"Your webhook authentication is {valid_signature}")

   # Return an XML answer to Plivo if the signature is valid

   if valid_signature == True:
       xml = plivoxml.ResponseElement()
       speak_params = {"loop": "3"}
       xml.add(plivoxml.SpeakElement("Hello, from Plivo", **speak_params))
       response = make_response(xml.to_string())
       response.headers["Content-type"] = "text/xml"
       print("Send XML to Plivo server")
       print(xml.to_string())
       return response, 200
   else:
       return "Bad request", 400


if __name__ == "__main__":
   app.run(host="127.0.0.1", debug=True)
