-- SQL Script to create a user and databases(web-01 and web-02).

-- create user 'holberton_user'
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- Grant privileges to the user.
GRANT SELECT, REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

-- Flush the new privileges
FLUSH PRIVILEGES;

-- Create another user.
CREATE USER IF NOT EXISTS 'ubuntu'@'localhost' IDENTIFIED BY 'web@ubuntu';
GRANT ALL PRIVILEGES ON *.* TO 'ubuntu'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
