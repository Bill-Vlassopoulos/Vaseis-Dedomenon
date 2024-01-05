import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.sip import voidptr
from datetime import datetime, timedelta


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
        login_button.clicked.connect(self.pelatis_window)

        ########################## CREATE ACCOUNT BUTTON #########################
        create_account_button = QPushButton("Create Account", self)
        create_account_button.setStyleSheet("background-color: orange; color: black;")
        create_account_button.clicked.connect(self.create_account)

        line_edits_vbox.setContentsMargins(90, 20, 20, 20)
        line_edits_vbox.addStretch()
        line_edits_vbox.addWidget(name)
        line_edits_vbox.addWidget(password)
        line_edits_vbox.addStretch()

        vbox.addLayout(line_edits_vbox)
        vbox.addStretch()
        hbox.addStretch()
        hbox.addWidget(login_button)
        hbox.addWidget(create_account_button)
        hbox.addStretch()

        vbox.addLayout(hbox)
        self.setLayout(vbox)

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
        name = QLineEdit()
        hbox = QHBoxLayout()

        name.setPlaceholderText("username")
        name.setFixedHeight(50)
        name.setFixedWidth(250)
        name.setStyleSheet("color:white; border:2px solid white; border-radius:10;")
        name.setFont(QFont("Arial", 12))

        password = QLineEdit()
        password.setPlaceholderText("password")
        password.setFixedHeight(50)
        password.setFixedWidth(250)
        password.setStyleSheet("color:white; border:2px solid white; border-radius:10;")
        password.setFont(QFont("Arial", 12))

        tilefono = QLineEdit()
        tilefono.setPlaceholderText("phone number(69********)")
        tilefono.setFixedHeight(50)
        tilefono.setFixedWidth(250)
        tilefono.setStyleSheet("color:white; border:2px solid white; border-radius:10;")
        tilefono.setFont(QFont("Arial", 12))

        email = QLineEdit()
        email.setPlaceholderText("email (name@example.com)")
        email.setFixedHeight(50)
        email.setFixedWidth(250)
        email.setStyleSheet("color:white; border:2px solid white; border-radius:10;")
        email.setFont(QFont("Arial", 12))

        create_account_button = QPushButton("Create Account", self)
        create_account_button.setStyleSheet("background-color: orange; color: black;")
        create_account_button.setMinimumSize(100, 50)
        #        create_account_button.clicked.connect(self.create_account)

        vbox.addWidget(name)
        vbox.addWidget(password)
        vbox.addWidget(tilefono)
        vbox.addWidget(email)
        vbox.setContentsMargins(90, 40, 40, 40)

        hbox.addStretch()
        hbox.addWidget(create_account_button)
        hbox.addStretch()

        main_vbox.addLayout(vbox)
        main_vbox.addLayout(hbox)

        self.setLayout(main_vbox)


class PelatisWindow(QWidget):
    def __init__(self):
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
        vbox.addWidget(QLabel("Επιλέξτε Ημερομηνία:"))
        vbox.addWidget(self.date)
        vbox.addWidget(QLabel("Επιλέξτε Τραπέζι:"))
        vbox.addWidget(self.tables)
        vbox.addWidget(QLabel("Επιλέξτε Αριθμό Ατόμων:"))
        vbox.addWidget(self.people)
        vbox.addStretch()
        self.kratisi_btn = QPushButton("Κάνε Κράτηση")
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

        ypovoli_kritikis_btn = QPushButton("Υποβολή Κριτικής")
        vbox_1.addWidget(ypovoli_kritikis_btn)
        self.kritiki.setLayout(vbox_1)
        self.kritiki_tab.addTab(self.kritiki, "Κριτική")
        #        self.kritiki_tab.setFixedSize(400, 330)
        hbox.addWidget(self.kritiki_tab)
        main_vbox.addLayout(hbox)
        # hbox.setContentsMargins(10, 10, 10, 10)
        self.kratiseis = QWidget()
        self.kratiseis_tab = QTabWidget()

        self.kratiseis_table = QTableWidget()
        self.kratiseis_table.setRowCount(3)
        self.kratiseis_table.setColumnCount(3)
        self.kratiseis_table.setHorizontalHeaderLabels(
            ["Ημερομηνία", "Τραπέζι", "Άτομα"]
        )

        kratiseis_hbox.addWidget(self.kratiseis_table)
        kratiseis_hbox.addWidget(QPushButton("Διαγραφή"))
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


if __name__ == "__main__":
    main()
