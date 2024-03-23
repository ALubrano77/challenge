-- public.dataproperties definition
CREATE TABLE IF NOT EXISTS dataproperties (
	"ID" int4 NULL,
	"Position" int4 NULL,
	"ParentID" int4 NULL,
	"Type" varchar(50) NULL,
	"Key" varchar(50) NULL,
	"Title" varchar(50) NULL,
	"Description" varchar(1024) NULL,
	"ReleasePolicy" varchar(50) NULL,
	"Datatype" varchar(50) NULL,
	"Unit" varchar(50) NULL,
	"Decimals" int4 NULL,
	"Default" varchar(50) NULL
);


-- public.margins definition
CREATE TABLE IF NOT EXISTS margins (
	"Key" varchar(50) NOT NULL,
	"Title" varchar(50) NULL,
	"Description" varchar(128) NULL,
	CONSTRAINT margins_pk PRIMARY KEY ("Key")
);


-- public.periods definition
CREATE TABLE IF NOT EXISTS periods (
	"Key" varchar(50) NOT NULL,
	"Title" int4 NULL,
	"Description" varchar(50) NULL,
	CONSTRAINT periods_pk PRIMARY KEY ("Key")
);


-- public.population definition
CREATE TABLE IF NOT EXISTS population (
	"Key" varchar(50) NOT NULL,
	"Title" varchar(50) NULL,
	"Description" varchar(50) NULL,
	CONSTRAINT population_pk PRIMARY KEY ("Key")
);


-- public.regioncharacteristics definition
CREATE TABLE IF NOT EXISTS regioncharacteristics (
	"Key" varchar(50) NOT NULL,
	"Title" varchar(50) NULL,
	"Description" varchar(256) NULL,
	CONSTRAINT regioncharacteristics_pk PRIMARY KEY ("Key")
);


-- public.tableinfos definition
CREATE TABLE IF NOT EXISTS tableinfos (
	"ID" int4 NULL,
	"Title" varchar(128) NULL,
	"ShortTitle" varchar(50) NULL,
	"Identifier" varchar(50) NULL,
	"Summary" varchar(128) NULL,
	"Modified" varchar(50) NULL,
	"ReasonDelivery" varchar(50) NULL,
	"ExplanatoryText" varchar(50) NULL,
	"Language" varchar(50) NULL,
	"Catalog" varchar(50) NULL,
	"Frequency" varchar(50) NULL,
	"Period" varchar(50) NULL,
	"ShortDescription" varchar(1024) NULL,
	"Description" varchar(8192) NULL,
	"DefaultPresentation" varchar(128) NULL,
	"DefaultSelection" varchar(1024) NULL,
	"GraphTypes" varchar(50) NULL,
	"OutputStatus" varchar(50) NULL,
	"Source" varchar(50) NULL,
	"MetaDataModified" varchar(50) NULL,
	"SearchPriority" int4 NULL
);


-- public.travelmodes definition
CREATE TABLE IF NOT EXISTS travelmodes (
	"Key" varchar(50) NOT NULL,
	"Title" varchar(50) NULL,
	"Description" varchar(512) NULL,
	CONSTRAINT travelmodes_pk PRIMARY KEY ("Key")
);


-- public.travelmotives definition
CREATE TABLE IF NOT EXISTS travelmotives (
	"Key" varchar(50) NOT NULL,
	"Title" varchar(50) NULL,
	"Description" varchar(512) NULL,
	CONSTRAINT travelmotives_pk PRIMARY KEY ("Key")
);


-- public."84710ENG_UntypedDataSet" definition
CREATE TABLE IF NOT EXISTS "84710ENG_UntypedDataSet" (
	"ID" int4 NULL,
	"TravelMotives" varchar(50) NULL,
	"Population" varchar(50) NULL,
	"TravelModes" varchar(50) NULL,
	"Margins" varchar(50) NULL,
	"RegionCharacteristics" varchar(50) NULL,
	"Periods" varchar(50) NULL,
	"Trips_1" varchar(50) NULL,
	"DistanceTravelled_2" varchar(50) NULL,
	"TimeTravelled_3" varchar(50) NULL,
	"Trips_4" varchar(50) NULL,
	"DistanceTravelled_5" varchar(50) NULL,
	"TimeTravelled_6" varchar(50) NULL,
	CONSTRAINT "84710ENG_UntypedDataSet_margins_FK" FOREIGN KEY ("Margins") REFERENCES margins("Key"),
	CONSTRAINT "84710ENG_UntypedDataSet_periods_FK" FOREIGN KEY ("Periods") REFERENCES periods("Key"),
	CONSTRAINT "84710ENG_UntypedDataSet_population_FK" FOREIGN KEY ("Population") REFERENCES population("Key"),
	CONSTRAINT "84710ENG_UntypedDataSet_regioncharacteristics_FK" FOREIGN KEY ("RegionCharacteristics") REFERENCES regioncharacteristics("Key"),
	CONSTRAINT "84710ENG_UntypedDataSet_travelmodes_FK" FOREIGN KEY ("TravelModes") REFERENCES travelmodes("Key"),
	CONSTRAINT "84710ENG_UntypedDataSet_travelmotives_FK" FOREIGN KEY ("TravelMotives") REFERENCES travelmotives("Key")
);
