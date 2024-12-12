# creating a small python address book

#Dictionary that stores Name and various info
contacts = {}

#function that add contacts
def add_contacts():
  #Nested dictionaries to take name and its various information
  key = input("Enter name for address: ")
  if key in contacts:
    print(f"{key} is already in the contact use the update function to update it")
  else:
    number = input("Enter Number: ")
    zipcode = int(input("Enter the zipcode: "))
    address = input("Enter Address: ")
    occupation = input("Enter Occupation: ")
    contacts[key] = {
      "Number" : number,
      "ZipCode" : zipcode,
      "Address" : address,
      "Occupation" : occupation    
    }
    print(" ")
    print(f"{key} has been added succesfully")

#Function that removes contact
def remove_contacts():
  key = input ("what contact name would you like to delete: ")
  if key in contacts:
    del contacts[key]
    print(f"{key} has been removed from the contact")
  else:
    print(f"{key} does not exist")


#Update contact as needed
def update_contacts():
  key = input("What name would you like to update: ")
  if key in contacts:
    print("What would you like to update?")
    print("1. Number")
    print("2. Zipcode")
    print("3. Address")
    print("4. Occupation")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        contacts[key]["Number"] = input("Enter new phone number: ")
    elif choice == "2":
        contacts[key]["Zipcode"] = input("Enter new zipcode: ")
    elif choice == "3":
        contacts[key]["Address"] = input("Enter new address: ")
    elif choice == "4":
        contacts[key]["Occupation"] = input("Enter new occupation: ")
    else:
        print("Invalid choice.")
    print(f"Contact {key} updated successfully.")
  else:
    print(f"Contact {key} does not exist. Use the add function to create it.")

#display contacts   
def display_contacts():
  key = input ("What Name would you like to display?: ")
  if len(contacts) == 0:
    print("The contact log is empty")
  elif key in contacts:
    print(contacts[key])
  else:
    print(f"{key} does not exist")

#display all contacts as needed
def display_all():
  for name, number in contacts.items():
    print (f"{name} : {number}")
  else:
    print("contact is all empty")

def main():
  while True:
    print(" ")
    print("Welcome to the address book")
    print("\nAddress Book Menu:")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Update Contact")
    print("4. Display Contact")
    print("5. Display All Contacts")
    print("6. Exit")
    choice = int(input("What would you like to do: "))
    if choice == 1:
      add_contacts()
    elif choice == 2:
      remove_contacts()
    elif choice == 3:
      update_contacts()
    elif choice == 4:
      display_contacts()
    elif choice == 5:
      display_all()
    elif choice == 6:
      print("Exiting the address book! Goodbye")
      break
    else:
      print("Invalid choice try again")

if __name__ == "__main__":
  main()