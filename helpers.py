from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To
import os

def sendEmail(senderDict, recipientDict, subject, body):
  message = Mail(
    # from_email=Email(os.environ.get('FROM_EMAIL'), 'Bastien Winant'),
    from_email=Email(senderDict["address"], senderDict["name"]),
    to_emails=To(recipientDict["address"], recipientDict["name"]),
    subject=subject,
    html_content=f'<h1>{body}</h1>'
  )

  try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
  except Exception as e:
    print(e.message)