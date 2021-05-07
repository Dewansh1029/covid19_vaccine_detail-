import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dmysql@3010",
    database="covid"
)

mycursor = mydb.cursor()

def select_where(pass_lst, table_name, user_lst) :
    query = " SELECT " + str(pass_lst[0]) + " FROM " + table_name + " WHERE userid = '" + user_lst + "';"
    print(query)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def insertQuery (col_name, col_values, table_name):
    query = "INSERT INTO "
    query = query + table_name + "("
    icounter = len(col_name) - 1
    for items in col_name :
        if icounter != 0:
            query = query + items + ", "
        else :
            query = query + items + ") VALUES ("
        icounter = icounter - 1

    icounter = len(col_values) - 1
    for items in col_values :
        if icounter >0:
            query = query + "'" + items + "'" + ", "
        else :
            query = query + "'" + items + "'" + ")"
        icounter = icounter - 1
    print(query)
    mycursor.execute(query)
    mydb.commit()
    print("Successfully added!")

def selectQuery (lst_col,table_name):
    query = " SELECT "
    icounter = len(lst_col) - 1
    for item in lst_col:
        if icounter > 0:
            query = query + str(item) + " , "
        else:
            query = query + str(item)            
        icounter = icounter - 1
    query = query + " FROM " + table_name + ";"

    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult
    # for x in myresult:
    #     print(x)

# UPDATE `members` SET `full_names` = 'Janet Smith Jones', `physical_address` = 'Melrose 123' WHERE `membership_name` = 'abc';

def updateQuery (table_name, col_name, col_values, vac_name):
    if table_name != "vaccine_details" and table_name != "vaccine_loc" :
        return
    else :
        query = "UPDATE " + table_name + " SET "
        icounter = len(col_name) - 1
        for items in range (0, len(col_name)):
            if icounter > 0:
                query = query + col_name[items] + "= '" + col_values[items] + "', "
            else :
                query = query + col_name[items] + " = '" + col_values[items] + "' WHERE " + "vac_name" + " = '" + vac_name + "';" 
            icounter = icounter - 1
        mycursor.execute(query)
        mydb.commit()
        print("Successfully updated!")
    return

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
def deleteQuery (table_name, vac_name):
    query = "DELETE FROM " + table_name + " WHERE vac_name = '" + vac_name + "'"
    mycursor.execute(query)
    mydb.commit()

def show_single_row(vaccine_name) :
    query = "SELECT * FROM vaccine_details WHERE vac_name like '%" + vaccine_name + "%';"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def search_all_rows(name) :
    query = "select * from vaccine_details where vac_name like '%" + name + "%' or vac_detail like '%" + name + "%' or vac_manufacture_place like '%" + name + "%';"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult
# ALTER TABLE user_details MODIFY name varchar(30) NOT NULL