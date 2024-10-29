-- List records with score >= 10
-- First, make sure we have the right environment
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- Now list all records with score >= 10
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;