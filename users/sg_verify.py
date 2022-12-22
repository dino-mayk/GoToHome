import os
from os.path import dirname, join

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# dotenv_path = join(dirname(__file__), '.env')
dotenv_path = join(dirname(__file__), 'dev.env')
load_dotenv(dotenv_path)

FROM_EMAIL = os.environ.get('FROM_EMAIL')
TO_EMAILS = os.environ.get('TO_EMAILS')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

message = Mail(
    from_email=FROM_EMAIL,
    to_emails=TO_EMAILS,
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>',
)
try:
    sg = SendGridAPIClient(
        SENDGRID_API_KEY,
    )
    response = sg.send(message)
except Exception as e:
    print(e.message)
