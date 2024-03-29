import sqlite3

conn = sqlite3.connect("SmartRestaurant.db")

cursor = conn.cursor()

commands = [
    """
CREATE TABLE "PELATIS"(
    "id_pelati" INTEGER NOT NULL UNIQUE,
    "onoma" varchar(20) NOT NULL,
    "eponimo" varchar(20) NOT NULL,
    "tilefono" varchar(13) NOT NULL,
    "email" varchar(20),
    "username" varchar(30),
    "password" varchar(20),

    PRIMARY KEY("id_pelati" AUTOINCREMENT)
);
""",
    """
CREATE TABLE "KRATISI"(
    "id_kratisis" INTEGER NOT NULL UNIQUE ,
    "imera_ora" datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
    "aritmos_atomon" INTEGER,
    
    PRIMARY KEY("id_kratisis" AUTOINCREMENT)
);
""",
    """
CREATE TABLE "TRAPEZI"(
    "id_trapeziou" INTEGER NOT NULL UNIQUE,
    "thesi" varchar(8),
    "aritmos_theseon" INTEGER NOT NULL CHECK("aritmos_theseon">0),
    "id_kratisis" INTEGER,
    FOREIGN KEY("id_kratisis") REFERENCES "KRATISI"("id_kratisis"),
    PRIMARY KEY("id_trapeziou")
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
    "kostos" REAL CHECK("kostos">0),
    "id_trapeziou" INTEGER NOT NULL,
    FOREIGN KEY("id_trapeziou") REFERENCES "TRAPEZI"("id_trapeziou"),
    PRIMARY KEY("id_paraggelias" AUTOINCREMENT)
);
""",
    """
CREATE TABLE "MAGEIRAS" (
	"afm_ypallilou"	integer NOT NULL UNIQUE,
	"onoma"	varchar(30) NOT NULL,
	"eponimo"	varchar(50) DEFAULT NULL,
	"misthos"	REAL NOT NULL CHECK("misthos>0"),
	"tilefono"	varchar(13) NOT NULL,
	"orario"    varchar (30) NOT NULL,
	PRIMARY KEY("afm_ypallilou")
);
""",
    """
CREATE TABLE "SERVITOROS" (
	"afm_ypallilou"	integer NOT NULL UNIQUE,
	"onoma"	varchar(30) NOT NULL,
	"eponimo"	varchar(50) DEFAULT NULL,
	"misthos"	integer NOT NULL,
	"tilefono"	varchar(13) NOT NULL,
	"orario"    varchar (30) NOT NULL,
	PRIMARY KEY("afm_ypallilou")
);
""",
    """

CREATE TABLE "PROMITHEYTIS" (
	"afm"	integer NOT NULL UNIQUE,
	"onoma"	varchar(30) NOT NULL,
	"epitheto"	varchar(50) DEFAULT NULL,
	"tilefono"	integer NOT NULL,
	PRIMARY KEY("afm")
);
""",
    """
CREATE TABLE "YLIKA" (
	"id_ylikoy"	integer NOT NULL UNIQUE ,
	"onoma"	varchar(30) NOT NULL,
	"katigoria"	varchar(50) DEFAULT NULL,
	"diathesimi_posothta"	integer NOT NULL,
	PRIMARY KEY("id_ylikoy" AUTOINCREMENT)
);
""",
    """
CREATE TABLE "FAGITO" (
	"id_proiontos" INTEGER NOT NULL UNIQUE ,
	"onoma" VARCHAR(30) NOT NULL,
	"kostos" REAL NOT NULL,
	"diathesimothta" INTEGER NOT NULL CHECK ("diathesimothta" >= 0),
	"syntagi" varchar(500) NOT NULL,
    PRIMARY KEY("id_proiontos" AUTOINCREMENT)
);
""",
    """
CREATE TABLE "POTO" (
	"id_proiontos" INTEGER NOT NULL UNIQUE ,
	"onoma" VARCHAR(30) NOT NULL,
	"kostos" REAL NOT NULL CHECK(kostos>0.0),
	"diathesimothta" INTEGER NOT NULL CHECK ("diathesimothta" >= 0),
	PRIMARY KEY("id_proiontos" AUTOINCREMENT)
);
""",
    """
CREATE TABLE "PARASKEYAZEI" (
	"afm_ypallilou"	integer NOT NULL,
	"id_proiontos"	integer NOT NULL,
	FOREIGN KEY("afm_ypallilou") REFERENCES "MAGEIRAS"("afm_ypallilou")
	FOREIGN KEY("id_proiontos") REFERENCES "FAGITO"("id_proiontos")
	PRIMARY KEY("afm_ypallilou","id_proiontos")
);
""",
    """
CREATE TABLE "APOTELEITAI" (
	"id_proiontos"	integer NOT NULL,
	"id_ylikoy" integer NOT NULL,
    FOREIGN KEY("id_proiontos") REFERENCES "FAGITO"("id_proiontos"),
    FOREIGN KEY("id_ylikoy") REFERENCES "YLIKA"("id_ylikoy"),
	PRIMARY KEY("id_proiontos","id_ylikoy")
);
""",
    """

CREATE TABLE "PERILAMBANEI" (
	"id_paraggelias"	integer NOT NULL,
	"id_proiontos"	integer NOT NULL,
	FOREIGN KEY("id_paraggelias") REFERENCES "PARAGGELIA"("id_paraggelias"),
	FOREIGN KEY("id_proiontos") REFERENCES "POTO"("id_proiontos"),
	FOREIGN KEY("id_proiontos") REFERENCES "FAGITO"("id_proiontos")
    PRIMARY KEY("id_paraggelias","id_proiontos")
);
""",
    """
CREATE TABLE "ANALAMBANEI" (
	"id_paraggelias" integer NOT NULL,
	"afm_ypallilou"	integer NOT NULL,
    FOREIGN KEY("id_paraggelias") REFERENCES "PARAGGELIA"("id_paraggelias"),
    FOREIGN KEY("afm_ypallilou") REFERENCES "SERVITOROS"("afm_ypallilou"),
    PRIMARY KEY("id_paraggelias","afm_ypallilou")
);
""",
    """
CREATE TABLE "EFODIAZEI" (
	"afm"	integer NOT NULL,
	"id_ylikoy"	integer NOT NULL,
	PRIMARY KEY("id_ylikoy", "afm")
	FOREIGN KEY("afm") REFERENCES "PROMITHEYTIS"("afm") 
	FOREIGN KEY("id_ylikoy") REFERENCES "YLIKA"("id_ylikoy") 
);
""",
    """
CREATE TABLE "PROMITHEVEI" (
	"afm"	integer NOT NULL,
	"id_proiontos"	integer NOT NULL,
	"imer_paradosis" datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
	PRIMARY KEY("afm", "id_proiontos"),
    FOREIGN KEY("afm") REFERENCES "PROMITHEYTIS"("afm"),
    FOREIGN KEY("id_proiontos") REFERENCES "POTO"("id_proiontos")
);
""",
]

for command in commands:
    conn.execute(command)

conn.commit()
conn.close()
