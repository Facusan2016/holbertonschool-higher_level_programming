-- Write a script that creates the table unique_id on your MySQL server.

-- The script itself

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(256) NOT NULL
);
