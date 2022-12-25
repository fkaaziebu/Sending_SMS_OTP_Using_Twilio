from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

phone_number = os.getenv("PHONE_NUMBER")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello world from twilio", from_="+233550815604", to=phone_number
)

print("SMS has been sent")
print(message)