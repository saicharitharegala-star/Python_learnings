class Contact:
    phone_directory = []

    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number
        Contact.phone_directory.append(self)
    
    def show_contact(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}"
    
    @classmethod 
    def show_all_contacts(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts found in the phone book.")
        else:
            print("Phone Book Contacts:")
            for contact in cls.phone_directory:
                print(contact.show_contact())
    
    @classmethod
    def search_contact(cls, name):
        for contact in cls.phone_directory:
            if contact.name.lower() == name.lower():
                return contact.phone_number
        return "Contact not found "
    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number) > 8 and phone_number.isdigit():
            return True
        else:
            return False



n_contacts = int(input("Enter the number of contacts you want to add: "))
for i in range(n_contacts):
        name = input(f"Enter the name of the contact {i + 1}:")
        phone_number = input(f"Enter the phone number of the contact {i + 1}:")
        if Contact.validate_phone_number(phone_number):
            Contact(name, phone_number)
        else:
            print("Invalid phone number! Please enter a valid phone number with more than 8 digits.")
    
Contact.show_all_contacts()



