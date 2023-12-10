import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(from_email, to_email):
  sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

  message = Mail(
    from_email=from_email,
    to_emails=to_email,
    subject='Here is your Twilio Sendgrid Email',
    html_content='<h1>Hello World</h1>')
  
  response = sg.send(message)
  print(response.status_code, response.body, response.headers)

if __name__=="__main__":
  to_email = os.environ.get('TO_EMAIL')
  from_email = os.environ.get('FROM_EMAIL')

  send_email(from_email=from_email, to_email=to_email)