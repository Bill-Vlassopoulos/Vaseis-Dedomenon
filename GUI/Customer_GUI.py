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
        super(MainWindow, self).__init__()
        ##########################MAINWINDOW BASIC ATTRIBUTES####################
        self.setWindowTitle("Estiatorio")
        self.setGeometry(300, 300, 450, 450)
        self.setFixedSize(450, 450)
        self.setStyleSheet("background-color: black;")

        ##########################CREATING LAYOUTS#########################
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        line_edits_vbox = QVBoxLayout()

        ########################## USERNAME #########################
        self.name = QLineEdit()
        self.name.setPlaceholderText("username")
        self.name.setFixedHeight(50)
        self.name.setFixedWidth(250)
        self.name.setStyleSheet(
            "color:white; border:2px solid white; border-radius:10;"
        )
        self.name.setFont(QFont("Arial", 12))

        ########################## PASSWORD #########################
        self.password = QLineEdit()
        self.password.setPlaceholderText("password")
        self.password.setFixedHeight(50)
        self.password.setFixedWidth(250)
        self.password.setStyleSheet(
            "color:white; border:2px solid white; border-radius:10;"
        )
        self.password.setFont(QFont("Arial", 12))

        ########################## LOG IN BUTTON #########################
        login_button = QPushButton("Log In", self)
        login_button.setStyleSheet("background-color: orange; color: black;")
        login_button.clicked.connect(self.check_user)

        ########################## CREATE ACCOUNT BUTTON #########################
        create_account_button = QPushButton("Create Account", self)
        create_account_button.setStyleSheet("background-color: orange; color: black;")
        create_account_button.clicked.connect(self.create_account)

        line_edits_vbox.setContentsMargins(90, 20, 20, 20)
        line_edits_vbox.addStretch()
        line_edits_vbox.addWidget(self.name)
        line_edits_vbox.addWidget(self.password)
        line_edits_vbox.addStretch()

        vbox.addLayout(line_edits_vbox)
        vbox.addStretch()
        hbox.addStretch()
        hbox.addWidget(login_button)
        hbox.addWidget(create_account_button)
        hbox.addStretch()

        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def check_user(self):
        query = "SELECT username, password FROM PELATIS"
        cursor.execute(query)
        results = cursor.fetchall()
        if (self.name.text(), self.password.text()) in results:
            self.pelatis_win = PelatisWindow(
                username=self.name.text(), password=self.password.text()
            )
            self.pelatis_win.show()
            self.close()
        else:
            self.name.setText("")
            self.password.setText("")

    def create_account(self):
        self.second = SecondWindow()
        self.second.show()

    def pelatis_window(self):
        self.pelatis_win = PelatisWindow()
        self.pelatis_win.show()


class SecondWindow(QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.setWindowTitle("Estiatorio")
        self.setGeometry(400, 350, 450, 450)
        self.setFixedSize(450, 450)
        self.setStyleSheet("background-color: black;")
        vbox = QVBoxLayout()
        main_vbox = QVBoxLayout()

        hbox = QHBoxLayout()

        self.username = QLineEdit()
        self.username.setPlaceholderText("username")
        self.username.setFixedHeight(50)
        self.username.setFixedWidth(250)
        self.username.setStyleSheet(
            "color:white; border:2px solid white; border-radius:10;"
        )
        self.username.setFont(QFont("Arial", 12))

        self.password = QLineEdit()
        self.password.setPlaceholderText("password")
        self.password.setFixedHeight(50)
        self.password.setFixedWidth(250)
        self.password.setStyleSheet(
            "color:white; border:2px solid white; border-radius:10;"
        )
        self.password.setFont(QFont("Arial", 12))

        self.tilefono = QLineEdit()
        self.tilefono.setPlaceholderText("phone number(69********)")
        self.tilefono.setFixedHeight(50)
        self.tilefono.setFixedWidth(250)
        self.tilefono.setStyleSheet(
            "color:white; border:2px solid white; border-radius:10;"
        )
        self.tilefono.setFont(QFont("Arial", 12))

        self.email = QLineEdit()
        self.email.setPlaceholderText("email (name@example.com)")
        self.email.setFixedHeight(50)
        self.email.setFixedWidth(250)
        self.email.setStyleSheet(
            "color:white; border:2px solid white; border-radius:10;"
        )
        self.email.setFont(QFont("Arial", 12))

        self.onoma = QLineEdit()
        self.onoma.setPlaceholderText("name")
        self.onoma.setFixedHeight(50)
        self.onoma.setFixedWidth(250)
        self.onoma.setStyleSheet(
            "color:white; border:2px solid white; border-radius:10;"
        )
        self.onoma.setFont(QFont("Arial", 12))

        self.epitheto = QLineEdit()
        self.epitheto.setPlaceholderText("surname")
        self.epitheto.setFixedHeight(50)
        self.epitheto.setFixedWidth(250)
        self.epitheto.setStyleSheet(
            "color:white; border:2px solid white; border-radius:10;"
        )
        self.epitheto.setFont(QFont("Arial", 12))

        create_account_button = QPushButton("Create Account", self)
        create_account_button.setStyleSheet("background-color: orange; color: black;")
        create_account_button.setMinimumSize(100, 50)
        create_account_button.clicked.connect(self.pelatis_window)
        #        create_account_button.clicked.connect(self.create_account)

        vbox.addWidget(self.username)
        vbox.addWidget(self.password)
        vbox.addWidget(self.tilefono)
        vbox.addWidget(self.email)
        vbox.addWidget(self.onoma)
        vbox.addWidget(self.epitheto)
        vbox.setContentsMargins(90, 40, 40, 40)

        hbox.addStretch()
        hbox.addWidget(create_account_button)
        hbox.addStretch()

        main_vbox.addLayout(vbox)
        main_vbox.addLayout(hbox)

        self.setLayout(main_vbox)

    def pelatis_window(self):
        query = "SELECT username, password FROM PELATIS"
        cursor.execute(query)
        results = cursor.fetchall()
        self.email
        if (self.username, self.password) in results:
            self.username.setText("")
            self.password.setText("")
            self.onoma.setText("")
            self.epitheto.setText("")
            self.email.setText("")
            self.tilefono.setText("")
        else:
            query = "INSERT INTO PELATIS (onoma, eponimo, tilefono, email, username, password) VALUES(?,?,?,?,?,?)"
            cursor.execute(
                query,
                (
                    self.onoma.text(),
                    self.epitheto.text(),
                    self.tilefono.text(),
                    self.email.text(),
                    self.username.text(),
                    self.password.text(),
                ),
            )
            conn.commit()
            username = self.username.text()
            password = self.password.text()
            self.pelatis_win = PelatisWindow(username=username, password=password)
            self.pelatis_win.show()


class PelatisWindow(QWidget):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        query = "select id_pelati from PELATIS where username='{}' and password='{}'".format(
            self.username, self.password
        )
        cursor.execute(query)
        results = cursor.fetchall()
        self.id_pelati = results[0][0]
        # self.id_pelati = id_pelati
        super(PelatisWindow, self).__init__()
        self.setWindowTitle("Estiatorio")
        self.setGeometry(500, 300, 700, 700)
        self.setFixedSize(800, 700)
        # self.setStyleSheet("background-color: black;")
        hbox = QHBoxLayout()
        kratiseis_hbox = QHBoxLayout()
        main_vbox = QVBoxLayout()
        vbox = QVBoxLayout()
        vbox_1 = QVBoxLayout()
        hbox_1 = QHBoxLayout()

        self.kratisi_tab = QTabWidget(self)
        self.kratisi = QWidget()
        # self.kratisi_tab.setStyleSheet("background-color:gray;")
        # self.date = QCalendar()
        self.date = QComboBox(self)
        self.people = QComboBox(self)
        self.date.addItems(self.load_dates())
        self.tables = QComboBox(self)
        self.tables.activated.connect(self.people_numbers_limit)
        self.tables.addItems(self.gettables())
        self.ora_afixis = QComboBox(self)
        self.ora_afixis.addItems(self.gettimes())
        vbox.addWidget(QLabel("Επιλέξτε Ημερομηνία:"))
        vbox.addWidget(self.date)
        vbox.addWidget(QLabel("Επιλέξτε Τραπέζι:"))
        vbox.addWidget(self.tables)
        vbox.addWidget(QLabel("Επιλέξτε Αριθμό Ατόμων:"))
        vbox.addWidget(self.people)
        vbox.addWidget(QLabel("Επιλέξτε Ώρα άφιξης:"))
        vbox.addWidget(self.ora_afixis)
        vbox.addStretch()
        self.kratisi_btn = QPushButton("Κάνε Κράτηση")
        self.kratisi_btn.clicked.connect(self.ypovoli_kratisis)
        vbox.addWidget(self.kratisi_btn)
        self.kratisi.setLayout(vbox)
        self.kratisi_tab.addTab(self.kratisi, "Κράτηση")
        #        self.kratisi_tab.setFixedSize(400, 330)
        hbox.addWidget(self.kratisi_tab)

        self.kritiki_tab = QTabWidget(self)
        self.kritiki = QWidget()
        vbox_1.addWidget(QLabel("Γράψτε Κριτική:"))
        self.textedit = QTextEdit()
        vbox_1.addWidget(self.textedit)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(10)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(1)
        vbox_1.addWidget(self.slider)

        self.ypovoli_kritikis_btn = QPushButton("Υποβολή Κριτικής")
        self.ypovoli_kritikis_btn.clicked.connect(self.ypovoli_kritikis)
        vbox_1.addWidget(self.ypovoli_kritikis_btn)
        self.kritiki.setLayout(vbox_1)
        self.kritiki_tab.addTab(self.kritiki, "Κριτική")
        #        self.kritiki_tab.setFixedSize(400, 330)
        hbox.addWidget(self.kritiki_tab)
        main_vbox.addLayout(hbox)
        # hbox.setContentsMargins(10, 10, 10, 10)
        self.kratiseis = QWidget()
        self.kratiseis_tab = QTabWidget()

        self.kratiseis_table = QTableWidget()
        self.kratiseis_table.setColumnCount(3)
        self.kratiseis_table.setHorizontalHeaderLabels(
            ["Τραπέζι", "Ημερομηνία-Ώρα", "Άτομα"]
        )
        self.delete_btn = QPushButton("Διαγραφή")
        self.delete_btn.clicked.connect(self.delete_kratisi)
        kratiseis_hbox.addWidget(self.kratiseis_table)
        kratiseis_hbox.addWidget(self.delete_btn)
        self.kratiseis.setLayout(kratiseis_hbox)
        self.kratiseis_tab.addTab(self.kratiseis, "Κρατήσεις")

        main_vbox.addWidget(self.kratiseis_tab)

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

    def ypovoli_kritikis(self):
        text = self.textedit.toPlainText()
        query = "select id_pelati from PELATIS where username='{}' and password='{}'".format(
            self.username, self.password
        )
        cursor.execute(query)
        results = cursor.fetchall()
        self.id_pelati = results[0][0]

        try:
            query = "INSERT INTO KRITIKI (id, bathmologia, perigrafi, imerominia, id_pelati) VALUES(NULL,?,?,?,?)"
            cursor.execute(
                query, (str(self.slider.value()), text, getdatetime(), self.id_pelati)
            )
            conn.commit()

        except Exception as e:
            print("Error " + str(e))
        self.textedit.setText("")

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

    def gettimes(self):
        return ["19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00"]

    def ypovoli_kratisis(self):
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

        self.kratiseis_table.clearContents()
        self.kratiseis_table.setRowCount(0)

        query = "select id_trapeziou,imera_ora,aritmos_atomon from KRATISI where id_kratisis in (select id_kratisis from KANEI where id_pelati={})".format(
            self.id_pelati
        )
        cursor.execute(query)
        results = cursor.fetchall()

        # Ορίστε τον αριθμό των γραμμών του πίνακα
        self.kratiseis_table.setRowCount(len(results))

        for row_index, row_data in enumerate(results):
            id_trapeziou, imera_ora, aritmos_atomon = row_data

            # Προσθέστε τα δεδομένα σε κάθε κελί του πίνακα
            self.kratiseis_table.setItem(
                row_index, 0, QTableWidgetItem(str(id_trapeziou))
            )
            self.kratiseis_table.setItem(row_index, 1, QTableWidgetItem(str(imera_ora)))
            self.kratiseis_table.setItem(
                row_index, 2, QTableWidgetItem(str(aritmos_atomon))
            )

    def get_kratiseis(self):
        self.kratiseis_table.clearContents()
        self.kratiseis_table.setRowCount(0)

        query = "select id_trapeziou,imera_ora,aritmos_atomon from KRATISI where id_kratisis in (select id_kratisis from KANEI where id_pelati={})".format(
            self.id_pelati
        )
        cursor.execute(query)
        results = cursor.fetchall()

        # Ορίστε τον αριθμό των γραμμών του πίνακα
        self.kratiseis_table.setRowCount(len(results))

        for row_index, row_data in enumerate(results):
            id_trapeziou, imera_ora, aritmos_atomon = row_data

            # Προσθέστε τα δεδομένα σε κάθε κελί του πίνακα
            self.kratiseis_table.setItem(
                row_index, 0, QTableWidgetItem(str(id_trapeziou))
            )
            self.kratiseis_table.setItem(row_index, 1, QTableWidgetItem(str(imera_ora)))
            self.kratiseis_table.setItem(
                row_index, 2, QTableWidgetItem(str(aritmos_atomon))
            )

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


def getdatetime():
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime


if __name__ == "__main__":
    main()
