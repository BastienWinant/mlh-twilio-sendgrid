# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='bastien.winant@mail.mcgill.ca',
    to_emails='bastien.winant@gmail.com',
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