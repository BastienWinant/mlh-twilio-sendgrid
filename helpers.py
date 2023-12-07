# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail, Email, To, Attachment, FileContent, FileType, FileName, Disposition, ContentId
# import os

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To

def sendTextEmail(emailContent):
  subject = emailContent.get("subject")
  if not subject:
    subject = "No Subject"

  emailHTML = ""

  textTitle = emailContent.get("title")
  if textTitle:
    emailHTML += "<h1>"
    emailHTML += emailContent["title"]
    emailHTML += "</h1>"
  
  textBody = emailContent.get("body")
  if textBody:
    emailHTML += "<p>"
    emailHTML += emailContent["body"]
    emailHTML += "</p>"
  
  sendEmail(subject, emailHTML)

def sendImageEmail(emailContent):
  subject = emailContent.get("subject")
  if not subject:
    subject = "No Subject"
  
  emailHTML = ""

  textTitle = emailContent.get("title")
  if textTitle:
    emailHTML += "<h1>"
    emailHTML += emailContent["title"]
    emailHTML += "</h1>"
  
  imgSrc = emailContent.get("img_src")
  imgCaption = emailContent.get("img_caption")

  if imgSrc:
    emailHTML += "<figure style='margin: 0;'>"
    emailHTML += f"<img src='{imgSrc}' style='width: 400px; height: auto;' />"

    if imgCaption:
      emailHTML += f"<figcaption><i>{imgCaption}</i></figcaption>"

    emailHTML += "</figure>"
  
  sendEmail(subject, emailHTML)

def sendEmail(subject, html_body):
  """
  Sends email to from chosen recipient to chosen recipient

  Arguments:
  subject (str): email subject
  html_body (dict): dictionary containint email body elements
  """
  try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

    message = Mail(
      from_email=Email(os.environ.get('FROM_EMAIL')),
      to_emails=To(os.environ.get('TO_EMAIL')),
      subject=subject,
      html_content=html_body
    )
    
    response = sg.send(message)
    print(response.status_code, response.headers, response.body)
  except Exception as e:
    print(f"Error sending email: {e}")