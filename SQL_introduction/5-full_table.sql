-- Print full description of first_table
-- 1. create a database hbtn_0c_0
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- 2. create the table first_table
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
-- Print full description of first_table
SHOW CREATE TABLE first_table;