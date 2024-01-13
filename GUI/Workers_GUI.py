import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.sip import voidptr
from datetime import datetime, timedelta
import sqlite3

conn = sqlite3.connect("SmartRestaurant.db")
cursor = conn.cursor()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        main_vbox = QVBoxLayout()
        self.setWindowTitle("Estiatorio")
        self.setGeometry(300, 300, 450, 450)
        self.setFixedSize(450, 450)
        self.kratiseis_btn = QPushButton("Κρατήσεις")
        self.kratiseis_btn.clicked.connect(self.open_kratiseis)

        self.new_paraggelia_btn = QPushButton("Νέα Παραγγελία")
        self.new_paraggelia_btn.clicked.connect(self.open_new_paraggelia)

        self.edit_paraggelia_btn = QPushButton(
            "Διαχείριση Παραγγελίας/Κόστος Παραγγελίας"
        )
        self.edit_paraggelia_btn.clicked.connect(self.open_paraggelia_edit)

        self.paradotea_piata_pota_btn = QPushButton("Πιάτα/Ποτά προς παράδοση")
        self.paradotea_piata_pota_btn.clicked.connect(self.open_paradotea_pp)

        main_vbox.addWidget(self.kratiseis_btn)
        main_vbox.addWidget(self.new_paraggelia_btn)
        main_vbox.addWidget(self.edit_paraggelia_btn)
        main_vbox.addWidget(self.paradotea_piata_pota_btn)
        self.setLayout(main_vbox)

    def open_kratiseis(self):
        self.krat = Kratiseis()
        self.krat.show()

    def open_new_paraggelia(self):
        self.parag = Paraggelies()
        self.parag.show()

    def open_paraggelia_edit(self):
        self.parag_edit = Paraggelia_Management()
        self.parag_edit.show()

    def open_paradotea_pp(self):
        self.paradotea_pp = Pros_Paradosi()
        self.paradotea_pp.show()


class Paraggelies(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)
        main_vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        down_right_vbox = QVBoxLayout()
        down_hbox = QHBoxLayout()
        left_vbox = QVBoxLayout()
        right_vbox = QVBoxLayout()
        self.fagita = QListWidget()
        self.pota = QListWidget()
        self.menu_creation()
        self.trapezi_cmb = QComboBox()
        self.gettables()
        trapezi_label = QLabel("Eπιλέξτε Τραπέζι:")
        piata_label = QLabel("Επιλέξτε Πιάτα:")
        pota_label = QLabel("Επιλέξτε Ποτά:")
        self.ypovoli_trapeziou = QPushButton("Επιλογή Τραπεζιού")
        self.ypovoli_trapeziou.clicked.connect(self.new_paraggelia)
        add_food_btn = QPushButton("Προσθήκη Πιάτου")
        add_food_btn.clicked.connect(self.add_food)
        add_drink_btn = QPushButton("Προσθήκη Ποτού")
        add_drink_btn.clicked.connect(self.add_poto)
        ypovoli_btn = QPushButton("Υποβολή Παραγγελίας")
        delete_btn = QPushButton("Διαγραφή Προιόντος")
        delete_btn.clicked.connect(self.delete_proion)
        self.kratiseis_table = QTableWidget()
        self.kratiseis_table.setRowCount(3)
        self.kratiseis_table.setColumnCount(2)
        self.kratiseis_table.setHorizontalHeaderLabels(["Όνομα", "Κόστος"])

        left_vbox.addWidget(piata_label)
        left_vbox.addWidget(self.fagita)
        left_vbox.addStretch()

        right_vbox.addWidget(pota_label)
        right_vbox.addWidget(self.pota)
        right_vbox.addStretch()

        hbox.addLayout(left_vbox)
        hbox.addStretch()
        hbox.addLayout(right_vbox)

        down_right_vbox.addWidget(trapezi_label)
        down_right_vbox.addWidget(self.trapezi_cmb)
        down_right_vbox.addWidget(self.ypovoli_trapeziou)
        down_right_vbox.addWidget(add_food_btn)
        down_right_vbox.addWidget(add_drink_btn)
        down_right_vbox.addWidget(delete_btn)
        # down_right_vbox.addWidget(ypovoli_btn)
        down_right_vbox.addStretch()
        down_hbox.addWidget(self.kratiseis_table)
        down_hbox.addLayout(down_right_vbox)
        main_vbox.addLayout(hbox)
        main_vbox.addLayout(down_hbox)
        self.setLayout(main_vbox)

    def menu_creation(self):
        query = "select onoma from FAGITO "
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            self.fagita.addItem(row[0])

        query = "select onoma from POTO "
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            self.pota.addItem(row[0])

    def gettables(self):
        query = "SELECT id_trapeziou FROM TRAPEZI"
        cursor.execute(query)
        results = cursor.fetchall()
        list = [t[0] for t in results]
        self.trapezi_cmb.addItems(list)

    def new_paraggelia(self):
        query = "insert into PARAGGELIA(imer_ora,kostos,id_trapeziou) VALUES (?, ?, ?)"

        cursor.execute(query, (getdatetime(), 0.01, self.trapezi_cmb.currentText()))
        conn.commit()

        query = "select id_paraggelias from PARAGGELIA order by id_paraggelias DESC limit 1;"
        cursor.execute(query)
        results = cursor.fetchone()
        self.id_paraggelias = results[0]

    def add_food(self):
        self.food_name = self.fagita.currentItem().text()
        query = "SELECT id_fagitoy FROM FAGITO WHERE onoma='{}'".format(self.food_name)
        cursor.execute(query)
        results = cursor.fetchone()
        self.id_fagitoy = results[0]

        cursor.execute(
            """
            INSERT INTO PERILAMBANEI (id_paraggelias, id_fagitoy, id_potoy, id_perilambanei)
            VALUES (?, ?, NULL, NULL)
        """,
            (self.id_paraggelias, self.id_fagitoy),
        )
        conn.commit()
        self.set_table_data()

    def add_poto(self):
        self.poto_name = self.pota.currentItem().text()
        query = "SELECT id_potoy FROM POTO WHERE onoma='{}'".format(self.poto_name)
        cursor.execute(query)
        results = cursor.fetchall()
        self.id_potoy = results[0][0]

        cursor.execute(
            """
            INSERT INTO PERILAMBANEI (id_paraggelias, id_fagitoy, id_potoy, id_perilambanei)
            VALUES (?, NULL, ?, NULL)
        """,
            (self.id_paraggelias, self.id_potoy),
        )
        conn.commit()
        self.set_table_data()

    def set_table_data(self):
        self.kratiseis_table.clearContents()
        self.kratiseis_table.setRowCount(0)

        # Εκτελέστε το κατάλληλο SQL ερώτημα για να πάρετε τα δεδομένα από τη βάση
        cursor.execute(
            """
            SELECT onoma, kostos
            FROM FAGITO
            JOIN PERILAMBANEI ON FAGITO.id_fagitoy = PERILAMBANEI.id_fagitoy
            WHERE id_paraggelias = ?
            UNION ALL
            SELECT onoma,kostos
            FROM POTO
            JOIN PERILAMBANEI ON POTO.id_potoy = PERILAMBANEI.id_potoy 
            WHERE id_paraggelias = ?;
            """,
            (self.id_paraggelias, self.id_paraggelias),
        )

        # Πάρτε όλα τα αποτελέσματα
        results = cursor.fetchall()

        # Ορίστε τον αριθμό των γραμμών του πίνακα
        self.kratiseis_table.setRowCount(len(results))

        for row_index, row_data in enumerate(results):
            onoma, kostos = row_data

            # Προσθέστε τα δεδομένα σε κάθε κελί του πίνακα
            self.kratiseis_table.setItem(row_index, 0, QTableWidgetItem(str(onoma)))
            self.kratiseis_table.setItem(
                row_index, 1, QTableWidgetItem(str(kostos) + "0€")
            )

    def delete_proion(self):
        selected_row = self.kratiseis_table.currentRow()

        if selected_row >= 0:
            # Get the name of the item to be deleted
            item_name = self.kratiseis_table.item(selected_row, 0).text()
            # Delete the item from the database or perform other necessary actions
            # ...
            query = "select id_fagitoy from FAGITO where onoma=?"
            cursor.execute(query, (item_name,))
            results_food = cursor.fetchall()

            query = "select id_potoy from POTO where onoma=?"
            cursor.execute(query, (item_name,))
            results_drink = cursor.fetchall()

            if not results_food:
                cursor.execute(
                    """
                SELECT id_perilambanei FROM PERILAMBANEI WHERE id_paraggelias = ? AND id_potoy = ? LIMIT 1;
            """,
                    (self.id_paraggelias, results_drink[0][0]),
                )
                results = cursor.fetchone()
                self.id_perilambanei = results[0]

            else:
                cursor.execute(
                    """
                SELECT id_perilambanei FROM PERILAMBANEI WHERE id_paraggelias = ? AND id_fagitoy = ?  LIMIT 1;
            """,
                    (self.id_paraggelias, results_food[0][0]),
                )

                results = cursor.fetchone()
                self.id_perilambanei = results[0]

            cursor.execute(
                "delete from PERILAMBANEI where id_perilambanei=?",
                (self.id_perilambanei,),
            )
            conn.commit()
            # Remove the selected row from the QTableWidget
            self.kratiseis_table.removeRow(selected_row)
            self.set_table_data()


class Paraggelia_Management(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)
        main_vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        down_right_vbox = QVBoxLayout()
        down_hbox = QHBoxLayout()
        left_vbox = QVBoxLayout()
        right_vbox = QVBoxLayout()
        self.fagita = QListWidget()
        self.pota = QListWidget()
        self.menu_creation()
        self.trapezi_cmb = QComboBox()
        self.trapezi_cmb.activated.connect(self.open_paraggelia)
        trapezi_label = QLabel("Eπιλέξτε Τραπέζι:")
        piata_label = QLabel("Επιλέξτε Πιάτα:")
        kostos_label = QLabel("Τελικό Κόστος:")
        self.gettables()
        self.kostos_line_edit = QLineEdit()
        self.kostos_line_edit.setFixedSize(80, 40)
        pota_label = QLabel("Επιλέξτε Ποτά:")
        add_food_btn = QPushButton("Προσθήκη Πιάτου")
        add_food_btn.clicked.connect(self.add_food)
        add_drink_btn = QPushButton("Προσθήκη Ποτού")
        add_drink_btn.clicked.connect(self.add_poto)
        ypovoli_btn = QPushButton("Ανανέωση Παραγγελίας")
        delete_btn = QPushButton("Διαγραφή Προιόντος")
        delete_btn.clicked.connect(self.delete_proion)
        self.kratiseis_table = QTableWidget()
        self.kratiseis_table.setRowCount(3)
        self.kratiseis_table.setColumnCount(2)
        self.kratiseis_table.setHorizontalHeaderLabels(["Όνομα", "Κόστος"])

        left_vbox.addWidget(piata_label)
        left_vbox.addWidget(self.fagita)
        left_vbox.addStretch()

        right_vbox.addWidget(pota_label)
        right_vbox.addWidget(self.pota)
        right_vbox.addStretch()

        hbox.addLayout(left_vbox)
        hbox.addStretch()
        hbox.addLayout(right_vbox)

        down_right_vbox.addWidget(trapezi_label)
        down_right_vbox.addWidget(self.trapezi_cmb)
        down_right_vbox.addWidget(add_food_btn)
        down_right_vbox.addWidget(add_drink_btn)
        down_right_vbox.addWidget(delete_btn)
        down_right_vbox.addWidget(ypovoli_btn)
        down_right_vbox.addStretch()
        down_right_vbox.addWidget(kostos_label)
        down_right_vbox.addWidget(self.kostos_line_edit)

        down_hbox.addWidget(self.kratiseis_table)
        down_hbox.addLayout(down_right_vbox)
        main_vbox.addLayout(hbox)
        main_vbox.addLayout(down_hbox)
        self.setLayout(main_vbox)

    def menu_creation(self):
        query = "select onoma from FAGITO "
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            self.fagita.addItem(row[0])

        query = "select onoma from POTO "
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            self.pota.addItem(row[0])

    def gettables(self):
        query = "SELECT id_trapeziou FROM TRAPEZI"
        cursor.execute(query)
        results = cursor.fetchall()
        list = [t[0] for t in results]
        self.trapezi_cmb.addItems(list)

    def set_table_data(self):
        self.kratiseis_table.clearContents()
        self.kratiseis_table.setRowCount(0)

        # Εκτελέστε το κατάλληλο SQL ερώτημα για να πάρετε τα δεδομένα από τη βάση
        cursor.execute(
            """
            SELECT onoma, kostos
            FROM FAGITO
            JOIN PERILAMBANEI ON FAGITO.id_fagitoy = PERILAMBANEI.id_fagitoy
            WHERE id_paraggelias = ?
            UNION ALL
            SELECT onoma,kostos
            FROM POTO
            JOIN PERILAMBANEI ON POTO.id_potoy = PERILAMBANEI.id_potoy 
            WHERE id_paraggelias = ?;
            """,
            (self.id_paraggelias, self.id_paraggelias),
        )

        # Πάρτε όλα τα αποτελέσματα
        results = cursor.fetchall()

        # Ορίστε τον αριθμό των γραμμών του πίνακα
        self.kratiseis_table.setRowCount(len(results))

        for row_index, row_data in enumerate(results):
            onoma, kostos = row_data

            # Προσθέστε τα δεδομένα σε κάθε κελί του πίνακα
            self.kratiseis_table.setItem(row_index, 0, QTableWidgetItem(str(onoma)))
            self.kratiseis_table.setItem(
                row_index, 1, QTableWidgetItem(str(kostos) + "0€")
            )
        self.calc_cost()

    def open_paraggelia(self):
        self.id_trapeziou = self.trapezi_cmb.currentText()
        query = "select id_paraggelias from paraggelia where id_trapeziou=? order by imer_ora DESC limit 1;"
        cursor.execute(query, (self.id_trapeziou,))
        results = cursor.fetchone()
        self.id_paraggelias = results[0]
        self.set_table_data()

    def add_food(self):
        self.food_name = self.fagita.currentItem().text()
        query = "SELECT id_fagitoy FROM FAGITO WHERE onoma='{}'".format(self.food_name)
        cursor.execute(query)
        results = cursor.fetchone()
        self.id_fagitoy = results[0]

        cursor.execute(
            """
            INSERT INTO PERILAMBANEI (id_paraggelias, id_fagitoy, id_potoy, id_perilambanei)
            VALUES (?, ?, NULL, NULL)
        """,
            (self.id_paraggelias, self.id_fagitoy),
        )
        conn.commit()
        self.set_table_data()

    def add_poto(self):
        self.poto_name = self.pota.currentItem().text()
        query = "SELECT id_potoy FROM POTO WHERE onoma='{}'".format(self.poto_name)
        cursor.execute(query)
        results = cursor.fetchall()
        self.id_potoy = results[0][0]

        cursor.execute(
            """
            INSERT INTO PERILAMBANEI (id_paraggelias, id_fagitoy, id_potoy, id_perilambanei)
            VALUES (?, NULL, ?, NULL)
        """,
            (self.id_paraggelias, self.id_potoy),
        )
        conn.commit()
        self.set_table_data()

    def delete_proion(self):
        selected_row = self.kratiseis_table.currentRow()

        if selected_row >= 0:
            # Get the name of the item to be deleted
            item_name = self.kratiseis_table.item(selected_row, 0).text()
            # Delete the item from the database or perform other necessary actions
            # ...
            query = "select id_fagitoy from FAGITO where onoma=?"
            cursor.execute(query, (item_name,))
            results_food = cursor.fetchall()

            query = "select id_potoy from POTO where onoma=?"
            cursor.execute(query, (item_name,))
            results_drink = cursor.fetchall()

            if not results_food:
                cursor.execute(
                    """
                SELECT id_perilambanei FROM PERILAMBANEI WHERE id_paraggelias = ? AND id_potoy = ? LIMIT 1;
            """,
                    (self.id_paraggelias, results_drink[0][0]),
                )
                results = cursor.fetchone()
                self.id_perilambanei = results[0]

            else:
                cursor.execute(
                    """
                SELECT id_perilambanei FROM PERILAMBANEI WHERE id_paraggelias = ? AND id_fagitoy = ?  LIMIT 1;
            """,
                    (self.id_paraggelias, results_food[0][0]),
                )

                results = cursor.fetchone()
                self.id_perilambanei = results[0]

            cursor.execute(
                "delete from PERILAMBANEI where id_perilambanei=?",
                (self.id_perilambanei,),
            )
            conn.commit()
            # Remove the selected row from the QTableWidget
            self.kratiseis_table.removeRow(selected_row)
            self.set_table_data()

    def tuple_to_list(self, list):
        return [item[0] for item in list]

    def get_onoma_from_id_fagitoy(self, id_fagitoy):
        cursor.execute(
            """
            SELECT onoma FROM FAGITO WHERE id_fagitoy = ?
        """,
            (id_fagitoy,),
        )
        return cursor.fetchone()[0]

    def get_onoma_from_id_potoy(self, id_potoy):
        cursor.execute(
            """
            SELECT onoma FROM POTO WHERE id_potoy = ?
        """,
            (id_potoy,),
        )
        return cursor.fetchone()[0]

    def calc_cost(self):
        kostos = 0
        cursor.execute(
            """
            SELECT id_fagitoy from PERILAMBANEI WHERE id_paraggelias = ?
        """,
            (self.id_paraggelias,),
        )
        food = self.tuple_to_list(cursor.fetchall())
        food = [item for item in food if item is not None]
        cursor.execute(
            """
                SELECT id_potoy from PERILAMBANEI WHERE id_paraggelias = ?
            """,
            (self.id_paraggelias,),
        )
        drinks = self.tuple_to_list(cursor.fetchall())
        drinks = [item for item in drinks if item is not None]

        for item in food:
            item = self.get_onoma_from_id_fagitoy(item)
            cursor.execute(
                """
                SELECT kostos from FAGITO
                WHERE onoma = ?
            """,
                (item,),
            )
            result = cursor.fetchone()
            if result is not None and result[0] is not None:
                kostos += float(result[0])

        for item in drinks:
            item = self.get_onoma_from_id_potoy(item)
            cursor.execute(
                """
                SELECT kostos from POTO
                WHERE onoma = ?
            """,
                (item,),
            )
            result = cursor.fetchone()
            if result is not None and result[0] is not None:
                kostos += float(result[0])
        print("Value: " + str(kostos))
        self.kostos_line_edit.setText(str(kostos) + "€")


class Pros_Paradosi(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)
        main_hbox = QHBoxLayout()
        left_vbox = QVBoxLayout()
        right_vbox = QVBoxLayout()

        self.fagito_table = QTableWidget()
        self.fagito_table.setRowCount(3)
        self.fagito_table.setColumnCount(3)
        self.fagito_table.setHorizontalHeaderLabels(["Όνομα", "Ποσότητα", "Τραπέζι"])

        self.poto_table = QTableWidget()
        self.poto_table.setRowCount(3)
        self.poto_table.setColumnCount(3)
        self.poto_table.setHorizontalHeaderLabels(["Όνομα", "Ποσότητα", "Τραπέζι"])

        fagito_Label = QLabel("Πιάτα προς παράδοση:")
        drink_Label = QLabel("Ποτά προς παράδοση:")

        dish_delivered = QPushButton("Το πιάτο παραδόθηκε")
        drink_delivered = QPushButton("Το πoτό παραδόθηκε")

        left_vbox.addWidget(fagito_Label)
        left_vbox.addWidget(self.fagito_table)
        left_vbox.addWidget(dish_delivered)

        right_vbox.addWidget(drink_Label)
        right_vbox.addWidget(self.poto_table)
        right_vbox.addWidget(drink_delivered)

        main_hbox.addLayout(left_vbox)
        main_hbox.addLayout(right_vbox)

        self.setLayout(main_hbox)


class Kratiseis(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(650, 650)
        vbox = QVBoxLayout()
        main_vbox = QVBoxLayout()
        down_hbox = QHBoxLayout()
        down_right_vbox = QVBoxLayout()
        self.date = QComboBox(self)
        self.people = QComboBox(self)
        self.date.addItems(self.load_dates())
        self.tables = QComboBox(self)
        self.tables.addItems(self.gettables())
        self.tables.activated.connect(self.people_numbers_limit)
        self.name = QLineEdit()
        self.surname = QLineEdit()
        self.tilefono = QLineEdit()
        self.ypovoli_btn = QPushButton("Υποβολή Κράτησης")
        self.akyrosi_btn = QPushButton("Ακύρωση Κράτησης")
        self.ora_afixis = QComboBox(self)
        self.ora_afixis.addItems(self.gettimes())
        self.ypovoli_btn.clicked.connect(self.ypovoli_kratisis)
        self.akyrosi_btn.clicked.connect(self.delete_kratisi)
        self.kratiseis_table = QTableWidget()
        self.kratiseis_table.setRowCount(3)
        self.kratiseis_table.setColumnCount(5)
        self.kratiseis_table.setHorizontalHeaderLabels(
            ["Τραπέζι", "Ημερομηνία", "Άτομα", "Όνομα", "Επώνυμο"]
        )
        self.get_kratiseis()
        vbox.addWidget(QLabel("Επιλέξτε Ημερομηνία:"))
        vbox.addWidget(self.date)
        vbox.addWidget(QLabel("Επιλέξτε Τραπέζι:"))
        vbox.addWidget(self.tables)
        vbox.addWidget(QLabel("Επιλέξτε Αριθμό Ατόμων:"))
        vbox.addWidget(self.people)
        vbox.addWidget(QLabel("Επιλέξτε Ώρα Κράτησης:"))
        vbox.addWidget(self.ora_afixis)
        vbox.addWidget(QLabel("Δώστε το όνομα σας:"))
        vbox.addWidget(self.name)
        vbox.addWidget(QLabel("Δώστε το επίθετο σας:"))
        vbox.addWidget(self.surname)
        vbox.addWidget(QLabel("Δώστε το τηλέφωνο σας:"))
        vbox.addWidget(self.tilefono)

        vbox.addStretch()

        down_right_vbox.addStretch()
        down_right_vbox.addWidget(self.ypovoli_btn)
        down_right_vbox.addWidget(self.akyrosi_btn)
        down_right_vbox.addStretch()

        down_hbox.addWidget(self.kratiseis_table)
        down_hbox.addLayout(down_right_vbox)
        main_vbox.addLayout(vbox)
        main_vbox.addLayout(down_hbox)
        self.setLayout(main_vbox)

    def load_dates(self):
        today = datetime.now()

        # Δημιουργία λίστας με τις επόμενες 10 ημέρες ως συμβολοσειρές (εξαιρώντας τις Δευτέρες)
        next_10_days = [
            (today + timedelta(days=x)).strftime("%Y-%m-%d")
            for x in range(0, 10)
            if (today + timedelta(days=x)).weekday() != 0
        ]
        return next_10_days

    def gettables(self):
        query = "SELECT id_trapeziou FROM TRAPEZI"
        cursor.execute(query)
        results = cursor.fetchall()
        list = [t[0] for t in results]
        return list

    def people_numbers_limit(self):
        query = "select aritmos_theseon from TRAPEZI where id_trapeziou='{}'".format(
            self.tables.currentText()
        )
        cursor.execute(query)
        results = cursor.fetchall()
        self.people.clear()
        for i in range(1, results[0][0] + 1):
            self.people.addItem(str(i))

    def get_kratiseis(self):
        self.kratiseis_table.clearContents()
        self.kratiseis_table.setRowCount(0)

        query = """SELECT KRATISI.id_trapeziou, KRATISI.imera_ora, KRATISI.aritmos_atomon, PELATIS.onoma, PELATIS.eponimo 
        FROM PELATIS
        JOIN KANEI ON PELATIS.id_pelati = KANEI.id_pelati
        JOIN KRATISI ON KRATISI.id_kratisis = KANEI.id_kratisis
        WHERE KRATISI.imera_ora > ?"""
        cursor.execute(query, (getdatetime(),))
        results = cursor.fetchall()

        # Ορίστε τον αριθμό των γραμμών του πίνακα
        self.kratiseis_table.setRowCount(len(results))

        for row_index, row_data in enumerate(results):
            id_trapeziou, imera_ora, aritmos_atomon, onoma, epitheto = row_data

            # Προσθέστε τα δεδομένα σε κάθε κελί του πίνακα
            self.kratiseis_table.setItem(
                row_index, 0, QTableWidgetItem(str(id_trapeziou))
            )
            self.kratiseis_table.setItem(row_index, 1, QTableWidgetItem(str(imera_ora)))
            self.kratiseis_table.setItem(
                row_index, 2, QTableWidgetItem(str(aritmos_atomon))
            )
            self.kratiseis_table.setItem(row_index, 3, QTableWidgetItem(str(onoma)))
            self.kratiseis_table.setItem(row_index, 4, QTableWidgetItem(str(epitheto)))

    def ypovoli_kratisis(self):
        cursor.execute(
            "INSERT INTO PELATIS(onoma,eponimo,tilefono,email,username,password) VALUES(?,?,?,NULL,NULL,NULL)",
            (self.name.text(), self.surname.text(), self.tilefono.text()),
        )
        conn.commit()
        cursor.execute("SELECT id_pelati FROM PELATIS ORDER BY id_pelati DESC LIMIT 1;")
        results = cursor.fetchone()
        self.id_pelati = results[0]

        cursor.execute(
            """INSERT INTO KRATISI(imera_ora,aritmos_atomon,id_trapeziou) VALUES(?,?,?)
""",
            (
                self.date.currentText() + " " + self.ora_afixis.currentText() + ":00",
                int(self.people.currentText()),
                self.tables.currentText(),
            ),
        )
        conn.commit()

        cursor.execute(
            """
        SELECT id_kratisis
        FROM KRATISI
        ORDER BY id_kratisis DESC
        LIMIT 1;
    """
        )
        result = cursor.fetchone()
        id_kratisis = result[0]
        cursor.execute(
            """
            INSERT INTO KANEI(id_pelati, id_kratisis)
            VALUES(?,?)
                """,
            (self.id_pelati, id_kratisis),
        )
        conn.commit()
        self.get_kratiseis()

    def delete_kratisi(self):
        selected_row = self.kratiseis_table.currentRow()
        if selected_row >= 0:
            # Ανακτήστε τα δεδομένα της επιλεγμένης γραμμής
            id_trapeziou = self.kratiseis_table.item(selected_row, 0).text()
            imera_ora = self.kratiseis_table.item(selected_row, 1).text()
            aritmos_atomon = self.kratiseis_table.item(selected_row, 2).text()

            # Εδώ μπορείτε να προσθέσετε τον κώδικα για τη διαγραφή της επιλεγμένης γραμμής από τη βάση δεδομένων
            query = "select id_kratisis from kratisi where id_trapeziou='{}' AND imera_ora='{}' AND aritmos_atomon={}".format(
                id_trapeziou, imera_ora, aritmos_atomon
            )
            cursor.execute(query)
            results = cursor.fetchall()
            id_kratisis = results[0][0]

            query = "delete from KANEI where id_kratisis={}".format(id_kratisis)
            cursor.execute(query)
            conn.commit()

            query = "delete from KRATISI where id_kratisis={}".format(id_kratisis)
            cursor.execute(query)
            conn.commit()
            # Ενημερώστε τον πίνακα εκ νέου
            self.get_kratiseis()

    def gettimes(self):
        return ["19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00"]


def getdatetime():
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime


class Mageiras(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(650, 650)
        vbox = QVBoxLayout()
        pros_paradosi_btn = QPushButton("Πιάτα έτοιμα προς παράδοση")
        pros_paradosi_btn.clicked.connect(self.open_etoima_piata)
        katagrafi_ylikon_btn = QPushButton("Καταγραφή Υλικών")
        katagrafi_ylikon_btn.clicked.connect(self.open_inventory_update)
        vbox.addWidget(pros_paradosi_btn)
        vbox.addWidget(katagrafi_ylikon_btn)
        self.setLayout(vbox)

    def open_etoima_piata(self):
        self.et_pt = Etoima_Piata()
        self.et_pt.show()

    def open_inventory_update(self):
        self.invet = Ylika_Update()
        self.invet.show()


class Etoima_Piata(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(650, 650)
        vbox = QVBoxLayout()
        self.fagito_table = QTableWidget()
        self.fagito_table.setRowCount(3)
        self.fagito_table.setColumnCount(3)
        self.fagito_table.setHorizontalHeaderLabels(["Όνομα", "Ποσότητα", "Τραπέζι"])
        piato_pros_paradosi_btn = QPushButton("Πιάτο έτοιμο προς παράδοση")
        vbox.addWidget(self.fagito_table)
        vbox.addWidget(piato_pros_paradosi_btn)
        self.setLayout(vbox)


class Ylika_Update(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350, 350)
        vbox = QVBoxLayout()
        ylika_cmb = QComboBox()
        yliko_label = QLabel("Επιλέξτε Υλικό:")
        posotita_label = QLabel("Δώστε την διαθέσιμη ποσότητα του υλικού:")
        posotita_line_edit = QLineEdit()
        vbox.addWidget(yliko_label)
        vbox.addWidget(ylika_cmb)
        vbox.addWidget(posotita_label)
        vbox.addWidget(posotita_line_edit)
        vbox.addStretch()
        self.setLayout(vbox)


if __name__ == "__main__":
    main()
