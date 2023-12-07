from helpers import sendEmail
import os

sender = {
  "name": "Bastien Winant",
  "address": os.environ.get('FROM_EMAIL')
  }

recipient = {
  "address": os.environ.get('TO_EMAIL')
  }

subject = 'Sending this Twilio SendGrid is Fun'
body = "Hello World"

sendEmail(sender, recipient, subject, body)