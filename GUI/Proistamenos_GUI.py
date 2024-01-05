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


if __name__ == "__main__":
    main()
