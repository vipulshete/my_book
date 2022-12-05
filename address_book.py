
class User:

    def add_user(self, first_name, last_name, address, city, state, zip_code, phone_no, email, dict):
        '''
            add new user 
            give user input as first and last name
            return address book
        '''
        
        key = len(dict)+1   
        if key not in dict.keys():
            dict.update({key : {"first_name" : first_name, "last_name" : last_name, "address" : address, "city" : city, "state" : state, "zip_code" : zip_code, "phone_no" : phone_no, "email" : email}}) 
            return dict

    def edit_user(self, first_name, dict):
        '''
            edit user last name using  his privious first name
            give user input as privious first and modified last name
            return modifies user details
        '''
        for key, values in  dict.items():
            if values["first_name"] == first_name:
                last_name = input("Enter last name: ")
                values["last_name"] = last_name
                return values

    def delete_user(self, first_name, dict):
        '''
            edit user last name using  his privious first name
            give user input as privious first and modified last name
            return modifies user details
        '''
        for key, values in  dict.items():
            if values["first_name"] == first_name:
                del dict[key]
                return dict      

    def check_unique_first_name(self, first_name, dic):
        '''
            check unique name in dictionary
            give user input as first name and dictionary name
            return unique name present or not
        '''
        fn_list = []
        for key, values in dic.items():
            fn_list.append(values["first_name"]) 

        if first_name not in fn_list:
            return first_name
        else:
            return "first name alredy present"       


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

    # def add_person_in_perticulare_addressbook(self, dict, book_name):

    #     for book_name_key, persons in dict.items():
    #         if book_name == book_name_key:

    #             book_name_key.update({key : {person_details}})
    #          for book_key, book_value in my_book.items():
    #             for person_key, person_value in book_value.items():
    #                 if person_value["state"] == state:
    #                     print(person_value) 


if __name__ == "__main__":

    ## objects of class
    user = User()
    multiplebook = Multiplebook()

    ## BOOKS / Dictionary
    new_multiple_addbook = {'self_book': {1: {'first_name': 'vipul', 'last_name': 'shete', 'address': 'raygad', 'city': 'beed', 'state': 'maha', 'zip_code': 123, 'phone_no': 1254685, 'email': 'vipulshea55652'}, 2: {'first_name': 'renu', 'last_name': 'gonde', 'address': 'raygad', 'city': 'kaij', 'state': 'maha', 'zip_code': 45, 'phone_no': 25454, 'email': 'asdsf'}}, 'brother_book': {1: {'first_name': 'vaibhav', 'last_name': 'shete', 'address': 'sds', 'city': 'pune', 'state': 'hyd', 'zip_code': 546, 'phone_no': 255468, 'email': 'dsda'}}}
    addbook = {}

    while True:

        print("\n" + "1. To Add user")
        print("2. Edit last name using first name")
        print("3. delete user using first name")
        print("4. view current address book")
        print("5. Add current address books")
        print("6. Clear current all persons")
        print("7. View all address books")

        print("To exit select 0" + "\n")

        choice = int(input("Select opctions: "))

        if choice == 1:
            ## add new user
            
            first_name = input("Enter first name: ")
            fname =  user.check_unique_first_name(first_name, addbook)
            
            if first_name == fname:
                last_name = input("Enter last name: ")
                address = input("Enter address: ")
                city = input("Enter city: ")
                state = input("Enter state: ")
                zip_code = int(input("Enter zip_code: "))
                phone_no = int(input("Enter phone_no: "))
                email = input("Enter email: ")


                print("\n" + "Add user in perticular address book")
                print("1. Yes")
                print("2. No")

                select = int(input("Select the option"))

                if select == 1:

                    book_name = input("Enter address book name: ")
                    for book_name_key, persons in new_multiple_addbook.items():
                        if book_name_key == book_name:
                            print (user.add_user(first_name, last_name, address, city, state, zip_code, phone_no, email, persons))

                if select == 2:
                    print (user.add_user(first_name, last_name, address, city, state, zip_code, phone_no, email, addbook))


            else:
                print("Please enter unique first name") 

        if choice == 2:
            ## edit last name
            first_name = input("Enter first name: ")
            print(user.edit_user(first_name, addbook))

        if choice == 3:
            ## delete user
            first_name = input("Enter first name: ")
            print(user.delete_user(first_name, addbook))

        if choice == 4:
            ## print all dictionary
            print(addbook) 

        if choice == 5:
            ## add new user
            addbook_name = input("Enter address book name name: ")
            print(multiplebook.add_my_book(new_multiple_addbook, addbook_name, addbook)) 

        if choice == 6:
            ## clear all current persons
            print(multiplebook.clear_person_dict(addbook))

        if choice == 7:
            ## Print all dictionary
            print(new_multiple_addbook)

        elif choice == 0:
            break