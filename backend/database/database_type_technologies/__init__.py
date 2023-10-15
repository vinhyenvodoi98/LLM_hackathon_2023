from database.database_type_technologies.amazon_aurora import amazon_aurora
from database.database_type_technologies.cloud_sql import cloud_sql
from database.database_type_technologies.firestore import firestore
from database.database_type_technologies.mariadb import mariadb
from database.database_type_technologies.microsoft_sql_server import microsoft_sql_server
from database.database_type_technologies.mysql import mysql
from database.database_type_technologies.postgresql import postgresql
from database.database_type_technologies.tidb import tidb
from database.database_type_technologies.timescaledb import timescaledb

all_data = [
    mysql, postgresql, tidb,
    mariadb, timescaledb, microsoft_sql_server,
    amazon_aurora, cloud_sql, firestore
]
