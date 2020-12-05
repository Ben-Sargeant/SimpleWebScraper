from selenium import webdriver
from dotenv import load_dotenv
from twilio.rest import Client
import os
import time
import csv

load_dotenv()

base_url = "https://www.argos.co.uk"

def send_text(url, nickname, location):
  account_sid = os.environ['TWILIO_SID_KEY']
  auth_token = os.environ.get('TWILIO_API_KEY')
  client = Client(account_sid, auth_token)

  message = client.messages \
                  .create(
                       body=f"The {nickname} you want is in stock at {location}! Click the link below to order now! {url}",
                       from_='+19382018827',
                       to='+447429924911'
                   )

def searches():
  driver = webdriver.Chrome()
  driver.get(base_url)
  driver.find_element_by_id('consent_prompt_submit').click()

  with open('items.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
      driver.get(row[0])
      time.sleep(1)
      driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[3]/div[1]/section[2]/section/div[10]/div/form/div/input').send_keys(f'{row[2]}')
      driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[3]/div[1]/section[2]/section/div[10]/div/form/div/button').submit()
      time.sleep(1)
      status = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[3]/div[1]/section[2]/section/div[10]/div[2]/div/div/div[1]/div/div[2]/div[3]/div/div/ol/li[1]/button/div/div/p')
      if status.get_attribute('innerHTML') != "Not in stock here":
        print(f"{row[1]} is in stock!")
        # send_text(row[0], row[1], row[2])
      else:
        print(f"{row[1]} is not in stock!")

searches()

