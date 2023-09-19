-- MySQL script to start replication on a replica server

CHANGE MASTER TO
    MASTER_HOST='34.232.72.158',
    MASTER_USER='replica_user',
    MASTER_PASSWORD='effie254',
    MASTER_LOG_FILE='mysql-bin.000002',
    MASTER_LOG_POS=154;

START SLAVE;
SHOW SLAVE STATUS\G;
