#!/bin/bash

MYSQL_USER="your_mysql_user"
MYSQL_PASSWORD="your_mysql_password"
DATABASE_NAME="db_0"

# Check if the database already exists
DB_EXISTS=$(mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES LIKE '$DATABASE_NAME';" | grep "$DATABASE_NAME")

# If the database doesn't exist, create it
if [ -z "$DB_EXISTS" ]; then
    mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "CREATE DATABASE IF NOT EXISTS $DATABASE_NAME;"
    echo "Database $DATABASE_NAME created successfully."
else
    echo "Database $DATABASE_NAME already exists. No action taken."
fi
