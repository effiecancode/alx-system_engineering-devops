-- SQL Script to create a databases and table(web-01 and web-02).

-- Create a new database.
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;

-- Create new table.
DROP TABLE IF EXISTS nexus6;
CREATE TABLE nexus6 (
	id INT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);

INSERT INTO nexus6 (id, name) VALUES (1, 'effiecancode');

GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
