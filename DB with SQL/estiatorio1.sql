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

