import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect("SmartRestaurant.db")
cursor = conn.cursor()


def print_all_from_pinaka(name):
    query = "SELECT * FROM " + name
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def tuple_to_list(list):
    return [item[0] for item in list]  # [(1,), (2,), (3,), ... -> [1, 2, 3, ...


# checks if username and password are valid
def check_user(myusername, mypassword):
    query = "SELECT username, password FROM PELATIS"
    cursor.execute(query)
    results = cursor.fetchall()
    if (myusername, mypassword) in results:
        return 1
    else:
        return 0


# insert new customer
def insert_user(name, lastname, phone, mail, username=None, password=None):
    query = "INSERT INTO PELATIS (onoma, eponimo, tilefono, email, username, password) VALUES(?,?,?,?,?,?)"
    cursor.execute(query, (name, lastname, phone, mail, username, password))
    conn.commit()


# inserts kritiki to database
def insert_kritiki(bathmologia, perigrafi, id_pelati):
    try:
        query = "INSERT INTO KRITIKI (id, bathmologia, perigrafi, imerominia, id_pelati) VALUES(NULL,?,?,?,?)"
        cursor.execute(query, (bathmologia, perigrafi, getdatetime(), id_pelati))
        conn.commit()
    except Exception as e:
        print("Error " + str(e))


# return kratisis for a given day
# Sto gui make sure days form 1-9 are given in 01-09 form
def kratisi_for_day(daytime):
    mylist = []
    query = "SELECT id_kratisis, imera_ora FROM KRATISI"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        if daytime == (row[1])[8:10]:
            mylist.append(row)
    counter = len(mylist)
    conn.close()

    return counter, mylist  # returns number of kratisis + the tuple imera+ora of kratisis for a given day

def get_all_food():
    query = "SELECT onoma FROM FAGITO"
    cursor.execute(query)
    results = cursor.fetchall()
    return [t[0] for t in results]


def get_all_drinks():
    query = "SELECT onoma FROM POTO"
    cursor.execute(query)
    results = cursor.fetchall()
    return [t[0] for t in results]

def get_all_trapezia():
    query = "SELECT id_trapeziou FROM TRAPEZI"
    cursor.execute(query)
    results = cursor.fetchall()
    return [t[0] for t in results]

def get_id_from_yliko(name):
    query = "SELECT onoma, id_ylikoy FROM YLIKA"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        if row[0] == name:
            return row[1]

def insert_paraggelia(id_trapeziou, id_ylikoy, id_potoy):
    cursor.execute('''
            INSERT INTO PERILAMBANEI (NULL, imer_ora, kostos, id_trapeziou)
            VALUES (?, ?, ?, ?)
        ''', id_trapeziou, id_ylikoy, id_potoy)
    cursor.execute('''
        INSERT INTO PARAGGELIA (NULL, imer_ora, kostos, id_trapeziou)
        VALUES (?, ?, ?, ?)
    ''', id_trapeziou, id_ylikoy, id_potoy)


def getdatetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# de douleuei
def delete_row_from_pinaka(table_name, id):
    try:
        cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (id,))
    except Exception as e:
        print("Error " + str(e))

    pass


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
