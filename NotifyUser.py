from twilio.rest import Client

def notify_user():

    account_sid = "AC075fd754e468c96127a52c1f5c5486ea"
    auth_token = "c9569292d76ee8c8f6896207b2b33e88"

    from_whatsapp_number = "whatsapp:+14155238886"
    to_whatsapp_number = "whatsapp:+918826332442"

    client = Client(account_sid, auth_token)
    client.messages.create(to=to_whatsapp_number,
                           from_=from_whatsapp_number,
                           body="Intruder Alert")

if __name__ == '__main__':
    notify_user()
