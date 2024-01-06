import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect("SmartRestaurant.db")
cursor = conn.cursor()


# return kratisis for a given day
# Sto gui make sure days form 1-9 are given in 01-09 form
def kratisi_for_day(daytime):
    mylist = []
    query = "SELECT id_kratisis, imera_ora FROM KRATISI"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
        if day == int((row[1])[8:10]):
            mylist.append(row)
    counter = len(mylist)
    conn.close()

    return counter, list  # returns number of kratisis + the tuple of kratisis for a given day


def tuple_to_list(list):
    return [item[0] for item in list]  # [(1,), (2,), (3,), ... -> [1, 2, 3, ...


# checks if username and password are valid
def check_user(myusername, mypassword):
    query = "SELECT username, password FROM PELATIS"
    cursor.execute(query)
    results = cursor.fetchall()
    pass
    # check if input parameters match results


# insert new customer
def insert_user(name, lastname, phone, mail):
    query = "INSERT INTO PELATIS (onoma, eponimo, tilefono, email) VALUES(?,?,?,?)"
    cursor.execute(query, (name, lastname, phone, mail))
    conn.commit()


def print_all_from_pinaka(name):
    query = "SELECT * FROM " + name
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def getdatetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def insert_kritiki(bathmologia, perigrafi, id_pelati):
    query = "INSERT INTO KRITIKI (id, bathmologia, perigrafi, imerominia, id_pelati) VALUES(NULL,?,?,?,?)"
    cursor.execute(query, (bathmologia, perigrafi, getdatetime(), id_pelati))
    conn.commit()

def delete_row_from_pinaka(linenumber, name):
    try:



'''
# returns all tables
def all_id_tables():
    query = "SELECT id_trapeziou FROM TRAPEZI"
    cursor.execute(query)
    results = (cursor.fetchall())    
    print(tuple_to_list(results))    
    
    
    def all_thesi_tables():
    query = "SELECT thesi FROM TRAPEZI"
    cursor.execute(query)
    results = (cursor.fetchall())
    print(tuple_to_list(results))
'''
