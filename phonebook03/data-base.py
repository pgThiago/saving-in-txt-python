from os import path
from time import sleep
while True:
    def check_if_txt_exists():
        if path.exists('contacts.txt') == True:
            return True
        else:
            return False
    if check_if_txt_exists() == False:
        file = open('contacts.txt', 'w')
    contacts = {}
    dic_aux = {}
    file = open('contacts.txt', 'r')
    lines = file.readlines()
    
    def is_empty():
        check_if_txt_exists()
        if not lines:   
            return True
        else:
            return False
    
    def get_datas_from_txt():
        check_if_txt_exists()
        is_empty()
        if is_empty() == True:
            print('No contacts found!')
        else:
            file = open('contacts.txt', 'r')
            lines = file.readlines()
            for line in lines:
                line_split = line.split('-')
                name = line_split[0]
                name_string = ''.join(line_split[0]) # Name to string so we can use the upper and strip methods
                name = name_string.upper().strip()
                phoneNumber = line_split[1]
                dic_aux[name] = phoneNumber
            file.close()
    
    def setDatas_in_Empty_File():
        check_if_txt_exists()
        name = input('Name: ').upper().strip()
        phoneNumber = input('Phone number: ')
        dic_aux[name] = phoneNumber
        add_to_dict()
        send_to_database()
    
    def setDatas_in_not_Empty_File():
        check_if_txt_exists()
        is_empty()
        if is_empty() == False:
            get_datas_from_txt()
            name = input('Name: ').upper().strip()
            phoneNumber = input('Phone number: ')
            dic_aux[name] = phoneNumber
            add_to_dict()
            send_to_database()
            get_datas_from_txt()
            file.close()
        else:
            setDatas_in_Empty_File()
    
    def change():
        check_if_txt_exists()
        is_empty()
        if is_empty() == False:
            get_datas_from_txt()
            add_to_dict()
            contact_to_change = input('Contact name you wanna change: ').upper().strip()
            for key in list(dic_aux.keys()):
                if key == contact_to_change:
                    new_name = input('New name: ').upper().strip()
                    new_phone_number = input('New phone number: ')
                    dic_aux[new_name] = dic_aux.pop(key)
                    dic_aux[new_name] = new_phone_number
                    break   
            else:
                print(f'"{contact_to_change}" WAS NOT FOUND!')
                print()
    
    def delete():
        check_if_txt_exists()
        is_empty()
        if is_empty() == False:
            get_datas_from_txt()
            add_to_dict()
            contact_to_delete = input('Contact name you wanna delete: ').upper().strip()
            for key in list(dic_aux.keys()):
                if contact_to_delete == key:
                    del dic_aux[key]
                    break
            else:
                print(f'"{contact_to_delete}" WAS NOT FOUND!')
                print()        
    
    def search():
        check_if_txt_exists()
        is_empty()
        if is_empty() == False:
            get_datas_from_txt()
            add_to_dict()
            contact_to_search = input('Who u looking for? ').strip().upper()
            print()
            for key, value in dic_aux.items():
                if contact_to_search == key:
                    print(f'Here it is >>>>> Name: {key.capitalize()} ---- Phone number: {value}')
                    break
            else:
                print(f'"{contact_to_search}" WAS NOT FOUND!')
                print()
    
    def add_to_dict():
        check_if_txt_exists()
        for key, value in dic_aux.items():
            contacts[key] = value
    
    def your_contacts():
        is_empty()
        if is_empty() == False:
            get_datas_from_txt()
            add_to_dict()
            check_if_txt_exists()
            if len(contacts.keys()) == 1:
                print('1 CONTACT')
            else:
                print(f'YOU HAVE {len(contacts.keys())} CONTACTS.')
            print()
            print('$' * 50)
            print()
            print('YOUR CONTACTS LIST:')
            print()
            for contact in sorted(contacts.items()):
                name_str = ''.join(contact[0])
                print(f'Name: {name_str.capitalize()} ---- Phone number: {contact[1]}')
            print('$' * 50)
            print()
        else:
            print('$' * 50)
            print()
            print('YOUR CONTACTS LIST IS EMPTY!')
            print()
            print('$' * 50)
            print()
    
    def send_to_database():
        add_to_dict()
        file = open('contacts.txt', 'w')
        for contact in sorted(dic_aux.items()):
            string = f'{contact[0]}-{contact[1]}'
            file.write(f'{string.strip()}\n')
        file.close()    
    
    your_contacts()
    
    print('=-' * 17)
    print('Select one of the options below:')
    print('{:^27}\n{:^30}\n{:^30}\n{:^30}\n{:^28}'
    .format('1 - ADD', '2 - CHANGE', '3 - DELETE', '4 - SEARCH', '5 - EXIT'))
    print('=-' * 17)
    
    option = input('What you wanna do? ').strip()
    
    # Here starts the conditions
    if option == '1':
        setDatas_in_not_Empty_File()
        send_to_database()
    elif option == '2':
        change()
        send_to_database()
    elif option == '3':
        delete()
        send_to_database()
    elif option == '4':
        search()    
        send_to_database()
    elif option == '5':
        print('Finishing...')
        sleep(3)
        print('Finished.')
        break
    else:
        print('unavailable option')
