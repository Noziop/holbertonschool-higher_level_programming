#!/bin/bash

# 🧙‍♀️ Create SQL More Queries Project Structure 🔮

# Create README
echo "# SQL - More queries

## Description
Advanced SQL queries and MySQL user management - Learning privileges, joins, and constraints.

## Requirements
- Ubuntu 20.04 LTS or 22.04 LTS
- MySQL 8.0
- All SQL keywords should be in uppercase

## Files
- 0-privileges.sql : List user privileges
- 1-create_user.sql : Create MySQL user
- 2-create_read_user.sql : Create database and user
- 3-force_name.sql : Create table with NOT NULL
- 4-never_empty.sql : Create table with default value
- 5-unique_id.sql : Create table with UNIQUE
- 6-states.sql : Create database and table with PRIMARY KEY
- 7-cities.sql : Create table with FOREIGN KEY
- 8-cities_of_california_subquery.sql : Use subquery
- 9-cities_by_state_join.sql : Use JOIN
- 10-genre_id_by_show.sql : Use JOIN with multiple tables
- 11-genre_id_all_shows.sql : Use LEFT JOIN
- 12-no_genre.sql : Use WHERE NULL
- 13-count_shows_by_genre.sql : Use COUNT
- 14-my_genres.sql : Multiple JOINs
- 15-comedy_only.sql : Complex query
- 16-shows_by_genre.sql : Full table relationships" > README.md

# Create SQL files with their comments
for i in {0..16}; do
    case $i in
        0) echo "-- List privileges of MySQL users user_0d_1 and user_0d_2" > 0-privileges.sql;;
        1) echo "-- Create MySQL server user user_0d_1 with all privileges" > 1-create_user.sql;;
        2) echo "-- Create database and user with SELECT privilege" > 2-create_read_user.sql;;
        3) echo "-- Create table force_name with NOT NULL constraint" > 3-force_name.sql;;
        4) echo "-- Create table id_not_null with default value" > 4-never_empty.sql;;
        5) echo "-- Create table unique_id with UNIQUE constraint" > 5-unique_id.sql;;
        6) echo "-- Create database and table states with PRIMARY KEY" > 6-states.sql;;
        7) echo "-- Create table cities with FOREIGN KEY" > 7-cities.sql;;
        8) echo "-- List cities of California using subquery" > 8-cities_of_california_subquery.sql;;
        9) echo "-- List cities with state names using JOIN" > 9-cities_by_state_join.sql;;
        10) echo "-- List shows with at least one genre linked" > 10-genre_id_by_show.sql;;
        11) echo "-- List all shows with their genres" > 11-genre_id_all_shows.sql;;
        12) echo "-- List shows without genres" > 12-no_genre.sql;;
        13) echo "-- List genres and number of shows" > 13-count_shows_by_genre.sql;;
        14) echo "-- List genres of show Dexter" > 14-my_genres.sql;;
        15) echo "-- List Comedy shows" > 15-comedy_only.sql;;
        16) echo "-- List shows and their genres" > 16-shows_by_genre.sql;;
    esac
done

echo "Project structure created! 🎉"