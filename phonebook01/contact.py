from os import path 
from operator import itemgetter
from time import sleep

class Contact:
    
    def check_if_txt_exists(self):
        '''Checks if txt exists and if not just create it'''
        if path.exists('contacts.txt') == True:
            return True
        else:
            file = open('contacts.txt', 'w')
            file.close()
        
    def is_empty(self):
        '''checks if txt is empty. Return True if it is empty'''
        file = open('contacts.txt', 'r')
        lines = file.readlines()
        if not lines:
            return True
        else:
            return False

    def add_to_list(self, lis, di):
        '''Add the dict to the list
           lis: list_of_contacts in main.py
           di: dicionary in main.py 
        '''
        lis.append(di.copy())   
    def add_to_dictionary(self, di, lis, name, phone, birthday):
        '''Add name, phone and birthday to the dictionary'''
        di["Name"] = self.name
        di["Phone"] = self.phone
        di["Birthday"] = self.birthday.strip('\n')
        self.add_to_list(lis, di)

    def get_datas_from_txt(self, lis, di):
        '''Gets all contacts from txt'''
        file = open('contacts.txt','r')
        lines = file.readlines()
        for line in lines:
            line_split = line.strip('\n')
            line_split = line.split('=%$#=')
            self.name = ''.join(line_split[0])
            self.phone = ''.join(line_split[1])
            self.birthday = ''.join(line_split[2]).strip('\n')
            
            self.add_to_dictionary(di, lis, self.name, self.phone, self.birthday)
                   
    def send_to_txt(self, lis): 
        ''' Send contacts to txt '''     
        final_list = []
        for item in sorted(lis, key=itemgetter('Name')):
            if item not in final_list:
                final_list.append(item)
        
        with open('contacts.txt', 'w') as file: 
            for person in sorted(final_list, key=itemgetter('Name')):
                string = (f'{person["Name"]}=%$#={person["Phone"]}=%$#={person["Birthday"]}').strip()
                file.write(f'{string}\n')

    def your_contacts(self, lis, di):
        '''Show all contacts in txt to the user'''
        self.get_datas_from_txt(lis, di)
        # "Final list" to prevent duplicated items
        final_list = []
        for item in sorted(lis, key=itemgetter('Name')):
            if item not in final_list:
                final_list.append(item)
        
        if len(final_list) == 1:
            one_contact = f'{len(final_list)}  CONTACT'
            print(f'{one_contact}')
        else:
            lot_of_contacts = f'{len(final_list)}  CONTACTS'
            print(f'{lot_of_contacts}')
        sleep(0.3)
        print('YOUR  CONTACTS LIST')
        
        print('=-=' * 50)
        for person in sorted(final_list, key=itemgetter('Name')):
            sleep(0.3)
            txt = f'Name: {person["Name"]:<50}  Phone: {person["Phone"]:<50}  Birthday: {person["Birthday"]:>10}'
            print(f'{txt:^150}')
        print('=-=' * 50)

    def check_if_name_exists(self, lis, di, wanted_name):
        self.get_datas_from_txt(lis, di) 
        for con in sorted(lis, key=itemgetter('Name')):
            if con["Name"] == wanted_name:
                return True
        else:
            return False

    def check_if_phoneNumber_exists(self, lis, di, wanted_phone):
        self.get_datas_from_txt(lis, di) 
        for con in sorted(lis, key=itemgetter('Name')):
            if con["Phone"] == wanted_phone:
                return True
        else:
            return False


    def add(self, lis, di):
        ''' Add a new contact to txt '''
        self.get_datas_from_txt(lis, di)
        
        self.name = input('{}'.format('Name: ')).upper().strip()
        self.phone = input('{}'.format('Phone: '))
        self.birthday = input('{}'.format('Birthday (dd/mm/yyyy) please add "/ /" : ')).strip('\n')
        
        self.add_to_dictionary(di, lis, self.name, self.phone, self.birthday)
        self.send_to_txt(lis)

        
    def del_contact(self, lis, di, phone_that_will_be_deleted):
        self.get_datas_from_txt(lis, di) 
        for con in sorted(lis, key=itemgetter('Name')):
            if con["Phone"] == phone_that_will_be_deleted:
                ind = lis.index(con)
                del lis[ind]
                
        self.send_to_txt(lis)

    
    def change_contact(self, lis, di, wanted_name):
        for con in sorted(lis, key=itemgetter('Name')):
            if con["Name"] == wanted_name:
                ind = lis.index(con)
                del lis[ind]
        newName = input('{}'.format('New name: ')).upper().strip()
        newPhone = input('{}'.format('New phone: ')).strip()
        newBirthday = input('{}'.format('Birthday (dd/mm/yyyy) please add "/ /" : ')).strip('\n')
        di["Name"] = newName
        di["Phone"] = newPhone
        di["Birthday"] = newBirthday
        self.add_to_list(lis, di)
        self.send_to_txt(lis)
        
    def show_wanted_contact(self, lis, di, wanted_person):
        # Final list to not print duplicated items
        final_list = []
        for item in sorted(lis, key=itemgetter('Name')):
            if item not in final_list:
                final_list.append(item)
        for con in sorted(final_list, key=itemgetter('Name')):
            if con["Name"] == wanted_person:
                print(f'Here it is ====>>>> | Name: {con["Name"]}  Phone: {con["Phone"]}  Birthday: {con["Birthday"]} |')
                