# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To

message = Mail(
    from_email=Email(os.environ.get('FROM_EMAIL'), "Bastien Winant"),
    to_emails=To(os.environ.get('TO_EMAIL')),
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<h1>Hello World</h1><h2>I\'m using Twilio Sendgrid</h2>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)