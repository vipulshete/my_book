
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
        
        for user in  dict.items():
            new_user = (user[1])
            if new_user["first_name"] == first_name:
                last_name = input("Enter last name: ")
                new_user["last_name"] = last_name
            return user
              


if __name__ == "__main__":

    user = User()

    addbook = {1: {'first_name': 'vipul', 'last_name': 'shete'}, 2: {'first_name': 'vaibhav', 'last_name': 'joishi'}}

    while True:

        print("\n" + "1. To Add user")
        print("2. Edit last name using first name")
        print("3. view address book")
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
            ## print all dictionary
            print(addbook)    

        elif choice == 0:
            break