-- Update Bob's score
-- First, make sure we have the right environment
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- Update Bob's score to 10 using only his name
UPDATE second_table SET score = 10 WHERE name = "Bob";