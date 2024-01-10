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


def getdatetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


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


def get_all_tables():
    return ['a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5']


def get_id_from_fagito(name):
    query = "SELECT onoma, id_fagitoy FROM FAGITO"
    cursor.execute(query)
    results = cursor.fetchall()
    try:
        for row in results:
            if row[0] == name:
                return row[1]
    except Exception as e:
        print("Error " + str(e))


def get_id_from_poto(name):
    query = "SELECT onoma, id_potoy FROM POTO"
    cursor.execute(query)
    results = cursor.fetchall()
    try:
        for row in results:
            if row[0] == name:
                return row[1]
    except Exception as e:
        print("Error " + str(e))


def get_id_from_yliko(name):
    query = "SELECT onoma, id_ylikoy FROM YLIKA"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        if row[0] == name:
            return row[1]


def insert_kratisi(id_pelati, imera_ora, arithmos_atomon, id_trapeziou):
    cursor.execute('''
        INSERT INTO KRATISI(id_kratisis, imera_ora, arithmos_atomon, id_trapeziou)
        VALUES(NULL,?,?, ?)
    ''', (imera_ora, arithmos_atomon, id_trapeziou))
    conn.commit()

    cursor.execute('''
        SELECT id_kratisis
        FROM KRATISI
        ORDER BY id_kratisis DESC
        LIMIT 1;
    ''')
    result = cursor.fetchone()
    id_kratisis = result[0]
    cursor.execute('''
        INSERT INTO KANEI(id_pelati, id_kratisis)
        VALUES(?,?)
            ''', (id_pelati, id_kratisis))
    conn.commit()


# ta dedomena auta ta trexeis mia fora mono:)
'''insert_kratisi("1", "2024-01-01 20:00:00", "4", "a1")
insert_kratisi("2", "2024-01-01 20:00:00", "3", "a2")
insert_kratisi("3", "2024-01-01 21:00:00", "4", "a3")
insert_kratisi("4", "2024-01-01 21:00:00", "2", "a4")
insert_kratisi("7", "2024-01-02 20:00:00", "4", "a1")
insert_kratisi("8", "2024-01-02 20:00:00", "4", "b1")
insert_kratisi("10", "2024-01-02 20:00:00", "3", "b2")
insert_kratisi("12", "2024-01-02 21:00:00", "4", "b3")
insert_kratisi("1", "2024-02-01 20:00:00", "4", "a1")'''


def insert_proion_to_perilambanei(id_paraggelias, id_fagitoy=None, id_potoy=None):
    cursor.execute('''
            INSERT INTO PERILAMBANEI (id_paraggelias, id_fagitoy, id_potoy, id_perilambanei)
            VALUES (?, ?, ?, NULL)
        ''', (id_paraggelias, id_fagitoy, id_potoy))
    conn.commit()


# enter date+ time, get tables that are free for that time
def free_tables(date, time):
    free_table_list = get_all_tables()
    date_time = date + " " + time
    cursor.execute(
        '''
        SELECT id_trapeziou, imera_ora FROM KRATISI
        '''
    )
    results = cursor.fetchall()

    for row in results:
        if date_time == (row[1])[8:]:
            if row[0] in free_table_list:
                try:
                    free_table_list.remove(row[0])
                except:
                    pass

    return free_table_list


def get_kratisi_from_pelati(id_pelati):
    cursor.execute('''
            SELECT KANEI.id_pelati, KANEI.id_kratisis, KRATISI.imera_ora
            FROM KANEI
            INNER JOIN KRATISI ON KANEI.id_kratisis = KRATISI.id_kratisis
            WHERE KANEI.id_pelati = ?
        ''', (id_pelati,))

    results = cursor.fetchall()
    # mexri edw epistrefei oles tis kratisis  apo pelati

    for row in results:
        if row[2] < getdatetime():
            results.remove(row)

    return results  # returns tuple (id_pelati, id_kratisi, imerominia kratisis > currentdatetime)


def calculate_kostos(food, drinks):
    kostos = 0
    for item in food:
        cursor.execute('''
            SELECT kostos from FAGITO
            WHERE onoma = ?
        ''', (item,))
        result = cursor.fetchone()
        if result is not None and result[0] is not None:
            kostos += float(result[0])

    for item in drinks:
        cursor.execute('''
            SELECT kostos from POTO
            WHERE onoma = ?
        ''', (item,))
        result = cursor.fetchone()
        if result is not None and result[0] is not None:
            kostos += float(result[0])
    print("Value: " + str(kostos))
    return str(kostos)


calculate_kostos(["Greek salad", "Fries"], ["Iced Tea", "Water"])


def insert_paraggelia(id_trapeziou, food, drinks):
    kostos = calculate_kostos(food, drinks)
    imer_ora = getdatetime()
    cursor.execute('''
        INSERT INTO PARAGGELIA (id_paraggelias, imer_ora, kostos, id_trapeziou)
        VALUES (NULL, ?, ?, ?)
    ''', (imer_ora, kostos, id_trapeziou))
    conn.commit()
    id_paraggelias = cursor.lastrowid
    for item in food:
        insert_proion_to_perilambanei(id_paraggelias, get_id_from_fagito(item))
    for item in drinks:
        insert_proion_to_perilambanei(id_paraggelias, None, get_id_from_poto(item))


