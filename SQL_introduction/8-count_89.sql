-- Count records with id = 89
-- First, make sure we have the right environment
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
-- Count records with id = 89
SELECT COUNT(*) FROM first_table WHERE id = 89;