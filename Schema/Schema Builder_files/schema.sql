CREATE TABLE IF NOT EXISTS "ΠΕΛΑΤΗΣ" (
	"ID Πελάτη" integer,
	"Όνομα " string,
	"Επώνυμο" string,
	"Τηλέφωνο" integer,
	"Email" string,
	PRIMARY KEY ("ID Πελάτη")
);

CREATE TABLE IF NOT EXISTS "ΚΡΑΤΗΣΗ" (
	"ID Κράτησης" integer,
	"Ημερομηνία κ΄ Ώρα Κράτησης" datetime,
	"Ώρα Άφιξης" time,
	"Αριθμός Ατόμων" integer,
	PRIMARY KEY ("ID Κράτησης")
);

CREATE TABLE IF NOT EXISTS "ΚΡΙΤΙΚΗ" (
	"ID Κριτικής" integer,
	"Βαθμολογία" integer,
	"Περιγραφή" string,
	"Ημερομηνία Κριτικής" date,
	"ID Πελάτη" integer,
	PRIMARY KEY ("ID Κριτικής"),
	FOREIGN KEY ("ID Πελάτη") REFERENCES "ΠΕΛΑΤΗΣ" ("ID Πελάτη")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ΤΡΑΠΕΖΙ" (
	"Αριθμός Τραπεζιού" integer,
	"Θέση Τραπεζιού" varchar,
	"Αριθμός Θέσεων Τραπεζιού" integer,
	"Πρόσβαση ΑΜΕΑ" boolean,
	"ID Κράτησης" integer,
	PRIMARY KEY ("Αριθμός Τραπεζιού"),
	FOREIGN KEY ("ID Κράτησης") REFERENCES "ΚΡΑΤΗΣΗ" ("ID Κράτησης")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ΚΑΝΕΙ" (
	"ID Πελάτη" integer,
	"ID Κράτησης" integer,
	PRIMARY KEY ("ID Πελάτη", "ID Κράτησης"),
	FOREIGN KEY ("ID Πελάτη") REFERENCES "ΠΕΛΑΤΗΣ" ("ID Πελάτη")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("ID Κράτησης") REFERENCES "ΚΡΑΤΗΣΗ" ("ID Κράτησης")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ΠΑΡΑΓΓΕΛΙΑ" (
	"ID Παραγγελίας " integer,
	"Ώρα Παραγγελίας" time,
	"Κόστος" float,
	"Αριθμός Τραπεζιού" integer,
	PRIMARY KEY ("ID Παραγγελίας "),
	FOREIGN KEY ("Αριθμός Τραπεζιού") REFERENCES "ΤΡΑΠΕΖΙ" ("Αριθμός Τραπεζιού")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ΠΕΡΙΛΑΜΒΑΝΕΙ" (
	"ID Παραγγελίας" integer,
	"ID Προιόντος" integer,
	PRIMARY KEY ("ID Παραγγελίας", "ID Προιόντος"),
	FOREIGN KEY ("ID Παραγγελίας") REFERENCES "ΠΑΡΑΓΓΕΛΙΑ" ("ID Παραγγελίας ")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ΦΑΓΗΤΟ" (
	"ID Προιόντος" integer,
	"Όνομα" string,
	"Κόστος" float,
	"Διαθεσιμότητα" integer,
	"Συνταγή" string,
	"Ειδικά Χαρακτηριστικά" string,
	PRIMARY KEY ("ID Προιόντος"),
	FOREIGN KEY ("ID Προιόντος") REFERENCES "ΠΕΡΙΛΑΜΒΑΝΕΙ" ("ID Προιόντος")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ΠΟΤΟ" (
	"ID Προιόντος" integer,
	"Όνομα" string,
	"Κόστος" float,
	"Διαθεσιμότητα" integer,
	PRIMARY KEY ("ID Προιόντος"),
	FOREIGN KEY ("ID Προιόντος") REFERENCES "ΠΕΡΙΛΑΜΒΑΝΕΙ" ("ID Προιόντος")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ΠΡΟΜΗΘΕΥΤΗΣ" (
	"ΑΦΜ" integer,
	"Όνομα " string,
	"Επίθετο" string,
	"Τηλέφωνο" integer,
	PRIMARY KEY ("ΑΦΜ")
);

CREATE TABLE IF NOT EXISTS "ΠΡΟΜΗΘΕΥΕΙ" (
	"ΑΦΜ" integer,
	"ID Προιόντος" integer,
	"Ημερομηνία Παράδοσης" date,
	PRIMARY KEY ("ΑΦΜ", "ID Προιόντος"),
	FOREIGN KEY ("ΑΦΜ") REFERENCES "ΠΡΟΜΗΘΕΥΤΗΣ" ("ΑΦΜ")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("ID Προιόντος") REFERENCES "ΠΟΤΟ" ("ID Προιόντος")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ΥΛΙΚΑ" (
	"ID Υλικού" integer,
	"Όνομα" string,
	"Κατηγορία" string,
	"Διαθέσιμη Ποσότητα" integer,
	PRIMARY KEY ("ID Υλικού")
);

CREATE TABLE IF NOT EXISTS "ΑΠΟΤΕΛΕΙΤΑΙ" (
	"ID Προιόντος" integer,
	"ID Υλικού" integer,
	PRIMARY KEY ("ID Προιόντος", "ID Υλικού"),
	FOREIGN KEY ("ID Προιόντος") REFERENCES "ΦΑΓΗΤΟ" ("ID Προιόντος")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("ID Υλικού") REFERENCES "ΥΛΙΚΑ" ("ID Υλικού")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ΕΦΟΔΙΑΖΕΙ" (
	"ΑΦΜ" integer,
	"ID Υλικού" integer,
	PRIMARY KEY ("ΑΦΜ", "ID Υλικού"),
	FOREIGN KEY ("ΑΦΜ") REFERENCES "ΠΡΟΜΗΘΕΥΤΗΣ" ("ΑΦΜ")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("ID Υλικού") REFERENCES "ΥΛΙΚΑ" ("ID Υλικού")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ΣΕΡΒΙΤΟΡΟΣ" (
	"ΑΦΜ Υπαλλήλου" ,
	"Όνομα " ,
	"Επώνυμο " ,
	"ΜΙσθός" ,
	"Τηλέφωνο" ,
	"Ωράριο" ,
	PRIMARY KEY ("ΑΦΜ Υπαλλήλου")
);

CREATE TABLE IF NOT EXISTS "ΜΑΓΕΙΡΑΣ" (
	"ΑΦΜ Υπαλλήλου" ,
	"Όνομα " ,
	"Επώνυμο " ,
	"ΜΙσθός" ,
	"Τηλέφωνο" ,
	"Ωράριο" ,
	PRIMARY KEY ("ΑΦΜ Υπαλλήλου")
);

CREATE TABLE IF NOT EXISTS "ΑΝΑΛΑΜΒΆΝΕΙ" (
	"ΑΦΜ Υπαλλήλου" ,
	"ID Παραγγελίας" ,
	PRIMARY KEY ("ΑΦΜ Υπαλλήλου", "ID Παραγγελίας"),
	FOREIGN KEY ("ΑΦΜ Υπαλλήλου") REFERENCES "ΣΕΡΒΙΤΟΡΟΣ" ("ΑΦΜ Υπαλλήλου")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("ID Παραγγελίας") REFERENCES "ΠΑΡΑΓΓΕΛΙΑ" ("ID Παραγγελίας ")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ΠΑΡΑΣΚΕΥΑΖΕΙ" (
	"ΑΦΜ Υπαλλήλου" ,
	"ID Προιόντος" ,
	PRIMARY KEY ("ΑΦΜ Υπαλλήλου", "ID Προιόντος"),
	FOREIGN KEY ("ΑΦΜ Υπαλλήλου") REFERENCES "ΜΑΓΕΙΡΑΣ" ("ΑΦΜ Υπαλλήλου")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("ID Προιόντος") REFERENCES "ΦΑΓΗΤΟ" ("ID Προιόντος")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

