#!/bin/bash

# Créer le répertoire du projet
mkdir -p python-object_relational_mapping

# Se déplacer dans le répertoire
cd python-object_relational_mapping

# Créer tous les fichiers Python nécessaires
for i in {0..14}; do
    case $i in
        0) echo '#!/usr/bin/python3
"""Script that lists all states"""' > 0-select_states.py;;
        1) echo '#!/usr/bin/python3
"""Script that lists states starting with N"""' > 1-filter_states.py;;
        2) echo '#!/usr/bin/python3
"""Script that takes argument and lists states"""' > 2-my_filter_states.py;;
        3) echo '#!/usr/bin/python3
"""Script safe from SQL injection"""' > 3-my_safe_filter_states.py;;
        4) echo '#!/usr/bin/python3
"""Script that lists all cities"""' > 4-cities_by_state.py;;
        5) echo '#!/usr/bin/python3
"""Script that lists cities of a state"""' > 5-filter_cities.py;;
        6) echo '#!/usr/bin/python3
"""Contains State class and Base"""' > model_state.py;;
        7) echo '#!/usr/bin/python3
"""Lists all State objects"""' > 7-model_state_fetch_all.py;;
        8) echo '#!/usr/bin/python3
"""Prints first State object"""' > 8-model_state_fetch_first.py;;
        9) echo '#!/usr/bin/python3
"""Lists States containing letter a"""' > 9-model_state_filter_a.py;;
        10) echo '#!/usr/bin/python3
"""Prints State object with name passed"""' > 10-model_state_my_get.py;;
        11) echo '#!/usr/bin/python3
"""Adds State object Louisiana"""' > 11-model_state_insert.py;;
        12) echo '#!/usr/bin/python3
"""Changes name of State object"""' > 12-model_state_update_id_2.py;;
        13) echo '#!/usr/bin/python3
"""Deletes State objects with letter a"""' > 13-model_state_delete_a.py;;
        14) echo '#!/usr/bin/python3
"""Contains City class"""' > model_city.py
            echo '#!/usr/bin/python3
"""Prints all City objects"""' > 14-model_city_fetch_by_state.py;;
    esac
done

# Rendre tous les fichiers exécutables
chmod +x *.py

# Créer le README.md
echo "# Python - Object-relational mapping

## Description
Project about ORM (Object-Relational Mapping) with Python, MySQL and SQLAlchemy.

## Requirements
* Python 3.8.5
* MySQL 8.0
* MySQLdb 2.0.x
* SQLAlchemy 1.4.x" > README.md

echo "✨ Environnement magique créé ! 🎭"