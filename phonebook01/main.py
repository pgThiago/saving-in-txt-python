''' - Creates a list and a dictionary
    - Starts a infinity loop that only breaks when the user want to
    - If txt is empty then the user only have 2 methods: Add(); Quit(that is not really a method, of course).
'''
from contact import Contact
from operator import itemgetter
from os import system
from time import sleep
list_of_contacts = []
dic = {}
print('{:^145}'.format('W  E  L  C  O  M  E'))
print()
print()
while True:

    contact = Contact()
    contact.check_if_txt_exists()
    contact.your_contacts(list_of_contacts, dic)
    
    if contact.is_empty():
        print()
        print('{}'.format('Your contacts list is empty!'))
        print()

        print('{}\n{}'.format('1 ==> ADD','anything else ==> QUIT' ))
        
        options = input('What would you like to do? ').strip()
        # Add contact
        if options == '1':
            system('cls')
            contact.add(list_of_contacts, dic)
        
        # Exit
        else:
            print('Bye Bye...')
            sleep(5)
            system('cls')
            break
    
    else:        
        print('{}\n{}\n{}\n{}\n{}'.
        format('1 ==> ADD','2 ==> DELETE' ,'3 ==> CHANGE' ,'4 ==> SEARCH' ,'anything else ==> QUIT'))
        
        options = input('What would you like to do? ').strip()

        # Add contact
        if options == '1':
            system('cls')
            contact.add(list_of_contacts, dic)

        # Delete contact
        elif options == '2':
            system('cls')
            name_of_the_person_that_will_be_deleted = input('Type the name that will be deleted: ').strip().upper()
            if contact.check_if_name_exists(list_of_contacts, dic, name_of_the_person_that_will_be_deleted):
                contact.show_wanted_contact(list_of_contacts, dic, name_of_the_person_that_will_be_deleted)
                phone_of_the_person_that_will_be_deleted = input('Type the phone number that will be deleted: ').strip()
                if contact.check_if_phoneNumber_exists(list_of_contacts, dic, phone_of_the_person_that_will_be_deleted):
                    contact.del_contact(list_of_contacts, dic, phone_of_the_person_that_will_be_deleted)
                else:
                    print('Incorrect! Try again!')
            else:
                print(f'{name_of_the_person_that_will_be_deleted} was not found!')
        
        # Change contact
        elif options == '3':
            system('cls')
            name_of_the_person_that_will_be_changed = input('Type the name that will be changed: ').strip().upper()
            if contact.check_if_name_exists(list_of_contacts, dic, name_of_the_person_that_will_be_changed):
                contact.show_wanted_contact(list_of_contacts, dic, name_of_the_person_that_will_be_changed)
                phone_of_the_person_that_will_be_changed = input('Type the phone number of the person that will be changed: ').strip()
                if contact.check_if_phoneNumber_exists(list_of_contacts, dic, phone_of_the_person_that_will_be_changed):
                    contact.change_contact(list_of_contacts, dic, name_of_the_person_that_will_be_changed)
                else:
                    print('Incorrect! Try again!')
            else:
                print(f'{name_of_the_person_that_will_be_changed} was not found!')
        
        # Search contact
        elif options == '4':
            system('cls')
            name_of_the_wanted_person = input('Who are you looking for? ').strip().upper()
            if contact.check_if_name_exists(list_of_contacts, dic, name_of_the_wanted_person):
                contact.show_wanted_contact(list_of_contacts, dic, name_of_the_wanted_person)
            else:
                print(f'{name_of_the_wanted_person} was not found!')

        # Exit
        else:
            print('Bye Bye...')
            sleep(5)
            system('cls')
            break