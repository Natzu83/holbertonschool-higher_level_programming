-- A script that creates the database hbtn_0d_usa and the table states
-- If the table states already exists, the script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id int AUTO_INCREMENT NOT NULL UNIQUE,
    name varchar(256) NOT NULL,
    PRIMARY KEY (id)
);