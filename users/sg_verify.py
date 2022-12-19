from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='Duck123321@yandex.ru',
    to_emails='Duck123321@yandex.ru',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>',
)
try:
    sg = SendGridAPIClient(
        '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'
    )
    response = sg.send(message)
except Exception as e:
    print(e.message)
