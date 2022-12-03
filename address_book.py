
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