import requests
import os
import random
import json

import base64
import os
from helpers import sendImageEmail


def sendAPIRequest():
  payload = {
    'api_key': os.environ.get('NASA_API_KEY'), # get NASA API key 
    'sol': random.randint(0, 1000) # generate random number for Martian sol
    }

  try:
    url ="https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    r = requests.get(url, params=payload)
    r.raise_for_status()

    return json.loads(r.text)
  except requests.exceptions.HTTPError as errh: 
    print("HTTP Error") 
    print(errh.args[0]) 

def selectRandomPhoto():
  photoData = sendAPIRequest()

  try:
    photo = random.choice(photoData["photos"])
    return photo
  except ValueError as e:
    print(e) 
  except KeyError as e:
    print(e)
  except IndexError as e:
    print("Could not get a photo URL")
    print("Photos in the supplied data: ", len(photoData["photos"]))

def formatPhotodData(photoData):
  print(photoData)
  imgURL = photoData["img_src"]
  imgDate = photoData["earth_date"]
  roverName = photoData["rover"]["name"]

  return imgURL, imgDate, roverName


if __name__=="__main__":
  imgData = selectRandomPhoto()
  imgSrc, imgDate, roverName = formatPhotodData(imgData)

  emailData = {
    "title": "Here is your Mars Rover picture",
    "img_src": imgSrc,
    "img_caption": f"This photo was taken by rover {roverName} on {imgDate}"
    }

  sendImageEmail(emailData)