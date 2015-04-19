# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Get these credentials from http://twilio.com/user/account
account_sid = "AC458154d1e86d0826b01386a4c03765e1"
auth_token = "eda2f0c7f414b7994e4bf355d44bb88b"
client = TwilioRestClient(account_sid, auth_token)
 
# Make the call
call = client.calls.create(to="+19734760072",  # Any phone number
                           from_="+18625794183", # Must be a valid Twilio number
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print call.sid
