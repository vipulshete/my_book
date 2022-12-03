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