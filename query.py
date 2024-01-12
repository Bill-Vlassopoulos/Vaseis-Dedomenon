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


def get_onoma_from_id_fagitoy(id_fagitoy):
    cursor.execute('''
        SELECT onoma FROM FAGITO WHERE id_fagitoy = ?
    ''', (id_fagitoy,))
    return cursor.fetchone()[0]


def get_onoma_from_id_potoy(id_potoy):
    cursor.execute('''
        SELECT onoma FROM POTO WHERE id_potoy = ?
    ''', (id_potoy,))
    return cursor.fetchone()[0]


def get_id_from_yliko(name):
    query = "SELECT onoma, id_ylikoy FROM YLIKA"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        if row[0] == name:
            return row[1]


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
'''
insert_kratisi("1", "2024-01-01 20:00:00", "4", "a1")
insert_kratisi("2", "2024-01-01 20:00:00", "3", "a2")
insert_kratisi("3", "2024-01-01 21:00:00", "4", "a3")
insert_kratisi("4", "2024-01-01 21:00:00", "2", "a4")
insert_kratisi("7", "2024-01-02 20:00:00", "4", "a1")
insert_kratisi("8", "2024-01-02 20:00:00", "4", "b1")
insert_kratisi("10", "2024-01-02 20:00:00", "3", "b2")
insert_kratisi("12", "2024-01-02 21:00:00", "4", "b3")
insert_kratisi("1", "2024-02-01 20:00:00", "4", "a1")
'''


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

    return counter, mylist  # returns number of kratisis + the tuple imera+ora of kratisis for a given day


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


def delete_kratisi(id_pelati, id_kratisis):
    try:
        cursor.execute("DELETE FROM KANEI WHERE id_pelati = ? AND id_kratisis = ?", (id_pelati, id_kratisis))
        cursor.execute("DELETE FROM KRATISI WHERE id_kratisis = ?", (id_kratisis))
        conn.commit()
        print("Row deleted successfully")
    except sqlite3.Error as e:
        print(f"Error deleting row: {e}")

    conn.commit()


def insert_proion_to_perilambanei(id_paraggelias, id_fagitoy=None, id_potoy=None):
    cursor.execute('''
            INSERT INTO PERILAMBANEI (id_paraggelias, id_fagitoy, id_potoy, id_perilambanei)
            VALUES (?, ?, ?, NULL)
        ''', (id_paraggelias, id_fagitoy, id_potoy))
    conn.commit()


def calculate_kostos(id_paraggelias):
    kostos = 0
    cursor.execute('''
        SELECT id_fagitoy from PERILAMBANEI WHERE id_paraggelias = ?
    ''', (id_paraggelias,))
    food = tuple_to_list(cursor.fetchall())
    food = [item for item in food if item is not None]
    cursor.execute('''
            SELECT id_potoy from PERILAMBANEI WHERE id_paraggelias = ?
        ''', (id_paraggelias,))
    drinks = tuple_to_list(cursor.fetchall())
    drinks = [item for item in drinks if item is not None]

    for item in food:
        item = get_onoma_from_id_fagitoy(item)
        cursor.execute('''
            SELECT kostos from FAGITO
            WHERE onoma = ?
        ''', (item,))
        result = cursor.fetchone()
        if result is not None and result[0] is not None:
            kostos += float(result[0])

    for item in drinks:
        item = get_onoma_from_id_potoy(item)
        cursor.execute('''
            SELECT kostos from POTO
            WHERE onoma = ?
        ''', (item,))
        result = cursor.fetchone()
        if result is not None and result[0] is not None:
            kostos += float(result[0])
    print("Value: " + str(kostos))
    return str(kostos)


def insert_into_paraggelia(id_paraggelias, newfoods = None, newdrinks = None):
    if newfoods != None:
        for item in newfoods:
            insert_proion_to_perilambanei(id_paraggelias, get_id_from_fagito(item), None)
    if newdrinks != None:
        for item in newdrinks:
            insert_proion_to_perilambanei(id_paraggelias, None, get_id_from_poto(item))


def insert_paraggelia(id_trapeziou, food, drinks):
    imer_ora = getdatetime()
    cursor.execute('''
        INSERT INTO PARAGGELIA (id_paraggelias, imer_ora, kostos, id_trapeziou)
        VALUES (NULL, ?, ?, ?)
    ''', (imer_ora, None, id_trapeziou))
    conn.commit()
    id_paraggelias = cursor.lastrowid
    insert_into_paraggelia(id_paraggelias, food, drinks)


def get_id_paraggelias_from_trapezi(id_trapeziou):
    cursor.execute('''
        SELECT id_paraggelias from PARAGGELIA WHERE id_trapeziou = ?
    ''', (id_trapeziou,))
    return (cursor.fetchone())[0]


def delete_paraggelia(id_paraggelias):
    try:
        cursor.execute("DELETE FROM PARAGGELIA WHERE id_paraggelias = ? ", (id_paraggelias,))
        cursor.execute("DELETE FROM PERILAMBANEI WHERE id_paraggelias = ?", (id_paraggelias,))
        conn.commit()
        print("Row deleted successfully")
    except sqlite3.Error as e:
        print(f"Error deleting row: {e}")

    conn.commit()


# την καλεις οταν εχει τελειωσει η παραγγελια (αφου εχει γινει τυχον update)
def set_kostos_in_paraggelia(id_paraggelias):
    cursor.execute('''
        UPDATE PARAGGELIA SET kostos = ? WHERE id_paraggelias = ?
    ''', (calculate_kostos(id_paraggelias), id_paraggelias))
    conn.commit()


def delete_proion_from_perilambanei(id_paraggelias, id_fagitoy=None, id_potoy=None):
    try:
        cursor.execute('''
                DELETE FROM PERILAMBANEI WHERE id_paraggelias = ? AND id_fagitoy = ? AND id_potoy = ?
            ''', (id_paraggelias, id_fagitoy, id_potoy))
        conn.commit()
    except Exception as e:
        print("Error: " + str(e))


def remove_from_paraggelia(id_paraggelias, delfoods = None, deldrinks = None):
    if delfoods !=None:
        for item in delfoods:
            delete_proion_from_perilambanei(id_paraggelias, get_id_from_fagito(item))
    if deldrinks!= None:
        for item in deldrinks:
            delete_proion_from_perilambanei(id_paraggelias, None, get_id_from_poto(item))

remove_from_paraggelia("14", ["Fries"])
