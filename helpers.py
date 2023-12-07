from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To
import os

def sendEmail(senderDict, recipientDict, subject, body):
  """
  Sends email to from chosen recipient to chosen recipient

  Arguments:
  senderDict (dict): must 'name' and 'address' keys
  recipientDict (dict): must 'name' and 'address' keys
  subject (str): email subject text
  body (str): email body text
  """
  message = Mail(
    from_email=Email(senderDict["address"], senderDict.get("name")),
    to_emails=To(recipientDict["address"], recipientDict.get("name")),
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