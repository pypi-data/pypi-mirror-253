# lapa_database_structure

## about

database structure layer for my personal server.

## installation

> pip install lapa_database_structure

## usage

### to add a new database

- create a package with package name as database name.

### to add a new schema

- add package in database_name package with schema name as package name.

### to add a new table

- create /database_name/schema_name/tables.py file if not already created.
- create class corresponding to your new table add in /database_name/schema_name/tables.py file.

### to add default data in table

- append row objects containing your default data to the data_to_insert list inside the
  /database_name/schema_name/tables.py file.

**do not forget to add new database_names, schema_names and/or table_names to main.py enums to make it accessible
through api calls.**

## configs

None

## env

- python>=3.12.0

## changelog

### v0.0.3

- Changed package name to lapa_database_structure.

### v0.0.2

- Update table for file_storage -> File.

### v0.0.1

- initial implementation.

## Feedback is appreciated. Thank you!
