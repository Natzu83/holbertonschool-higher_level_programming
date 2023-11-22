-- A script that creates the database hbtn_0d_usa and the table of cities
-- If the database hbtn_0d_usa already exists, the script should not fail
-- If the table cities already exists, the script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL UNIQUE,
    state_id INT NOT NULL,
    name varchar(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);