from twilio.rest import Client 
 
account_sid = 'ACd45ed68562b7fd914ad4785361c77186' 
auth_token = '94918186d8b9e10819f5e248e18b5968' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12056275172',        
                              body = "xasxs",
                              to='+528127487741' 
                          ) 
 
print(message.sid)