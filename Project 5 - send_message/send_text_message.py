"""
This program allows the user to send a message
to his phone through twilio API.
The user needs to have an account on twilio and a twilion phone number.

Download the twilio-python library from http://twilio.com/docs/libraries

"""


from twilio.rest import TwilioRestClient
 
your_phone_number = "+2126xxxxxxxx"
twilio_number = "+123XXXXXXXXXX"

# Find these values at https://twilio.com/user/account

account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
client = TwilioRestClient(account_sid, auth_token)
 
# send the message 
message = client.messages.create(to=your_phone_number, from_= twilio_number,
                                     body="Hello, A meesage sent from Twilio!")

print(message.sid)