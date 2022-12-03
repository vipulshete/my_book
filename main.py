from address_book import User
from multiple_book import Multiplebook


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
        print("8. Search by city or state")
        print("9. View dictionar of city or state wise persons")
        print("10. Count by city or state")
        print("11. Address book sort by parameter")

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

                print (user.add_user(first_name, last_name, address, city, state, zip_code, phone_no, email, addbook))

            else:
                print("Please enter unique first name") 

        elif choice == 2:
            ## edit last name
            first_name = input("Enter first name: ")
            print(user.edit_user(first_name, addbook))

        elif choice == 3:
            ## delete user
            first_name = input("Enter first name: ")
            print(user.delete_user(first_name, addbook))

        elif choice == 4:
            ## print all dictionary
            print(addbook) 

        elif choice == 5:
            ## add new user
            addbook_name = input("Enter address book name name: ")
            print(multiplebook.add_my_book(new_multiple_addbook, addbook_name, addbook)) 

        elif choice == 6:
            ## clear all current persons
            print(multiplebook.clear_person_dict(addbook))

        elif choice == 7:
            ## Print all dictionary
            print(new_multiple_addbook)

        elif choice == 8:
            ## Persons search by city or state

            print("Search persons by city or state")
            
            print("\n" + "1. search by city")
            print("2. search by state" + "\n")

            select = int(input("select the option: ") )

            if select == 1:
                city = input("Enter the city name: ")
                print(multiplebook.search_by_city(new_multiple_addbook, city))

            elif select == 2:
                state = input("Enter the state name: ")
                print(multiplebook.search_by_state(new_multiple_addbook, state))    

        elif choice == 9:
        ## Dictionary of city or state persons

            print("Search persons by city or state")
            
            print("\n" + "1. View city wise persons")
            print("2. View state wise persons" + "\n")

            select = int(input("select the option: ") )

            if select == 1:
                print(multiplebook.dict_of_city_persons(new_multiple_addbook))

            elif select == 2:
                print(multiplebook.dict_of_state_persons(new_multiple_addbook))   

        elif choice == 10:
        ## Count by city or state 

            print("Search persons by city or state")
            
            print("\n" + "1. View city wise persons")
            print("2. View state wise persons" + "\n")

            select = int(input("select the option: ") )

            if select == 1:
                city_dict = multiplebook.dict_of_city_persons(new_multiple_addbook)
                print(multiplebook.group_by(city_dict))
                
            elif select == 2:
                state_dict = multiplebook.dict_of_state_persons(new_multiple_addbook)
                print(multiplebook.group_by(state_dict))         

        elif choice == 11:
        ## Address book sort by parameter

            print("Address book sort by parameter")
            address_book_name = input("Enter the address book name: ")
            parameter = input("Enter sort by parameter: ")

            print(multiplebook.sorting_parameter(new_multiple_addbook, address_book_name, parameter))
            
        elif choice == 0:
            break