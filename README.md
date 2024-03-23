# challenge

# High Level analysis of the requisite

## Data analysis
The metadata file contains several tables DDL and DML without a clear separator.
In the tables data are there are information about dimensions and topics without expliciting FKs.
The first table "TableInfos" contains also a table of contents, data definitions, links, sources.

## solution 1
Considering the input, in particular the metadata.csv file, an industrialized way to proceed should be:
a parser for metadata to create Dimension, TopicGroup, Topic tables with proper PKs, FKs,
an ETL for fimension with data cleansing
an ETL for data with data cleansing and validation

## solution 2
considering also time availability and POC scope the solution will be:
manual DDL creation with idempotency;
an ETL for fimension with data cleansing
an ETL for data

## tool exploration
for ETL several solutions have been explored from off-the-shelf ETL to python frameworks:
airbyte, nifi, airflow
great expectations, polars, pandas



## data ingestion issues

### data cleansing
**during ingestion**
* trim keys
to do both in dims and in fact tables to not break FKs
* rename fields
in lowercase and starting with a char, to simplify query editing
renaming topic 1 measures per day (Trips_1,DistanceTravelled_2,TimeTravelled_3)
renaming topic 2 measures per year (Trips_4,DistanceTravelled_5,TimeTravelled_6)
* trip1 tp

### data casting
**after ingestion, in DB, to not change values before writing**
* to_numeric for measures



