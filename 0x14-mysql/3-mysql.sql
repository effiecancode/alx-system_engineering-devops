-- Creates replica user
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'effie254';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
