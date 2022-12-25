from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

verified_number = os.getenv("PHONE_NUMBER")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
verify_sid = os.getenv("VERIFY_SID")
client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to="+233501314009", channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)

