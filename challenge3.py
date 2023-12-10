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

  try:
    img = choice(photos)
    img_url = img['img_src']
    img_date=img['earth_date']
    img_rover=img['rover']['name']
    return img_url, img_date, img_rover
  except IndexError:
    return


def send_mars_email(from_email, to_email, img_data):
  sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

  message = Mail(
      from_email=from_email,
      to_emails=to_email,
      subject='Here is your Mars Rover picture',
      html_content=f"""
        <h1>Check out this Mars pic</h1>
        <figure style='margin: 0'>
          <img src='{img_data["url"]}' style='width: 400px; height: auto;' />
          <figcaption>Photo taken by {img_data["rover"]} on {img_data["date"]}</figcaption>
        </figure>
      """)

  response = sg.send(message)
  print(response.status_code, response.body, response.headers)

if __name__=="__main__":
  to_email = os.environ.get('TO_EMAIL')
  from_email = os.environ.get('FROM_EMAIL')

  try:
    img_url, img_date, img_rover = get_mars_photo(randint(0,1000))
    img_data = {
      "url": img_url,
      "date": img_date,
      "rover": img_rover
    }

    send_mars_email(from_email=from_email, to_email=to_email, img_data=img_data)
  except TypeError:
    print("Could not retrieve NASA picture.")