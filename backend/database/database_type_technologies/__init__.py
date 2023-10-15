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

general_purpose_sql = [
    mysql, postgresql, tidb,
    mariadb, microsoft_sql_server,
    amazon_aurora, cloud_sql
]

general_purpose_no_sql = [
    firestore
]

time_series = [
    timescaledb
]

in_memory = [

]
