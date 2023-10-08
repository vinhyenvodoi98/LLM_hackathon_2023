from database.database_type_technologies.big_query import big_query
from database.database_type_technologies.big_table import big_table
from database.database_type_technologies.cassandra import cassandra
from database.database_type_technologies.dynamodb import dynamodb
from database.database_type_technologies.influxdb import influxdb
from database.database_type_technologies.mariadb import mariadb
from database.database_type_technologies.microsoft_sql_server import microsoft_sql_server
from database.database_type_technologies.mongodb import mongodb
from database.database_type_technologies.mysql import mysql
from database.database_type_technologies.neo4j_db import neo4j_db
from database.database_type_technologies.oracle_database import oracle_database
from database.database_type_technologies.postgresql import postgresql
from database.database_type_technologies.redis import redis
from database.database_type_technologies.timescaledb import timescaledb

all_data = [
    big_query, big_table, cassandra,
    dynamodb, influxdb, mariadb,
    microsoft_sql_server, mongodb, mysql,
    neo4j_db, oracle_database, postgresql,
    redis, timescaledb
]
