
class User:

    def add_user(self, first_name, last_name, dict):
        '''
            add new user 
            give user input as first and last name
            return address book
        '''
        
        key = len(dict)+1   
        if key not in dict.keys():
            dict.update({key : {"first_name" : first_name, "last_name": last_name}}) 
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
        persons = dict.clear()
        return "Clear all present persons sucessfully"


if __name__ == "__main__":

    ## objects of class
    user = User()
    multiplebook = Multiplebook()

    ## BOOKS / Dictionary
    new_multiple_addbook = {}
    addbook = {1: {'first_name': 'vipul', 'last_name': 'shete'}, 2: {'first_name': 'vaibhav', 'last_name': 'joishi'}}

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
            last_name = input("Enter last name: ")

            print (user.add_user(first_name, last_name, addbook))

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