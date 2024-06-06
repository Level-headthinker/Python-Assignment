#  Dictionaries
# my_dic = {'name':'rimsha','Phon_no':'081765373','email':'rimshaqasim@gmail.com'}
# print(my_dic)

# list
# my_list = ['rimsha' , '074756434738', 'rimshaqasim@gmail.com' ]
# print(my_list)

# user input
# user_input = input("Enter your name")

# file handling 
# file_handling = open("file.txt")

# basic function
# def userName():
#     print("Hello, my name is Rimsha Qasim")
# userName()    

contactList = []

def add_contact():
    name = input("Enter your name: ")   
    phone_no = input("Enter your phone number: ") 
    email = input("Enter your email: ")
    cont_dic = {
        'name': name,
        'phone_no': phone_no,
        'email': email
    }
    contactList.append(cont_dic)
    print(contactList)
def search_contact():
    name = input("Name of the user: ")
    for contact in contactList:
        if contact['name'] == name:
            print("your contact reults is",contact)
    print("Contact not found.")  
      
def delete_contact():
    print("delete contact details") 
    email = input("Enter email for delete contact details")
    for contact in contactList:
        if contact["email"] == email:
            contactList.remove(contact)
            print("delete contact of this email",email)
    print("Contact not found.")    
                          
while True:
    take_input = input("Enter 1 to add contact, 2 to search, 3 to delete, or 4 to exit: ")   
    if take_input == 1 :
        add_contact()
    elif take_input == 2:
        search_contact()
    elif take_input == 3:
        delete_contact()
    elif take_input == 4:
        print("exiting...")
        break
    else :
        print("invalid input please try again")                     