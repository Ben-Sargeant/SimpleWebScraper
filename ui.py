import csv

active = 1

print("Welcome to the Argos webscraper! Here you can add, remove, view or update your items that are being tracked.")


def add_item():
#url, nickname, location
  print("Please paste the url here: ")
  url = input()
  print("Enter a name for this item: ")
  nickname = input()
  print("Finally, where would you like to collect from?")
  location = input()

  row = [url, nickname, location]

  with open('items.csv', 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row)

  #display list?


def remove_item():



while active:
  print("1. Add an item")
  print("2. Remove an item")
  print("3. Update an item")
  print("4. View your items")
  print("or type Exit to close.")

  user_input = input().lower()

  print(user_input)

  if user_input == "exit":
    print("Goodbye!")
    active = 0
  else:
    if user_input == "1" or "add":
      add_item()
    if user_input == "2" or "remove":
      remove_item()
    # if user_input == "3" or "update":
    #   update_item()
    # if user_input == "4" or "view":
    #   view_items()
