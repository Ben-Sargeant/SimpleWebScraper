import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import csv
# import requests

load_dotenv()

base_url = "https://www.argos.co.uk"
urls = ['https://www.argos.co.uk/product/3156700','https://www.argos.co.uk/product/2699749']

# def send_text(url, nickname, location):
#  send text messages

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
        # pass it to the send text
        # send_text(row[0], row[1], row[2])
      else:
        print(f"{row[1]} is not in stock!")

searches()

