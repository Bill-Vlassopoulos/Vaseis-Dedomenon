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
    window = Statistika()
    window.show()
    app.exec()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        main_vbox = QVBoxLayout()
        self.setWindowTitle("Estiatorio")
        self.setGeometry(300, 300, 450, 450)
        self.setFixedSize(450, 300)
        self.kratiseis_btn = QPushButton("Διαχείριση Καταστήματος")

        self.new_paraggelia_btn = QPushButton("Στατιστικά")

        main_vbox.addWidget(self.kratiseis_btn)
        main_vbox.addWidget(self.new_paraggelia_btn)
        self.setLayout(main_vbox)


class Diacheirisi(QWidget):
    def __init__(self):
        super().__init__()
        main_vbox = QVBoxLayout()
        self.setWindowTitle("Estiatorio")
        self.setGeometry(300, 300, 450, 450)
        self.setFixedSize(450, 450)

        self.add_food_btn = QPushButton("Προσθήκη Φαγητού")
        self.add_poto_btn = QPushButton("Προσθήκη Ποτού")
        self.add_trapezi_btn = QPushButton("Προσθήκη Τραπέζι")

        main_vbox.addWidget(self.add_food_btn)
        main_vbox.addWidget(self.add_poto_btn)
        main_vbox.addWidget(self.add_trapezi_btn)
        self.setLayout(main_vbox)


class Trapezi(QWidget):
    def __init__(self):
        super().__init__()
        main_vbox = QVBoxLayout()
        self.setWindowTitle("Estiatorio")
        self.setGeometry(300, 300, 450, 450)
        self.setFixedSize(450, 450)

        kod_trap_line_edit = QLineEdit()
        theseis = QComboBox()
        topothesia_line_edit = QLineEdit()
        add_trapezi_btn = QPushButton("Προσθήκη Τραπεζιού")

        main_vbox.addWidget(QLabel("Δώστε Όνομα Τραπεζιού:"))
        main_vbox.addWidget(kod_trap_line_edit)
        main_vbox.addWidget(QLabel("Δώστε Αριθμό Θέσεων:"))
        main_vbox.addWidget(theseis)
        main_vbox.addWidget(QLabel("Δώστε Τοποθεσία Τραπεζιού:"))
        main_vbox.addWidget(topothesia_line_edit)
        main_vbox.addStretch()
        main_vbox.addWidget(add_trapezi_btn)
        self.setLayout(main_vbox)


class Food_Poto(QWidget):
    def __init__(self):
        super().__init__()
        right_vbox = QVBoxLayout()
        left_vbox = QVBoxLayout()
        main_hbox = QHBoxLayout()
        self.setWindowTitle("Estiatorio")
        self.setGeometry(300, 300, 450, 450)
        self.setFixedSize(450, 450)

        self.onoma_food_line_edit = QLineEdit()
        self.syntagi_text_edit = QTextEdit()
        self.kostos_line_edit = QLineEdit()
        self.add_food_btn = QPushButton("Προσθήκη Φαγητού")
        self.add_food_btn.clicked.connect(self.add_food)

        self.onoma_poto_line_edit = QLineEdit()
        self.kostos1_line_edit = QLineEdit()
        self.add_poto_btn = QPushButton("Προσθήκη Ποτού")
        self.add_poto_btn.clicked.connect(self.add_poto)

        left_vbox.addWidget(QLabel("Δώστε Όνομα Φαγητού:"))
        left_vbox.addWidget(self.onoma_food_line_edit)
        left_vbox.addWidget(QLabel("Δώστε το Κόστος:"))
        left_vbox.addWidget(self.kostos_line_edit)
        left_vbox.addWidget(QLabel("Δώστε την Συνταγή:"))
        left_vbox.addWidget(self.syntagi_text_edit)
        left_vbox.addStretch()
        left_vbox.addWidget(self.add_food_btn)

        right_vbox.addWidget(QLabel("Δώστε Όνομα Ποτού:"))
        right_vbox.addWidget(self.onoma_poto_line_edit)
        right_vbox.addWidget(QLabel("Δώστε το Κόστος:"))
        right_vbox.addWidget(self.kostos1_line_edit)
        right_vbox.addStretch()
        right_vbox.addWidget(self.add_poto_btn)

        main_hbox.addLayout(left_vbox)
        main_hbox.addLayout(right_vbox)
        self.setLayout(main_hbox)

    def add_food(self):
        cursor.execute(
            "insert into FAGITO(onoma,kostos,posotita,syntagi) VALUES(?,?,?,?)",
            (
                self.onoma_food_line_edit.text(),
                float(self.kostos_line_edit.text()),
                10,
                self.syntagi_text_edit.toPlainText(),
            ),
        )
        conn.commit()
        self.onoma_food_line_edit.setText("")
        self.kostos_line_edit.setText("")
        self.syntagi_text_edit.setText("")

    def add_poto(self):
        cursor.execute(
            "insert into POTO(onoma,kostos,posotita) VALUES(?,?,?)",
            (
                self.onoma_poto_line_edit.text(),
                float(self.kostos1_line_edit.text()),
                10,
            ),
        )
        conn.commit()
        self.onoma_poto_line_edit.setText("")
        self.kostos1_line_edit.setText("")


class Statistika(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estiatorio")
        self.setGeometry(300, 300, 450, 450)
        self.setFixedSize(450, 450)
        main_vbox = QVBoxLayout()
        self.day_profit_line_edit = QLineEdit()
        self.month_profit_line_edit = QLineEdit()
        top5_food = QLineEdit()
        top5_drinks = QLineEdit()
        self.get_month_profits()
        self.month_dates = QComboBox()
        self.month_dates.addItems(self.get_dates_until_last_month())
        self.month_dates.activated.connect(self.get_day_profits)
        main_vbox.addWidget(QLabel("Επέλεξε Ημερομηνία:"))
        main_vbox.addWidget(self.month_dates)
        main_vbox.addWidget(QLabel("Ημερήσια Έσοδα"))
        main_vbox.addWidget(self.day_profit_line_edit)

        main_vbox.addWidget(QLabel("Μηνιαία Έσοδα"))
        main_vbox.addWidget(self.month_profit_line_edit)
        main_vbox.addStretch()
        self.setLayout(main_vbox)

    def get_dates_until_last_month(self):
        today = datetime.now()

        # Δημιουργία λίστας με τις ημερομηνίες ως συμβολοσειρές (εκτός από τις Δευτέρες) μέχρι πριν ένα μήνα
        dates_list = [
            (today - timedelta(days=x)).strftime("%Y-%m-%d")
            for x in range(0, 30)
            if (today - timedelta(days=x)).weekday() != 0
        ]

        return dates_list

    def get_day_profits(self):
        self.month_dates.currentText()
        cursor.execute(
            """
            SELECT sum(FAGITO.kostos)
            FROM PERILAMBANEI
            JOIN PARAGGELIA ON PERILAMBANEI.id_paraggelias=PARAGGELIA.id_paraggelias
            JOIN FAGITO ON PERILAMBANEI.id_fagitoy=FAGITO.id_fagitoy
            WHERE imer_ora LIKE '{}%'
            """.format(
                self.month_dates.currentText()
            ),
        )
        results = cursor.fetchone()
        food_profits = results[0]
        cursor.execute(
            """
            SELECT sum(POTO.kostos)
            FROM PERILAMBANEI
            JOIN PARAGGELIA ON PERILAMBANEI.id_paraggelias=PARAGGELIA.id_paraggelias
            JOIN POTO ON PERILAMBANEI.id_potoy=POTO.id_potoy
            WHERE imer_ora LIKE '{}%'
            """.format(
                self.month_dates.currentText()
            )
        )
        results = cursor.fetchone()
        drink_profits = results[0]
        self.day_profit_line_edit.setText(str(food_profits + drink_profits) + "€")

    def get_month_profits(self):
        self.first_day = self.first_day_of_month()
        cursor.execute(
            """
            SELECT sum(FAGITO.kostos)
            FROM PERILAMBANEI
            JOIN PARAGGELIA ON PERILAMBANEI.id_paraggelias=PARAGGELIA.id_paraggelias
            JOIN FAGITO ON PERILAMBANEI.id_fagitoy=FAGITO.id_fagitoy
            WHERE imer_ora >'{}'
            """.format(
                self.first_day
            ),
        )
        results = cursor.fetchone()
        food_profits = results[0]
        cursor.execute(
            """
            SELECT sum(POTO.kostos)
            FROM PERILAMBANEI
            JOIN PARAGGELIA ON PERILAMBANEI.id_paraggelias=PARAGGELIA.id_paraggelias
            JOIN POTO ON PERILAMBANEI.id_potoy=POTO.id_potoy
            WHERE imer_ora > '{}'
            """.format(
                self.first_day
            )
        )
        results = cursor.fetchone()
        drink_profits = results[0]
        self.month_profit_line_edit.setText(str(food_profits + drink_profits) + "€")

    def first_day_of_month(self):
        today = datetime.now()
        first_day = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        formatted_first_day = first_day.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_first_day


if __name__ == "__main__":
    main()
