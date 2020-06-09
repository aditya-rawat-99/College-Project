# from flask import Flask, request, redirect
# from twilio.twiml.messaging_response import MessagingResponse
#
# app = Flask(__name__)
#
# @app.route("/sms", methods=["GET","POST"])
# def sms_reply():
#     resp = MessagingResponse()
#
#     resp.message("Okay")
#
#     return str(resp)
#
# if __name__ == "__main__":
#     app.run(debug=True)

from twilio.rest import Client

account_sid = "AC075fd754e468c96127a52c1f5c5486ea"
auth_token = "c9569292d76ee8c8f6896207b2b33e88"

from_whatsapp_number = "whatsapp:+14155238886"
to_whatsapp_number = "whatsapp:+918826332442"

client = Client(account_sid,auth_token)
client.messages.create(to=to_whatsapp_number,
                       from_=from_whatsapp_number,
                       body="message")
