from random import choice, randint
import os
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'


def get_mars_photo(sol, api_key='NASA_API_KEY'):
  params = {'sol': sol, 'api_key': os.environ.get(api_key)}
  response = requests.get(rover_url, params).json()
  photos = response['photos']
  
  return choice(photos)['img_src']


def send_mars_email(from_email, to_email, img_url):
  sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

  message = Mail(
      from_email=from_email,
      to_emails=to_email,
      subject='Here is your Mars Rover picture',
      html_content='<strong>Check out this Mars pic</strong><br>'
                    f'<img src="{img_url}"></img>')

  response = sg.send(message)
  print(response.status_code, response.body, response.headers)

if __name__=="__main__":
  to_email = os.environ.get('FROM_EMAIL')
  from_email = os.environ.get('TO_EMAIL')
  image_url = get_mars_photo(randint(0,1000))
  print(to_email)
  print(from_email)
  print(image_url)
  send_mars_email(from_email=from_email, to_email=to_email, img_url=image_url)