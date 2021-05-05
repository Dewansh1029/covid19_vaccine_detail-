import covid_db as database
import sys
from sys import exit
import datetime

# def main():
#     val = input(" For adding vaccine name, date and place of manufacturing and date of expiry: \n Press 1 \n For adding vaccine name its availability and quantity: \n Press 2 \n To see vaccine name, date and place of manufacturing and date of expiry: \n Press 3 \n To see vaccine name its availability and quantity: \n Press "\
#         "4 \n For updating vaccine manufacture and expiry\n Press 5\n For updating availability and quantity: \n Press 6\n For deleting any information: \n Press 7\n")
#     if val == "1" :
#         name = input("Enter vaccine name: ")
#         detail = input("Enter vaccine detail: ")
#         manufacture_place = input("Enter vaccine manufacture place: ")
#         manufacture_date = input("Enter vaccine manufacture date(YYYY-MM-DD): ")
#         expiry = input("Enter vaccine expiry(YYYY-MM-DD): ")
        
#         if manufacture_date > expiry :
#             print ('Incorrect data in date field!')
#             sys.exit()
#         else :
#             col_name = ['vac_name', 'vac_detail', 'vac_manufacture_place', 'vac_manufacture_date', 'vac_expiry']
#             col_values = [name, detail, manufacture_place, manufacture_date, expiry]
#             table_name = "aboutvac"
#             database.insertQuery (col_name, col_values, table_name)
#             print("Successfully added, press 3 to see")

#     elif val == "2" :
#         name = input("Enter vaccine name: ")
#         available_in_cities = input("Enter vaccine available in cities: ")
#         available_from = input("Enter vaccine availablity start date(YYYY-MM-DD): ")
#         available_till = input("Enter vaccine availablity end date(YYYY-MM-DD): ")
#         quantity_in_bottles = input("Enter no. of bottles of available vaccine: ")
        
#         if available_from > available_till :
#             print ('Incorrect data in date field!')
#             sys.exit()
#         else :
#             col_name = ['vac_name', 'vac_cities', 'vac_startdate' , 'vac_enddate', 'vac_quantity']
#             col_values = [name, available_in_cities, available_from, available_till, quantity_in_bottles]
#             table_name = "eachvacdetail"
#             database.insertQuery (col_name, col_values, table_name)
#             print("Successfully added, press 4 to see")

#     elif val == "3" :
#         print("Vaccine name and manugactured by: \n")
#         lst_col = ['vac_name', 'vac_detail']
#         table_name = "aboutvac"
#         select = database.selectQuery (lst_col, table_name)
#         for x in select:
#             print(x)
        
#     elif val == "4" :
#         print("Vaccine name and quantity: \n")
#         lst_col = ['vac_name', 'vac_quantity']
#         table_name = "eachvacdetail"
#         select = database.selectQuery (lst_col, table_name)
#         for x in select:
#             print(x)
        
#     elif val == "5" :
#         table_name = "aboutvac"
#         vac_name = input('Enter vaccine name whose details you want to change: ')
        
#         vac_manufactured_by = input('Enter new manufacturer ')
#         vac_manufacture_place = input('Enter new manufacture place ')
#         vac_manufacture_date = input('Enter new manufacture date ')
#         vac_expiry = input('Enter new expiry date ')
        
#         col_name = ['vac_detail', 'vac_manufacture_place', 'vac_manufacture_date', 'vac_expiry']
#         col_values = [vac_manufactured_by, vac_manufacture_place, vac_manufacture_date, vac_expiry]

#         database.updateQuery (table_name, col_name, col_values, vac_name)
#         print("Successfully updated, press 3 to see")

#     elif val == "6" :
#         table_name = "eachvacdetail"
#         vac_name = input('Enter vaccine name whose details you want to change: ')
        
#         cities = input('Enter new manufacturer: ')
#         startdate = input('Enter new manufacture place: ')
#         enddate = input('Enter new manufacture date: ')
#         quantity = input('Enter new expiry date: ')
        
#         col_name = ['vac_cities', 'vac_startdate', 'vac_enddate', 'vac_quantity']
#         col_values = [cities, startdate, enddate, quantity]

#         database.updateQuery (table_name, col_name, col_values, vac_name)
#         print("Successfully updated, press 4 to see")


#     elif val == "7" :
#         table_name = input('Enter table name: ')
#         vac_name = input('Enter vaccine name to be deleted: ')
#         database.deleteQuery (table_name, vac_name)
#         print("Successfully deleted")


#     else :
#         print("Incorrect input")

def input_table2(name, available_in_cities, available_from, available_till, quantity_in_bottles) :
    print('Inside businesslayer function')
    col_name = ['vac_name', 'vac_cities', 'vac_startdate' , 'vac_enddate', 'vac_quantity']
    col_values = [name, available_in_cities, available_from, available_till, quantity_in_bottles]
    table_name = "vaccine_loc"
    database.insertQuery (col_name, col_values, table_name)

def input_table1(name, detail, manufacture_place, manufacture_date, expiry) :
    col_name = ['vac_name', 'vac_detail', 'vac_manufacture_place', 'vac_manufacture_date', 'vac_expiry']
    col_values = [name, detail, manufacture_place, manufacture_date, expiry]
    table_name = "vaccine_details"
    database.insertQuery (col_name, col_values, table_name)

def insert_userDetails(name, userid, password) :
    col_name = ['name', 'userid', 'password']
    col_values = [name, userid, password]
    table_name = "user_details"
    database.insertQuery (col_name, col_values, table_name)

def insert_contact(cname, cemail, caddress) :
    col_name = ['name', 'email', 'address']
    col_values = [cname, cemail, caddress]
    table_name = 'contact_details'
    database.insertQuery (col_name, col_values, table_name)
# def show_details(vaccine_name) :
#     lst_col = ['vac_name']
#     table_name = 'vaccine_details'
#     names = str(database.selectQuery(lst_col, table_name))
#     print(names)
#     if vaccine_name not in names or vaccine_name == '':
#         print('Vaccine name does not exits in table!')
#         return [],0
#         # return 0
#     else :
#         lst_output = database.show_single_row(vaccine_name)
#         print(type(lst_output))
#         return lst_output,1
#         # return 1
def only_vac_name():
    lst_col = ['vac_name']
    table_name = "vaccine_details"
    data = database.selectQuery (lst_col,table_name)
    return data

# def select_by_vac_name() :
#     lst_col = ['vac_name']
#     table_name = "vaccine_details"
#     data = selectQuery (lst_col,table_name)
#     print(data)
#     return data


def update_by_vac_name(vname, vby, vplace, vdate, vexpiry) :
    table_name = 'vaccine_details'
    col_name = ['vac_detail', 'vac_manufacture_place', 'vac_manufacture_date', 'vac_expiry']
    col_values = [vby, vplace, vdate, vexpiry]
    vac_name = vname
    database.updateQuery (table_name, col_name, col_values, vac_name)
    return

def show_details(vaccine_name) :
    lst_output = database.show_single_row(vaccine_name)
    if len(lst_output)==0 or vaccine_name == '':
        print('Vaccine name does not exits in table!')
        return [],0
        # return 0
    else :
        return lst_output,1
        # return 1

def show_full_table_details(name) :
    lst_output = database.search_all_rows(name)
    if len(lst_output) == 0 or name == '':
        print('Vaccine name does not exits in table!')
        return [],0
    else :
        return lst_output,1
        # return 1

def check_user(userid, password) :
    table_name = "user_details"
    user_lst = ['userid']
    users = str(database.selectQuery(user_lst, table_name))
    print(users)
    pass_lst = ['password']
    passwords = str(database.select_where(pass_lst, table_name, userid))
    print(passwords)
    if userid not in users or len(userid)==0:
        print('You are not registered \n Sign up to register yourself!')
        return 0
    elif password not in passwords or len(password)==0:
        print('Incorrect password!')
        return 1
    return 2

def checkinput(name):
    if len(name) == 0  :
        print('Data is not valid!')
        sys.exit()

def signupDetails(name, uid, password, conpassword) :
    if len(name) == 0 or len(uid) == 0 or len(password) == 0:
        return 0
    elif password != conpassword:
        return 1
    return 2

# def show_dropdown2val1() :

    # table_name = "vaccine_details"
    # col_name = [vac_detail, vac_manufacture_place, vac_manufacture_date,vac_expiry]
    # updateQuery (table_name, col_name, col_values, vac_name)

def main():

    val = input(" For adding vaccine name, date and place of manufacturing and date of expiry: \n Press 1 \n For adding vaccine name its availability and quantity: \n Press 2 \n To see vaccine name, date and place of manufacturing and date of expiry: \n Press 3 \n To see vaccine name its availability and quantity: \n Press "\
    "4 \n For updating vaccine manufacture and expiry\n Press 5\n For updating availability and quantity: \n Press 6\n For deleting any information: \n Press 7\n To exit, type exit: \n")

    while val :
        if val == "exit" :
            sys.exit()
        # val = input(" For adding vaccine name, date and place of manufacturing and date of expiry: \n Press 1 \n For adding vaccine name its availability and quantity: \n Press 2 \n To see vaccine name, date and place of manufacturing and date of expiry: \n Press 3 \n To see vaccine name its availability and quantity: \n Press "\
        #     "4 \n For updating vaccine manufacture and expiry\n Press 5\n For updating availability and quantity: \n Press 6\n For deleting any information: \n Press 7\n")
        if val == "1" :
            name = input("Enter vaccine name: ")
            checkinput(name)
            detail = input("Enter vaccine detail: ")
            checkinput(detail)
            manufacture_place = input("Enter vaccine manufacture place: ")
            checkinput(manufacture_place)
            manufacture_date = input("Enter vaccine manufacture date(YYYY-MM-DD): ")
            checkinput(manufacture_date)
            expiry = input("Enter vaccine expiry(YYYY-MM-DD): ")
            checkinput(expiry)
            
            if manufacture_date > expiry :
                print ('Incorrect data in date field!')
                return
            else :
                col_name = ['vac_name', 'vac_detail', 'vac_manufacture_place', 'vac_manufacture_date', 'vac_expiry']
                col_values = [name, detail, manufacture_place, manufacture_date, expiry]
                table_name = "vaccine_details"
                database.insertQuery (col_name, col_values, table_name)

        elif val == "2" :
            name = input("Enter vaccine name: ")
            checkinput(name)

            lst_col = ['vac_name']
            table_name = 'vaccine_details'
            names = str(database.selectQuery(lst_col, table_name))
            if name not in names:
                print('Vaccine location can not be added, first add vaccine details!')
                break


            available_in_cities = input("Enter vaccine available in cities: ")
            checkinput(available_in_cities)
            available_from = input("Enter vaccine availablity start date(YYYY-MM-DD): ")
            checkinput(available_from)
            try:
                datetime.datetime.strptime(available_from, '%Y-%m-%d')
            except ValueError:
                print("This is the incorrect date string format. It should be YYYY-MM-DD")
                continue
            available_till = input("Enter vaccine availablity end date(YYYY-MM-DD): ")
            checkinput(available_till)
            try:
                datetime.datetime.strptime(available_till, '%Y-%m-%d')
            except ValueError:
                print("This is the incorrect date string format. It should be YYYY-MM-DD")
                continue
            quantity_in_bottles = input("Enter no. of bottles of available vaccine: ")
            checkinput(quantity_in_bottles)
            # if type(quantity_in_bottles) != int :
            #     print('Invalid data!')
            #     print(type(quantity_in_bottles))
            #     continue
            
            if available_from > available_till :
                print ('Incorrect data in date field!')
                return
                # sys.exit()
            else :
                col_name = ['vac_name', 'vac_cities', 'vac_startdate' , 'vac_enddate', 'vac_quantity']
                col_values = [name, available_in_cities, available_from, available_till, quantity_in_bottles]
                table_name = "vaccine_loc"
                database.insertQuery (col_name, col_values, table_name)

        elif val == "3" :
            lst_col = ['vac_name', 'vac_detail']
            table_name = "vaccine_details"
            select = database.selectQuery (lst_col, table_name)
            print('Vaccine name','    ', 'vaccine manufactured by:')
            for x in select :
                print(x[0],'          ',x[1])
            
        elif val == "4" :
            lst_col = ['vac_name', 'vac_quantity']
            table_name = "vaccine_loc"
            select = database.selectQuery (lst_col, table_name)
            print('Vaccine name','    ', 'vaccine quantity(in bottles):')
            for x in select :
                print(x[0],'          ',x[1])
            
        elif val == "5" :
            table_name = "vaccine_details"
            vac_name = input('Enter vaccine name whose details you want to change: ')
            checkinput(vac_name)

            lst_col = ['vac_name']
            names = str(database.selectQuery(lst_col, table_name))
            if vac_name not in names:
                print('Vaccine name does not exits in table!')
                break
            else :
                vac_manufactured_by = input('Enter new manufacturer ')
                checkinput(vac_manufactured_by)
                vac_manufacture_place = input('Enter new manufacture place ')
                checkinput(vac_manufacture_place)
                vac_manufacture_date = input('Enter new manufacture date ')
                invalidinput(vac_manufacture_date)
                try:
                    datetime.datetime.strptime(vac_manufacture_date, '%Y-%m-%d')
                except ValueError:
                    print("This is the incorrect date string format. It should be YYYY-MM-DD")
                    continue
                vac_expiry = input('Enter new expiry date ')
                invalidinput(vac_expiry)
                
                col_name = ['vac_detail', 'vac_manufacture_place', 'vac_manufacture_date', 'vac_expiry']
                col_values = [vac_manufactured_by, vac_manufacture_place, vac_manufacture_date, vac_expiry]

                database.updateQuery (table_name, col_name, col_values, vac_name)
            

        elif val == "6" :
            table_name = "vaccine_loc"

            vac_name = input('Enter vaccine name whose details you want to change: ')
            checkinput(vac_name)

            lst_col = ['vac_name']
            names = str(database.selectQuery(lst_col, table_name))
            if vac_name not in names:
                print('Vaccine name does not exits in table!')
                break
            cities = input('Enter new manufacture city: ')
            checkinput(cities)
            startdate = input('Enter new avalable start date: ')
            checkinput(startdate)
            try:
                datetime.datetime.strptime(startdate, '%Y-%m-%d')
            except ValueError:
                print("This is the incorrect date string format. It should be YYYY-MM-DD")
                continue
            enddate = input('Enter new avalable end date: ')
            checkinput(enddate)
            try:
                datetime.datetime.strptime(enddate, '%Y-%m-%d')
            except ValueError:
                print("This is the incorrect date string format. It should be YYYY-MM-DD")
                continue
            quantity = input('Enter new quantity ')
            checkinput(quantity)
            
            col_name = ['vac_cities', 'vac_startdate', 'vac_enddate', 'vac_quantity']
            col_values = [cities, startdate, enddate, quantity]

            database.updateQuery (table_name, col_name, col_values, vac_name)

        elif val == "7" :
            table_name = input('Enter table name: ')
            if table_name != 'vaccine_details' and table_name != 'vaccine_loc' :
                print('No table exist!')
                return
            vac_name = input('Enter vaccine name to be deleted: ')
            checkinput(vac_name)
            lst_col = ['vac_name']
            names = str(database.selectQuery(lst_col, table_name))
            if vac_name not in names:
                print('Vaccine name does not exits!')
                break
            database.deleteQuery (table_name, vac_name)
            print("Successfully deleted!")

        else :
            print("Incorrect input")
    
        val = input(" For adding vaccine name, date and place of manufacturing and date of expiry: \n Press 1 \n For adding vaccine name its availability and quantity: \n Press 2 \n To see vaccine name, date and place of manufacturing and date of expiry: \n Press 3 \n To see vaccine name its availability and quantity: \n Press "\
        "4 \n For updating vaccine manufacture and expiry\n Press 5\n For updating availability and quantity: \n Press 6\n For deleting any information: \n Press 7\n To exit, type exit: \n")

        if val == "exit" :
            sys.exit()
# unknown error:
# UPDATE aboutvac SET vac_detail= 'sfaf', vac_manufacture_place= 'fsgv', vac_manufacture_date= '2020-02-12', vac_expiry = '2020-02-30' WHERE vac_name = 'coromil';
# INSERT INTO vaccine_loc(vac_name, vac_cities, vac_startdate, vac_enddate, vac_quantity) VALUES ('zvd', 'zv', '2120-03-02', '2910-02-30', '3')

if __name__ == '__main__':
	main()