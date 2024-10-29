-- List records by score
-- First, make sure we have the right environment
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- List all records ordered by score
SELECT score, name FROM second_table ORDER BY score DESC;