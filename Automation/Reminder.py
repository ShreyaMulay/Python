import schedule
import time
from twilio.rest import Client

ACCOUNT_SID = 'ACaeee5d5e2850ec75b433e22120925e26'
AUTH_TOKEN = '31ee411abed6b2a04f2d5ac45adf0714'
TWILIO_PHONE_NUMBER = '9371095337'
TARGET_PHONE_NUMBER = '9371095337'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms():
    message = client.messages.create(
        body="Hello",
        from_=TWILIO_PHONE_NUMBER,
        to=TARGET_PHONE_NUMBER
    )
    print(f"Sent message with SID: {message.sid}")

def main():
     while True:
        schedule.run_pending()
        time.sleep(1)
schedule.every(1).minute.do(send_sms)

if __name__ == "__main__":
    main()
   
