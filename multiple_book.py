import json
import csv
import pandas as pd


class Multiplebook():

    def add_my_book(self,dict, adressbook_name, persons):
        '''
            Add all persons in new addressbook 
            give user input as addressbook name and persons
            return addressbook name
        '''
        if adressbook_name not in dict.keys():
            new_persons = persons.copy()
            dict.update({adressbook_name : new_persons})
            return adressbook_name

    def clear_person_dict(self, dict):
        '''
            delete all person in address book 
            dictionary
            return string 
        '''
        dict.clear()
        return "Clear all present persons sucessfully"

    def search_by_city(self, my_book, city):

        for book_key, book_value in my_book.items():
            for person_key, person_value in book_value.items():
                if person_value["city"] == city:
                    print(person_value)      

    def search_by_state(self, my_book, state):

        for book_key, book_value in my_book.items():
            for person_key, person_value in book_value.items():
                if person_value["state"] == state:
                    print(person_value) 

    def dict_of_city_persons(self, my_book):

        city_persons = {}
        unique_city = []

        for book_key, book_value in my_book.items():
            for person_key, person_value in book_value.items():
                if person_value["city"] not in unique_city:
                    unique_city.append(person_value["city"]) 

        ####
        for each_city in unique_city:
            persons_in_city = {}
            city_persons.update({each_city : persons_in_city})
            for book_key, book_value in my_book.items():
                for person_key, person_value in book_value.items():
                    if person_value["city"] == each_city:
                        city_person_key = len(persons_in_city)+1
                        persons_in_city.update({city_person_key : person_value}) 

        return city_persons  

    def dict_of_state_persons(self, my_book):

        state_persons = {}
        unique_state = []

        for book_key, book_value in my_book.items():
            for person_key, person_value in book_value.items():
                if person_value["state"] not in unique_state:
                    unique_state.append(person_value["state"]) 
        
        ######
        for each_state in unique_state:
            persons_in_state = {}
            state_persons.update({each_state : persons_in_state})
            for book_key, book_value in my_book.items():
                for person_key, person_value in book_value.items():
                    if person_value["state"] == each_state:
                        state_person_key = len(persons_in_state)+1
                        persons_in_state.update({state_person_key : person_value}) 

        return state_persons                

    def group_by(self, state_dict):

        key_count = {}
        for key, values in state_dict.items():
            key_count.update({key : len(values)}) 

        return key_count 

    def sorting_parameter(self, my_book, addbook_name, parameter):
    
        sorted_entries = {}
        person_list = []
        for key, value in my_book.items():
            if key == addbook_name:       
                for key1, value1 in value.items():
                    person_list.append(value1) 
                    
        sorted_list = sorted(person_list, key = lambda a: a[parameter])
        
        for i in range(0, len(sorted_list)):
            sorted_entries.update({i+1 : sorted_list[i]})
            
        return sorted_entries 

    def write_text_file(self, dict, file_name):

        with open(f"{file_name}.txt", "w") as text_file:
            text_file.write(str(dict))  

        return f"file create sucessfull + {file_name}"

    def read_text_file(self, file_path):
        try:
            with open(file_path) as text_file:
                content = text_file.read()
                return content

        except FileNotFoundError:
            print("File not Found")        

    def write_in_json(self, my_book, file_name):

        with open(f"{file_name}.json", "w") as json_file:
                json.dump(my_book, json_file, indent = 2)


    def read_json_file(self, file_paath):
        try:
            with open(file_paath, "r") as json_file:
                content = json.load(json_file)
            return content

        except FileNotFoundError:
            print("File not Found")

    def write_in_csv(self, my_book, file_name):

        with open(f'{file_name}.csv', "a") as csv_file:    
            fields = ['book_name', 'sr_no', 'first_name' , 'last_name' , 'address', 'city' , 'state' , 'zip_code' , 'phone_no' , 'email']
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(fields)
            
            for book_name, persons in my_book.items():
                for sr_no, detail in persons.items():
                    data = [book_name, sr_no, detail['first_name'], detail['last_name'], detail['address'], detail['city'], detail['state'], detail['zip_code'], detail['phone_no'], detail['email']]                  
                    csv_writer.writerow(data)

    def read_csv_file(self, file_paath):
        try:
            with open(file_paath, "r") as csv_file:
                data = pd.read_csv(csv_file)
                print(data)

        except FileNotFoundError:
            print("File not Found")