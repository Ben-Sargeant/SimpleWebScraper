from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from twilio.rest import Client
import os
import time
import csv

options = Options()
options.headless = False
options.add_argument('--disable-gpu')


load_dotenv()

base_url = "https://www.argos.co.uk"

def send_text(url, nickname, location):
  account_sid = os.environ['TWILIO_SID_KEY']
  auth_token = os.environ.get('TWILIO_API_KEY')
  client = Client(account_sid, auth_token)

  message = client.messages \
                  .create(
                       body=f"The {nickname} you want is in stock at {location}! Click the link below to order now! {url}",
                       from_=os.environ.get('MY_MOBILE'),
                       to='+447429924911'
                   )

def searches():
  driver = webdriver.Chrome(options=options)
  driver.get(base_url)
  driver.find_element_by_id('consent_prompt_submit').click()

  with open('items.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
      driver.get(row[0])
      time.sleep(1)
      driver.find_element_by_name('search').send_keys(f'{row[2]}')
      driver.find_element_by_class_name('SearchStockstyles__SearchButton-sc-1olt28i-4').submit()
      time.sleep(1)
      status = driver.find_element_by_class_name('AvailabilityResultstyles__AvailabilityResultHeadingCollectTitle-sc-1vk7ryk-7')
      if status.get_attribute('innerHTML') == "Not in stock here":
        print(f"{row[1]} is not in stock!")
      else:
        print(f"{row[1]} is in stock!")
        send_text(row[0], row[1], row[2])

searches()

