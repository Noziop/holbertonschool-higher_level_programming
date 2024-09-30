#!/bin/bash


# Créer les fichiers Python
touch python-serialization/task_00_basic_serialization.py
touch python-serialization/task_01_pickle.py
touch python-serialization/task_02_csv.py
touch python-serialization/task_03_xml.py

# Créer les fichiers de données d'exemple
echo 'name,age,city
John,28,New York
Alice,24,Los Angeles
Bob,22,Chicago
Eve,30,San Francisco' > python-serialization/data.csv

echo '{"name": "John", "age": 30, "city": "New York"}' > python-serialization/data.json

echo '<?xml version="1.0" encoding="UTF-8"?>
<root>
  <name>John</name>
  <age>28</age>
  <city>New York</city>
</root>' > python-serialization/data.xml

echo "Fichiers créés avec succès dans le répertoire python-serialization"