import requests
import os
import random
import json

import base64
import os
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from sendgrid import SendGridAPIClient


def sendAPIRequest():
  payload = {
    'api_key': os.environ.get('NASA_API_KEY'), # get NASA API key 
    'sol': random.randint(0, 1000)
    } # generate random number for Martian sol

  try:
    url ="https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    r = requests.get(url, params=payload)
    r.raise_for_status()

    return json.loads(r.text)
  except requests.exceptions.HTTPError as errh: 
    print("HTTP Error") 
    print(errh.args[0]) 

def selectRandomPhoto(jsonData):
  try:
    photo = random.choice(jsonData["photos"])
    # photoURL = jsonData["photos"][photoID]
    return photo["img_src"]
    # print(jsonData["photos"][photoID]['img_src'])
  except ValueError as e:
    print(e) 
  except KeyError as e:
    print(e)

if __name__=="__main__":
  photoData = sendAPIRequest()
  photoURL = selectRandomPhoto(photoData)
  print(photoURL)