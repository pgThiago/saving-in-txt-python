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
        print('{:>74}'.format('Your contacts list is empty!'))
        print()

        print('{:>73}\n{:>86}'.format('1 ==> ADD','anything else ==> QUIT' ))
        
        options = input('{:>91}'.format('What would you like to do? ')).strip()
        
        if options == '1':
            system('cls')
            contact.add(list_of_contacts, dic)
        
        else:
            break
    
    else:        
        print('{:>73}\n{:>76}\n{:>76}\n{:>76}\n{:>86}'.
        format('1 ==> ADD','2 ==> DELETE' ,'3 ==> CHANGE' ,'4 ==> SEARCH' ,'anything else ==> QUIT'))
        
        options = input('{:>75}'.format('What would you like to do? ')).strip()

        if options == '1':
            system('cls')
            contact.add(list_of_contacts, dic)
        
        elif options == '2':
            system('cls')
            search_to_delete = input('{:>75}'.format('Who are you looking for to delete? ')).upper().strip()
            # Shows who is going to be deleted
            if contact.search(list_of_contacts, dic, search_to_delete) == True:
                contact.show_wanted_contact(list_of_contacts, dic, search_to_delete)
                delete = input('{:>75}'.format('Type the contact phone number that you wanna delete: ')).strip()
                if contact.delete(list_of_contacts, dic, delete) == True:
                    contact.del_contact(list_of_contacts, dic, delete)
                    print(f'{search_to_delete:>70} has been deleted.')
                else:
                    print('{:^150}'.format('Incorrect! Try again!'))
            else:
                print(f'{search_to_delete:^150} was not found.')
        
        elif options == '3':
            system('cls')
            search_to_change = input('{:>75}'.format('Who are you looking for to change? ')).upper().strip()
            # Shows who is going to be changed
            if contact.search(list_of_contacts, dic, search_to_change) == True:
                contact.show_wanted_contact(list_of_contacts, dic, search_to_change)
                phone_change = input('{:>75}'.format('Type the contact phone number that you wanna change: ')).strip()
                if contact.change(list_of_contacts, dic, phone_change, search_to_change) == True:
                    contact.add_to_dic_after_calling_change_function(list_of_contacts, dic, phone_change, search_to_change)
                    print(f'{search_to_change:>75} has been updated')
                else:
                    print('{:^150}'.format('Incorrect! Try again!'))
            else:
                print(f'{search_to_change:^150} was not found.')
        
        elif options == '4':
            system('cls')
            search = input('{:>75}'.format('Who are you looking for? ')).upper().strip()
            contact.search(list_of_contacts, dic, search)
            contact.show_wanted_contact(list_of_contacts, dic, search)
        else:
            print('Bye Bye...')
            sleep(5)
            system('cls')
            break   
  