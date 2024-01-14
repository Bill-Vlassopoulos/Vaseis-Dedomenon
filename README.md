# Βάσεις Δεδομένων-Ομάδα 14
Απαραίτητες βιβλιοθήκες για λειτουργία του κώδικα: PyQt5 (pip install pyqt5), datetime (datetime, timedelta), sqlite3, hashlib.
Στο αρχέιο team_14.zip υπάρχουν τα εξής Folders: GUI και Schema. Στο Folder GUI υπάρχουν οι κώδικες python: customer_GUI.py, workers_GUI.py, proistamenos_GUI.py (που είναι οι τρεις διεπαφές της εφαρμογής μας) και την create_table.py (δημιουργία της βάσης SmartRestaurant.tb) και την import_data.py (εισαγωγή δεδομένων στην βάση), η εικόνα bg_image.png, τα αρχεία txt PELATIS.txt, FAGITO.txt, POTO.txt και TRAPEZI.txt τα οποία περιλαμβάνουν δεδομένα για την βάση, καθώς και ένα αρχείο README.txt.
Αρχικά, εισάγουμε το folder GUI σε ένα ide όπου τρέχει python 3.12 και κατεβάζουμε τις απαραίτητες βιβλιοθήκες. Έπειτα, τρέχουμε το αρχείο create_table.py το οποίο δημιουργεί την βάση SmartRestaurant.db (σε περίπτωση που υπάρχει ήδη το αρχείο .db στο Folder και τρέξει ο κώδικας πάλι, θα εμφανιστεί στο terminal ότι υπάρχει ήδη τραπέζι με το όνομα PELATIS). Στην συνέχεια, τρέχουμε το αρχείο import_data.py και εισάγονται τα δεδομένα (txt files) στην βάση. Εφόσον έχει δημιουργηθεί η βάση και έχουν εισαχθεί τα δεδομένα ορθά, μπορούμε να τρέξουμε τις διεπαφές. Για την διεπαφή του πελάτη τρέχουμε την customer_GUI.py και εμφανίζεται το παράθυρο αυτού. Για τον σερβιτόρο υπάρχει αντίστοιχα το wotkers_GUI.py, ενώ για τον διαχειριστή υπάρχει το proistamenos_GUI.py.
