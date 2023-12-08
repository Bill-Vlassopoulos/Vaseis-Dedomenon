BEGIN TRANSACTION;
DROP TABLE IF EXISTS "TRAPEZI";
CREATE TABLE IF NOT EXISTS "TRAPEZI"(
    "id_trapeziou" INTEGER NOT NULL,
    "thesi" varchar(8),
    "aritmos_theseon" INTEGER NOT NULL,
    "id_kratisis" INTEGER,
    CONSTRAINT "TRAPEZI_fk0" FOREIGN KEY("id_kratisis") REFERENCES "KRATISI"("id_kratisis") ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY("id_trapeziou")
);

DROP TABLE IF EXISTS "PELATIS";
CREATE TABLE IF NOT EXISTS "PELATIS"(
    "id_pelati" INTEGER NOT NULL,
    "onoma" varchar(8),
    "eponimo" varchar(8),
    "tilefono" varchar(13),
    "email" varchar(8),

    PRIMARY KEY("id")
);

DROP TABLE IF EXISTS "KRATISI";
CREATE TABLE IF NOT EXISTS "KRATISI"(
    "id_kratisis" INTEGER NOT NULL,
    "imera_ora" datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
    "ora_afiksis" datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
    "aritmos_atomon" INTEGER,
    
    PRIMARY KEY("id_kratisis")
);

DROP TABLE IF EXISTS "KRITIKI";
CREATE TABLE IF NOT EXISTS "KRITIKI"(
    "id" INTEGER NOT NULL,
    "bathmologia" varchar(8),
    "perigrafi" varchar(400),
    "imerominia" datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
    "id_pelati" varchar(8),
    CONSTRAINT "KRITIKI_fk0" FOREIGN KEY("id_pelati") REFERENCES "PELATIS"("id_pelati") ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY("id")
);

DROP TABLE IF EXISTS "PARAGGELIA";
CREATE TABLE IF NOT EXISTS "PARAGGELIA"(
    "id" INTEGER NOT NULL,
    "imer_ora" datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
    "kostos" REAL,
    "id_trapeziou" INTEGER,
    CONSTRAINT "PARAGGELIA_fk0" FOREIGN KEY("id_trapeziou") REFERENCES "KRATISI"("id_trapeziou") ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY("id")
);

BEGIN TRANSACTION;
DROP TABLE IF EXISTS "MAGEIRAS";
CREATE TABLE IF NOT EXISTS "MAGEIRAS" (
	"afm_ypallilou"	integer NOT NULL,
	"onoma"	varchar(30) NOT NULL,
	"eponimo"	varchar(50) DEFAULT NULL,
	"misthos"	integer NOT NULL,
	"tilefono"	varchar(13) NOT NULL,
	"orario"    varchar (30) NOT NULL
	PRIMARY KEY("afm_ypallilou")
);

DROP TABLE IF EXISTS "SERVITOROS";
CREATE TABLE IF NOT EXISTS "SERVITOROS" (
	"afm_ypallilou"	integer NOT NULL,
	"onoma"	varchar(30) NOT NULL,
	"eponimo"	varchar(50) DEFAULT NULL,
	"misthos"	integer NOT NULL,
	"tilefono"	varchar(13) NOT NULL,
	"orario"    varchar (30) NOT NULL
	PRIMARY KEY("afm_ypallilou")
);

DROP TABLE IF EXISTS "PROMITHEYTIS";
CREATE TABLE IF NOT EXISTS "PROMITHEYTIS" (
	"afm"	integer NOT NULL,
	"onoma"	varchar(30) NOT NULL,
	"epitheto"	varchar(50) DEFAULT NULL,
	"tilefono"	integer NOT NULL,
	PRIMARY KEY("afm")
);


DROP TABLE IF EXISTS "YLIKA";
CREATE TABLE IF NOT EXISTS "YLIKA" (
	"id_ylikoy"	integer NOT NULL,
	"onoma"	varchar(30) NOT NULL,
	"katigoria"	varchar(50) DEFAULT NULL,
	"diathesimi_posothta"	integer NOT NULL,
	PRIMARY KEY("id_ylikoy")
);


DROP TABLE IF EXISTS "FAGITO";
CREATE TABLE IF NOT EXISTS "FAGITO" (
	"id_proiontos" INTEGER NOT NULL,
	"onoma" VARCHAR(30) NOT NULL,
	"kostos" REAL NOT NULL,
	"diathesimothta" INTEGER NOT NULL CHECK ("diathesimothta" >= 0),
	"syntagi" varchar(100) NOT NULL,
    "eidika_charaktiristika" varchar(15) NOT NULL,
    PRIMARY KEY("id_proiontos")
);


DROP TABLE IF EXISTS "POTO";
CREATE TABLE IF NOT EXISTS "POTO" (
	"id_proiontos" INTEGER NOT NULL,
	"onoma" VARCHAR(30) NOT NULL,
	"kostos" REAL NOT NULL,
	"diathesimothta" INTEGER NOT NULL CHECK ("diathesimothta" >= 0),
	PRIMARY KEY("id_proiontos")
);

DROP TABLE IF EXISTS "PERILAMBANEI";
CREATE TABLE IF NOT EXISTS "PERILAMBANEI" (
	"id_paraggelias"	integer NOT NULL,
	"id_proiontos"	integer NOT NULL,
	PRIMARY KEY("id_paraggelias"),
	CONSTRAINT "PERILAMBANEI_fk0" FOREIGN KEY("id_paraggelias") REFERENCES "PARAGGELIA"("id_paraggelias") ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT "PERILAMBANEI_fk1" FOREIGN KEY("id_proiontos") REFERENCES "POTO"("id_proiontos") ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT "PERILAMBANEI_fk2" FOREIGN KEY("id_proiontos") REFERENCES "FAGITO"("id_proiontos") ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS "ANALAMBANEI";
CREATE TABLE IF NOT EXISTS "ANALAMBANEI" (
	"id_paraggelias"	integer NOT NULL,
	"afm_ypallilou"	integer NOT NULL,
	PRIMARY KEY("id_paraggelias"),
	CONSTRAINT "ANALAMBANEI_fk0" FOREIGN KEY("id_paraggelias") REFERENCES "PARAGGELIA"("id_paraggelias") ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT "ANALAMBANEI_fk1" FOREIGN KEY("afm_ypallilou") REFERENCES "SERBITOROS"("afm_ypallilou") ON DELETE CASCADE ON UPDATE CASCADE,
);

DROP TABLE IF EXISTS "EFODIAZEI";
CREATE TABLE IF NOT EXISTS "EFODIAZEI" (
	"afm"	integer NOT NULL,
	"id_ylikoy"	integer NOT NULL,
	PRIMARY KEY("id_ylikoy", "afm"),
	CONSTRAINT "EFODIAZEI_fk0" FOREIGN KEY("afm") REFERENCES "PROMITHEYTIS"("afm") ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT "EFODIAZEI_fk1" FOREIGN KEY("id_ylikoy") REFERENCES "YLIKA"("id_ylikoy") ON DELETE CASCADE ON UPDATE CASCADE,
);

DROP TABLE IF EXISTS "PROMITHEVEI";
CREATE TABLE IF NOT EXISTS "PROMITHEVEI" (
	"afm"	integer NOT NULL,
	"id_proiontos"	integer NOT NULL,
	"imer_paradosis" datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
	PRIMARY KEY("afm", "id_proiontos"),
	CONSTRAINT "PROMITHEVEI_fk0" FOREIGN KEY("afm") REFERENCES "PROMITHEYTIS"("afm") ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT "PROMITHEVEI_fk1" FOREIGN KEY("id_proiontos") REFERENCES "POTO"("id_proiontos") ON DELETE CASCADE ON UPDATE CASCADE,
);