-- List records with name value
-- First, make sure we have the right environment
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- List all records with name value, ordered by descending score
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;