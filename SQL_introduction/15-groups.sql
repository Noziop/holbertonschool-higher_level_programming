-- List number of records by score
-- First, make sure we have the right environment
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- Group records by score and count them
SELECT score, COUNT(*) as number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;