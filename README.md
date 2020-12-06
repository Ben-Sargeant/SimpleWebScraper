Simple Python Webscraper

This is a simple webscraper I have built to practice Python. It is designed so I can set up a CRON job to check the availability of an item (for example, everyday).
If it is available, I will receive an SMS to my mobile letting me know.

There are two scripts, the first (webscraper.py) performs the searches and issues the SMS. The second runs a simple UI allowing me to perform all CRUD operations of the items I am tracking.

The text messages are sent through a Twilio trial account and display as below:
