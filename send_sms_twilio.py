from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC719cfa8f490e643031874aa2c9040f85"
# Your Auth Token from twilio.com/console
auth_token  = "fce4f704cd8b233648d04c4210eb0f81"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5541984604949", 
    from_="+13135645130",
    body="Hello from Python!")

print(message.sid)
