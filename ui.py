import csv

def menu():
  print("-------------------------------------")
  print("1. Add an item")
  print("2. Remove an item")
  print("3. Update an item")
  print("4. View your items")
  print("or type Exit to close.")
  print("-------------------------------------")

def add_item():
  url = input("Please paste the url here: ")
  nickname = input("Enter a name for this item: ")
  location = input("Finally, where would you like to collect from? ")

  row = [url, nickname, location]

  with open('items.csv', 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(row)

  print("Item added!")


def remove_item():
  selection = input("What item would you like to delete? Enter the name: ").lower()
  updated_list = []
  with open('items.csv') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        if row[1] != selection:
          updated_list.append(row)

  with open("items.csv","w",newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(updated_list)
    print("File has been updated")


def update_item():
  selection = input("Enter the Name, Location or URL you would like to update: ").lower()
  updated_info = input("What would you like to update that to? ").lower()
  items = []
  with open('items.csv') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        if selection not in row:
          items.append(row)
        else:
          new_item = []
          for detail in row:
            if detail == selection:
              new_item.append(detail.replace(selection, updated_info))
            else:
              new_item.append(detail)
          items.append(new_item)

  with open("items.csv","w",newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(items)
    print("File has been updated")

def show_items():
  print("Currently Tracked Items: ")
  with open('items.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      print(f'Name: {row[1].capitalize()} | Location: {row[2].capitalize()} | URL: {row[0]}')



active = True

print("Welcome to the Argos webscraper! Here you can add, remove, view or update your items that are being tracked.")

menu()

while active:

  user_input = input().lower()

  if user_input == "exit":
    print("Goodbye!")
    active = False
  elif user_input == "1" or user_input == "add":
    add_item()
    menu()
  elif user_input == "2" or user_input == "remove":
    remove_item()
    menu()
  elif user_input == "3" or user_input == "update":
    show_items()
    update_item()
    menu()
  elif user_input == "4" or user_input == "view":
    show_items()
    menu()
  else:
    print("Invalid option")
