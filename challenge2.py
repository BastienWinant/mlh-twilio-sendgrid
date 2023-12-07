from helpers import sendTextEmail
import os

sender = {
  "name": "Bastien Winant",
  "address": os.environ.get('FROM_EMAIL')
  }

recipient = {
  "address": os.environ.get('TO_EMAIL')
  }

emailData = {
  "subject": "Twilio Challenge 2",
  "title": "Hello World",
  "body": "This email was sent via the SendGrid API"
}

sendTextEmail(emailData)