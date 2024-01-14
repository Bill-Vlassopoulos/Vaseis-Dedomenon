import sqlite3

conn = sqlite3.connect("SmartRestaurant.db")

cursor = conn.cursor()

commands = [
    """
CREATE TABLE "PELATIS"(
    "id_pelati" INTEGER PRIMARY KEY AUTOINCREMENT,
    "onoma" varchar(20) NOT NULL,
    "eponimo" varchar(20) NOT NULL,
    "tilefono" varchar(13) NOT NULL,
    "email" varchar(20),
    "username" varchar(30),
    "password" varchar(20)
);
""",
    """
CREATE TABLE "TRAPEZI"(
    "id_trapeziou" varchar(10) NOT NULL UNIQUE,
    "thesi" varchar(20),
    "aritmos_theseon" INTEGER NOT NULL CHECK("aritmos_theseon">0),
    PRIMARY KEY("id_trapeziou")
);
""",
    """
CREATE TABLE "KRATISI"(
    "id_kratisis"  INTEGER PRIMARY KEY AUTOINCREMENT,
    "imera_ora" datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
    "aritmos_atomon" INTEGER,
    "id_trapeziou" varchar(10) NOT NULL,
    FOREIGN KEY("id_trapeziou") REFERENCES "TRAPEZI"("id_trapeziou")
);
""",
    """
CREATE TABLE "KRITIKI"(
    "id" INTEGER NOT NULL UNIQUE ,
    "bathmologia" varchar(8) CHECK("bathmologia">0),
    "perigrafi" varchar(400),
    "imerominia" datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
    "id_pelati" INTEGER,
    FOREIGN KEY("id_pelati") REFERENCES "PELATIS"("id_pelati") ,
    PRIMARY KEY("id" AUTOINCREMENT)
);
""",
    """
CREATE TABLE "PARAGGELIA"(
    "id_paraggelias" INTEGER NOT NULL UNIQUE ,
    "imer_ora" datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
    "kostos" REAL,
    "id_trapeziou" INTEGER NOT NULL,
    FOREIGN KEY("id_trapeziou") REFERENCES "TRAPEZI"("id_trapeziou"),
    PRIMARY KEY("id_paraggelias" AUTOINCREMENT)
);
""",
    """
CREATE TABLE "FAGITO" (
	"id_fagitoy" INTEGER NOT NULL UNIQUE ,
	"onoma" VARCHAR(30) NOT NULL,
	"kostos" REAL NOT NULL,
	"syntagi" varchar(500) NOT NULL,
    PRIMARY KEY("id_fagitoy" AUTOINCREMENT)
);
""",
    """
CREATE TABLE "POTO" (
	"id_potoy" INTEGER NOT NULL UNIQUE ,
	"onoma" VARCHAR(30) NOT NULL,
	"kostos" REAL ,
	PRIMARY KEY("id_potoy" AUTOINCREMENT)
);
""",
    """
CREATE TABLE PERILAMBANEI (
    "id_paraggelias" INTEGER NOT NULL,
    "id_fagitoy" INTEGER,
    "id_potoy" INTEGER,
    "id_perilambanei" INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY ("id_paraggelias") REFERENCES PARAGGELIA("id_paraggelias"),
    FOREIGN KEY ("id_potoy") REFERENCES POTO("id_potoy"),
    FOREIGN KEY ("id_fagitoy") REFERENCES FAGITO("id_fagitoy")
);
""",
    """
CREATE TABLE "KANEI" (
	"id_pelati" INTEGER,
	"id_kratisis"  INTEGER,
	PRIMARY KEY("id_pelati", "id_kratisis"),
    FOREIGN KEY("id_pelati") REFERENCES "TRAPEZI"("id_trapeziou"),
    FOREIGN KEY("id_kratisis") REFERENCES "KRATISI"("id_kratisis")
);
""",
]


for command in commands:
    conn.execute(command)

conn.commit()
conn.close()
