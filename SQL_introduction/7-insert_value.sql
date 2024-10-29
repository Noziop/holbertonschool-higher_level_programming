-- Insert a new row in first_table
-- First, make sure we have the right environment
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
-- Insert the new row with id = 89 and name = "Best School"
INSERT INTO first_table (id, name) VALUES (89, "Best School");