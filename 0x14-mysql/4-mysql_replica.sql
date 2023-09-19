-- MySQL script to start replication on a replica server

CHANGE MASTER TO
    MASTER_HOST='52.87.155.27',
    MASTER_USER='replica_user',
    MASTER_PASSWORD='replica_user_pwd',
    MASTER_LOG_FILE='mysql-bin.000001',
    MASTER_LOG_POS=154;

START SLAVE;
SHOW SLAVE STATUS\G;
