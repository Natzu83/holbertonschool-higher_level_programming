-- A script that creates the table force_name
-- If the table force_name already exists, then the script should not fail
CREATE TABLE IF NOT EXISTS force_name (
    id int,
    name varchar(256) NOT NULL
);