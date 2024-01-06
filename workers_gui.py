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
        super().__init__()
        main_vbox = QVBoxLayout()
        self.setWindowTitle("Estiatorio")
        self.setGeometry(300, 300, 450, 450)
        self.setFixedSize(450, 450)
        self.kratiseis_btn = QPushButton("Κρατήσεις")
        self.kratiseis_btn.clicked.connect(self.open_kratiseis)

        self.new_paraggelia_btn = QPushButton("Νέα Παραγγελία")
        self.new_paraggelia_btn.clicked.connect(self.open_new_paraggelia)

        self.edit_paraggelia_btn = QPushButton("Διαχείριση Παραγγελίας")
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
        fagita = QListWidget()
        pota = QListWidget()
        fagita.addItems(["pizza", "souvlaki"])
        pota.addItems(["νερό", "πορτοκαλάδα", "κόκα κόλα"])
        trapezi_cmb = QComboBox()
        trapezi_label = QLabel("Eπιλέξτε Τραπέζι:")
        piata_label = QLabel("Επιλέξτε Πιάτα:")
        pota_label = QLabel("Επιλέξτε Ποτά:")
        add_food_btn = QPushButton("Προσθήκη Πιάτου")
        add_drink_btn = QPushButton("Προσθήκη Ποτού")
        ypovoli_btn = QPushButton("Υποβολή Παραγγελίας")
        delete_btn = QPushButton("Διαγραφή Προιόντος")
        self.kratiseis_table = QTableWidget()
        self.kratiseis_table.setRowCount(3)
        self.kratiseis_table.setColumnCount(3)
        self.kratiseis_table.setHorizontalHeaderLabels(["Όνομα", "Ποσότητα", "Κόστος"])

        left_vbox.addWidget(piata_label)
        left_vbox.addWidget(fagita)
        left_vbox.addStretch()

        right_vbox.addWidget(pota_label)
        right_vbox.addWidget(pota)
        right_vbox.addStretch()

        hbox.addLayout(left_vbox)
        hbox.addStretch()
        hbox.addLayout(right_vbox)

        down_right_vbox.addWidget(trapezi_label)
        down_right_vbox.addWidget(trapezi_cmb)
        down_right_vbox.addWidget(add_food_btn)
        down_right_vbox.addWidget(add_drink_btn)
        down_right_vbox.addWidget(delete_btn)
        down_right_vbox.addWidget(ypovoli_btn)
        down_right_vbox.addStretch()
        down_hbox.addWidget(self.kratiseis_table)
        down_hbox.addLayout(down_right_vbox)
        main_vbox.addLayout(hbox)
        main_vbox.addLayout(down_hbox)
        self.setLayout(main_vbox)


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
        fagita = QListWidget()
        pota = QListWidget()
        fagita.addItems(["pizza", "souvlaki"])
        pota.addItems(["νερό", "πορτοκαλάδα", "κόκα κόλα"])
        trapezi_cmb = QComboBox()
        trapezi_label = QLabel("Eπιλέξτε Τραπέζι:")
        piata_label = QLabel("Επιλέξτε Πιάτα:")
        kostos_label = QLabel("Τελικό Κόστος:")
        kostos_line_edit = QLineEdit()
        kostos_line_edit.setFixedSize(80, 40)
        pota_label = QLabel("Επιλέξτε Ποτά:")
        add_food_btn = QPushButton("Προσθήκη Πιάτου")
        add_drink_btn = QPushButton("Προσθήκη Ποτού")
        ypovoli_btn = QPushButton("Ανανέωση Παραγγελίας")
        delete_btn = QPushButton("Διαγραφή Προιόντος")
        self.kratiseis_table = QTableWidget()
        self.kratiseis_table.setRowCount(3)
        self.kratiseis_table.setColumnCount(3)
        self.kratiseis_table.setHorizontalHeaderLabels(["Όνομα", "Ποσότητα", "Κόστος"])

        left_vbox.addWidget(piata_label)
        left_vbox.addWidget(fagita)
        left_vbox.addStretch()

        right_vbox.addWidget(pota_label)
        right_vbox.addWidget(pota)
        right_vbox.addStretch()

        hbox.addLayout(left_vbox)
        hbox.addStretch()
        hbox.addLayout(right_vbox)

        down_right_vbox.addWidget(trapezi_label)
        down_right_vbox.addWidget(trapezi_cmb)
        down_right_vbox.addWidget(add_food_btn)
        down_right_vbox.addWidget(add_drink_btn)
        down_right_vbox.addWidget(delete_btn)
        down_right_vbox.addWidget(ypovoli_btn)
        down_right_vbox.addStretch()
        down_right_vbox.addWidget(kostos_label)
        down_right_vbox.addWidget(kostos_line_edit)

        down_hbox.addWidget(self.kratiseis_table)
        down_hbox.addLayout(down_right_vbox)
        main_vbox.addLayout(hbox)
        main_vbox.addLayout(down_hbox)
        self.setLayout(main_vbox)


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
        self.name = QLineEdit()
        self.surname = QLineEdit()
        self.ypovoli_btn = QPushButton("Υποβολή Κράτησης")
        self.kratiseis_table = QTableWidget()
        self.kratiseis_table.setRowCount(3)
        self.kratiseis_table.setColumnCount(3)
        self.kratiseis_table.setHorizontalHeaderLabels(
            ["Ημερομηνία", "Τραπέζι", "Άτομα"]
        )

        vbox.addWidget(QLabel("Επιλέξτε Ημερομηνία:"))
        vbox.addWidget(self.date)
        vbox.addWidget(QLabel("Επιλέξτε Τραπέζι:"))
        vbox.addWidget(self.tables)
        vbox.addWidget(QLabel("Επιλέξτε Αριθμό Ατόμων:"))
        vbox.addWidget(self.people)
        vbox.addWidget(QLabel("Δώστε το όνομα σας:"))
        vbox.addWidget(self.name)
        vbox.addWidget(QLabel("Δώστε το επίθετο σας:"))
        vbox.addWidget(self.surname)

        vbox.addStretch()

        down_right_vbox.addStretch()
        down_right_vbox.addWidget(self.ypovoli_btn)
        down_right_vbox.addWidget(QPushButton("Ακύρωση Κράτησης"))
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


if __name__ == "__main__":
    main()